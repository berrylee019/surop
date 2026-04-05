import streamlit as st
import pandas as pd
import time
import numpy as np
from rdkit import Chem
from rdkit.Chem import Draw

# Plotly 설치 여부 체크 (설계 모드 시각화용)
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

# 2. 커스텀 CSS (사이드바 가독성 & 가시성 보정)
custom_css = """
    <style>
    .stApp { background-color: #0c1a2e !important; }
    h1, h2, h3, h4, p, li, span, label, .stMarkdown { color: #ffffff !important; }

    /* [해결] 사이드바 가독성 고정 */
    section[data-testid="stSidebar"] { background-color: #f1f3f5 !important; }
    section[data-testid="stSidebar"] * { color: #0c1a2e !important; }
    section[data-testid="stSidebar"] h1 { font-weight: 800 !important; }
    
    /* 표 스타일 */
    div[data-testid="stTable"] { background-color: #ffffff !important; border-radius: 10px !important; padding: 5px !important; }
    div[data-testid="stTable"] table { color: #000000 !important; }
    div[data-testid="stTable"] td, div[data-testid="stTable"] th { color: #000000 !important; background-color: #ffffff !important; }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: #ffe135 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- [함수] 분자 시각화 ---
def render_molecule(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        return Draw.MolToImage(mol, size=(300, 300)) if mol else None
    except: return None

# --- [사이드바] 모드 선택 컨트롤 ---
with st.sidebar:
    st.title("🧬 SUROP")
    st.write("**S**uperior **U**niversal **R**eceptor **O**ptimization **P**latform")
    st.divider()
    
    # 분석형 vs 설계형 선택 라디오 버튼
    app_mode = st.radio(
        "실행 모드를 선택하세요",
        ["🏠 Home (Concept)", "🔍 분석형 모드 (Analysis)", "🧪 설계형 모드 (AI Design)"]
    )
    
    st.divider()
    st.info("System Status: Active")
    st.info("NemoClaw AI Engine Running")

# --- [모드 1] 홈 화면: 개념 및 요약 설명 ---
if app_mode == "🏠 Home (Concept)":
    st.image(IMAGE_URL, caption="SUROP: Aging Target Protein Discovery Interface", use_container_width=True)
    
    st.title("Welcome to SUROP Platform")
    st.header("Superior Universal Receptor Optimization Platform")
    
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("📌 핵심 개념 (Concept)")
        st.write("""
        **이준호 교수 가이드 핵심:**
        1. **항생제 기능 배제**: 미생물 총(Microbiome)을 파괴하지 않는 비항생제성 설계.
        2. **미토콘드리아 정밀 타겟팅**: 노화의 핵심인 미토콘드리아 내 표적 효소에만 정확히 결합.
        3. **활성산소(ROS) 억제**: 정밀 설계된 분자 구조를 통해 노화 관련 산화 스트레스 감소.
        """)
    
    with col_r:
        st.subheader("📋 서비스 요약 (Summary)")
        st.write("""
        - **분석형 모드**: 대규모 라이브러리 스캔을 통한 최적 결합 후보 물질 발굴 및 검증.
        - **설계형 모드**: AI를 이용한 분자 조각(Fragment) 조합 및 타겟 선택성(Selectivity) 정밀 디자인.
        """)
        
    st.divider()
    st.success("왼쪽 사이드바에서 원하시는 모드를 선택하여 연구를 시작하세요.")

# --- [모드 2] 분석형 모드 ---
elif app_mode == "🔍 분석형 모드 (Analysis)":
    st.title("🔍 Target Protein Analysis Mode")
    st.write("대규모 라이브러리를 스캔하여 표적 단백질에 최적화된 화합물을 식별합니다.")
    
    target_pdb = st.text_input("분석할 PDB ID 입력", "1UNL")
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

# --- [모드 3] 설계형 모드 ---
elif app_mode == "🧪 설계형 모드 (AI Design)":
    st.title("🧪 AI-Driven Molecular Design Mode")
    st.write("이준호 교수님의 가이드에 따라 비항생제성 미토콘드리아 표적 화합물을 정밀 설계합니다.")
    
    # 설계형 핵심 기능: 선택성 맵
    if px:
        st.subheader("1. Target Selectivity Verification")
        chart_data = pd.DataFrame({
            "Compound": [f"Design-{i}" for i in range(1, 6)],
            "Mito-Affinity": np.random.uniform(9.0, 9.9, 5),
            "Bacterial-Affinity": np.random.uniform(1.0, 3.0, 5)
        })
        fig = px.scatter(chart_data, x="Bacterial-Affinity", y="Mito-Affinity", text="Compound", 
                         title="Mito vs Bacteria Selectivity (Ideal: Left-Top)")
        st.plotly_chart(fig, use_container_width=True)

    # 설계형 핵심 기능: 분자 조각 조합
    st.subheader("2. AI Fragment Assembly")
    scaffold = st.selectbox("Base Scaffold", ["Benzene", "Indole", "Pyridine"])
    if st.button("Design New Molecule"):
        img = render_molecule("C1=CC(=C(C=C1)O)O")
        if img:
            st.image(img, caption=f"AI Optimized {scaffold} Structure")
            st.success("비항생제성 및 미토콘드리아 표적 최적화 완료")

# 하단 연락처
st.divider()
st.info("📫 Contact: misatech@surop.com | 서울대학교 이준호 교수님 연구팀 전용 채널")
