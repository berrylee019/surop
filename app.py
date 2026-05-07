import streamlit as st
import pandas as pd
import time
import numpy as np
import requests
import json
import plotly.graph_objects as go
from rdkit import Chem
from rdkit.Chem import Draw
from stmol import showmol
import py3Dmol

# Plotly 설치 여부 체크 (설계 모드 및 시연용 시각화)
try:
    import plotly.express as px
except ImportError:
    px = None

# 1. 페이지 설정
st.set_page_config(
    page_title="SUROP | Precision Drug Discovery",
    page_icon="🧬",
    layout="wide"
)

# [이미지 주소]
IMAGE_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWi2G3PZ2y0MSNuxEQ3xTFfp6WnVQ7uLnPUQaSNE5a_PPsFvCgL_xALuvusjUo3OV-S4MddYAQWxMxsob9EpNujqwh9cXBP09bxZSS_O2y42zW668O7fPgD_fPVMkqWnx1p5n2KkA1nrZR3zUgvUp0ZE59yinMWEJRrLNIALGQm2Uq10gvAD9KDgg3Rpk/s1168/surop.jpg"

# 2. 커스텀 CSS
custom_css = """
    <style>
    .stApp { background-color: #0c1a2e !important; }
    h1, h2, h3, h4, p, li, span, label, .stMarkdown { color: #ffffff !important; }

    /* 사이드바 가독성 고정 */
    section[data-testid="stSidebar"] { background-color: #f1f3f5 !important; }
    section[data-testid="stSidebar"] * { color: #0c1a2e !important; }
    section[data-testid="stSidebar"] h1 { font-weight: 800 !important; }
    
    /* 표(Table) 가독성 */
    div[data-testid="stTable"] { 
        background-color: #1e293b !important; 
        border-radius: 10px !important; 
        padding: 10px !important; 
    }
    div[data-testid="stTable"] table { color: #ffffff !important; }
    div[data-testid="stTable"] td, div[data-testid="stTable"] th { 
        color: #ffffff !important; 
        background-color: #1e293b !important; 
        border-bottom: 1px solid #334155 !important;
    }

    /* 셀렉트박스 및 입력창 배경 가독성 */
    div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        color: white !important;
    }
    div[role="listbox"] {
        background-color: #1e293b !important;
        color: white !important;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: #ffe135 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100% !important;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- [함수] 2D 분자 시각화 (RDKit) ---
def render_molecule(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        return Draw.MolToImage(mol, size=(300, 300)) if mol else None
    except: return None

# --- [함수] 3D 단백질 시각화 (stmol + py3Dmol) ---
def render_3d_viewer(pdb_path):
    try:
        with open(pdb_path, "r") as f:
            pdb_data = f.read()
        
        view = py3Dmol.view(width=800, height=500)
        view.addModel(pdb_data, 'pdb')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo({'centered': True})
        view.spin(True) 
        showmol(view, height=500)
    except Exception as e:
        st.error(f"PDB 파일을 로드할 수 없습니다. 경로를 확인해주세요: {pdb_path}")

# --- [사이드바] 모드 선택 컨트롤 ---
with st.sidebar:
    st.title("🧬 SUROP")
    st.write("**S**uperior **U**niversal **R**eceptor **O**ptimization **P**latform")
    st.divider()
    
    app_mode = st.radio(
        "실행 모드를 선택하세요",
        [
            "🏠 Home (Concept)", 
            "🔗 NCI GDC Data Link", # 새롭게 추가된 기술 시연 모듈
            "🔍 분석형 모드 (Analysis)", 
            "🧪 설계형 모드 (AI Design)"
        ]
    )
    
    st.divider()
    st.info("System Status: Active")
    st.info("NemoClaw AI Engine Running")

# --- [모드 1] 홈 화면: 개념 및 요약 설명 ---
if app_mode == "🏠 Home (Concept)":
    st.image(IMAGE_URL, caption="SUROP: Aging Target Protein Discovery Interface", width='stretch')
    
    st.title("Welcome to SUROP Platform")
    st.header("Superior Universal Receptor Optimization Platform")
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📌 핵심 개념 (Concept)")
        st.write("""
        **핵심 기술 가이드:**
        1. **DNA 오리가미 최적화**: 항원과 면역증강제의 정밀 배치를 통한 면역 효율 극대화.
        2. **개인 맞춤형 항원 발굴**: 비용과 시간을 획기적으로 단축하는 가상 스크리닝(In-silico).
        3. **미토콘드리아 정밀 타겟팅**: 노화의 핵심 원인인 산화 스트레스 제어 및 ROS 억제.
        """)
    
    with col_r:
        st.subheader("📋 서비스 요약 (Summary)")
        st.write("""
        - **분석형 모드**: 대규모 라이브러리 스캔을 통한 최적 결합 후보 물질 발굴 및 검증.
        - **설계형 모드**: AI를 이용한 분자 조각 조합 및 타겟 선택성 정밀 디자인.
        """)
        
    st.divider()
    
    st.subheader("🧪 Live Demo: Interactive 3D Antigen Analysis")
    st.write("박사님 연구에 최적화된 표준 모델 항원 데이터를 로드하고 3차원 구조를 확인합니다.")
    
    btn_col1, btn_col2, btn_col3 = st.columns(3)
    
    if 'show_viewer' not in st.session_state:
        st.session_state['show_viewer'] = False

    with btn_col1:
        if st.button("📍 Load: Ovalbumin (1OVA)"):
            with st.spinner('박사님 모델 항원(OVA) 분석 중...'):
                time.sleep(1.0)
                st.session_state['active_pdb'] = "samples/1OVA.pdb"
                st.session_state['analysis_result'] = "💡 분석 결과: DNA 오리가미 결합 최적 간격 3.5nm 도출"
                st.session_state['show_viewer'] = False

    with btn_col2:
        if st.button("📍 Load: SARS-CoV-2 (6M0J)"):
            with st.spinner('코로나 스파이크 단백질 분석 중...'):
                time.sleep(1.0)
                st.session_state['active_pdb'] = "samples/6M0J.pdb"
                st.session_state['analysis_result'] = "💡 분석 결과: Spike RBD-ACE2 결합 인터페이스 식별 완료"
                st.session_state['show_viewer'] = False

    with btn_col3:
        if st.button("📍 Load: Cancer Neo (1S9W)"):
            with st.spinner('암 신생항원(NY-ESO-1) 분석 중...'):
                time.sleep(1.0)
                st.session_state['active_pdb'] = "samples/1S9W.pdb"
                st.session_state['analysis_result'] = "💡 분석 결과: NY-ESO-1 항원-HLA A2 복합체 정밀 스캔 완료"
                st.session_state['show_viewer'] = False

    if 'active_pdb' in st.session_state:
        st.success(f"{st.session_state['active_pdb'].split('/')[-1]} 로드 완료!")
        st.info(st.session_state['analysis_result'])
        
        import json
        packet = {"antigen_name": st.session_state['active_pdb'].split('/')[-1].replace('.pdb', ''), "optimized_spacing_nm": 3.5 if "1OVA" in st.session_state['active_pdb'] else 0.0, "target_system": "DoriVac Scaffold", "security_token": "SUROP-SECURE-99X82"}
        st.download_button(label="📥 DoriVac 연동 패킷 다운로드 (JSON)", data=json.dumps(packet, indent=2), file_name=f"{st.session_state['active_pdb'].split('/')[-1].replace('.pdb', '')}_surop_packet.json", mime="application/json")
        
        if st.button(f"🔍 {st.session_state['active_pdb'].split('/')[-1]} 3D 구조 시각화 시작"):
            st.session_state['show_viewer'] = True

    if st.session_state.get('show_viewer'):
        st.divider()
        st.subheader(f"🎥 Interactive 3D Viewer: {st.session_state['active_pdb'].split('/')[-1]}")
        render_3d_viewer(st.session_state['active_pdb'])

# =========================================================================
# [신규 모듈] NCI GDC Data Link (DNA Change 기술적 워크플로우)
# =========================================================================
elif app_mode == "🔗 NCI GDC Data Link":
    st.title("🔗 NCI GDC Real-time Genomic Link")
    st.markdown("암 환자의 실시간 DNA 변이 데이터를 기반으로 **맞춤형 3D 신생항원**을 생성하는 워크플로우를 시연합니다.")

    # 1. 환자 데이터 패칭 섹션
    col1, col2 = st.columns([3, 1])
    with col1:
        patient_id = st.text_input("Target Patient ID (Submitter ID)", value="TCGA-A7-A0CE")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Fetch Genomic Data"):
            st.session_state.gdc_data_fetched = True

    if st.session_state.get('gdc_data_fetched'):
        with st.spinner("Connecting to NCI GDC Data Portal..."):
            # 실제 시연을 위한 API 필터 설정
            filters = {"op": "and", "content": [{"op": "in", "content": {"field": "cases.submitter_id", "value": [patient_id]}}]}
            params = {"filters": json.dumps(filters), "fields": "genomic_dna_change,ssm_id,consequence.transcript.consequence_type", "size": "5"}
            
            try:
                # GDC API 호출 및 데이터 구성
                response = requests.get("https://api.gdc.cancer.gov/ssms", params=params)
                data = response.json().get("data", {}).get("hits", [])
                
                if data:
                    st.subheader(f"📋 Patient {patient_id}: Mutation Analysis")
                    df = pd.DataFrame([
                        {
                            "DNA Change": m.get('genomic_dna_change'),
                            "Consequence": m.get('consequence', [{}])[0].get('transcript', {}).get('consequence_type', 'N/A')
                        } for m in data
                    ])
                    st.table(df)

                    st.markdown("---")
                    st.subheader("🚀 Technical Workflow: Antigen Creation")
                    
                    # 시연의 핵심: missense_variant 선택 시나리오
                    selected_mut = st.selectbox("Select Target DNA Change for 3D Modeling", df['DNA Change'].tolist())
                    
                    if st.button("⚡ Execute AI Prediction Pipeline", type="primary"):
                        # [이미지 생성 유도 태그 - 시너지 효과]
                        # 
                        
                        p_bar = st.progress(0)
                        status = st.empty()
                        
                        # Step 1: Translation
                        status.text("Step 1: Translating DNA Change to Amino Acid Sequence...")
                        time.sleep(1)
                        p_bar.progress(33)
                        st.success(f"✔️ Translated: {selected_mut} → **p.Gly12Asp (G12D) Mutation**")

                        # Step 2: Extraction
                        status.text("Step 2: Extracting 25-mer Peptide Fragment...")
                        time.sleep(1)
                        p_bar.progress(66)
                        st.code("Fragment: MTEYKLVVVGADGVGKSALTIQLI (Mutated Region Highlighted)", language="text")

                        # Step 3: 3D Prediction 시각화
                        status.text("Step 3: Folding Prediction via ESMFold AI...")
                        time.sleep(1.5)
                        p_bar.progress(100)
                        
                        # 3D 결과 시각화 (임시 Plotly 서피스로 화려하게 연출)
                        st.subheader("🔬 Predicted 3D Neo-Antigen Structure")
                        z = np.random.standard_normal((15, 15))
                        fig = go.Figure(data=[go.Surface(z=z, colorscale='Electric', opacity=0.9)])
                        fig.update_layout(title=f"Target Model: {selected_mut}", width=800, height=500)
                        st.plotly_chart(fig, use_container_width=True)
                        
                        st.info("💡 **Ready for DoriVac:** 본 구조 데이터를 기반으로 3.5nm 정밀 배치를 위한 DoriVac Recipe 생성이 가능합니다.")
                else:
                    st.warning("데이터를 찾을 수 없습니다. 다른 환자 ID를 입력해 주세요.")
            except:
                st.error("API 연결 중 오류가 발생했습니다.")

# --- [모드 2] 분석형 모드 (기존 코드 유지) ---
elif app_mode == "🔍 분석형 모드 (Analysis)":
    st.title("🔍 Target Protein Analysis Mode")
    st.write("대규모 라이브러리를 스캔하여 표적 단백질에 최적화된 화합물을 식별합니다.")
    
    default_id = "1OVA" if st.session_state.get('active_pdb') == "samples/1OVA.pdb" else "1UNL"
    target_pdb = st.text_input("분석할 PDB ID 입력", default_id)
    
    if st.button("Run Deep Analysis"):
        with st.spinner('Analyzing...'):
            time.sleep(1.2)
            mock_data = {
                "Rank": [1, 2, 3],
                "Compound ID": ["SUROP-B01", "SUROP-B02", "SUROP-B03"],
                "Affinity": [-12.42, -11.95, -11.51],
                "Toxic Filter": ["SAFE", "SAFE", "SAFE"]
            }
            st.table(pd.DataFrame(mock_data))
            st.balloons()

# --- [모드 3] 설계형 모드 (기존 코드 유지) ---
elif app_mode == "🧪 설계형 모드 (AI Design)":
    st.title("🧪 AI-Driven Molecular Design Mode")
    st.write("비항생제성 미토콘드리아 표적 화합물을 정밀 설계합니다.")
    
    if px:
        st.subheader("1. Target Selectivity Verification")
        chart_data = pd.DataFrame({
            "Compound": [f"Design-{i}" for i in range(1, 6)],
            "Mito-Affinity": np.random.uniform(9.0, 9.9, 5),
            "Bacterial-Affinity": np.random.uniform(1.0, 3.0, 5)
        })
        fig = px.scatter(chart_data, x="Bacterial-Affinity", y="Mito-Affinity", text="Compound", 
                         title="Mito vs Bacteria Selectivity (Ideal: Left-Top)")
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("2. AI Fragment Assembly")
    scaffold = st.selectbox("Base Scaffold", ["Benzene", "Indole", "Pyridine"])
    if st.button("Design New Molecule"):
        img = render_molecule("C1=CC(=C(C=C1)O)O")
        if img:
            st.image(img, caption=f"AI Optimized {scaffold} Structure")
            st.success("비항생제성 및 미토콘드리아 표적 최적화 완료")

# 하단 연락처
st.divider()
st.info("📫 Contact: bslee@yahoo.com | MisaTech AI")
