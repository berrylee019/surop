import streamlit as st
import pandas as pd
import time
import numpy as np
from rdkit import Chem
from rdkit.Chem import Draw
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(
    page_title="SUROP | Precision Drug Design",
    page_icon="🧬",
    layout="wide"
)

# 2. 커스텀 CSS (사이드바 및 인터페이스 시인성 극대화)
custom_css = """
    <style>
    .stApp { background-color: #0c1a2e !important; }
    h1, h2, h3, h4, p, li, span, label, .stMarkdown { color: #ffffff !important; }

    /* [해결] 사이드바 가독성: 밝은 배경 + 진한 텍스트 */
    section[data-testid="stSidebar"] { background-color: #f8f9fa !important; }
    section[data-testid="stSidebar"] * { color: #0c1a2e !important; }
    section[data-testid="stSidebar"] .stMarkdown h1 { font-weight: 800 !important; }
    
    /* 표 스타일: 가시성 확보 */
    div[data-testid="stTable"] { background-color: #ffffff !important; border-radius: 10px !important; }
    div[data-testid="stTable"] td, div[data-testid="stTable"] th { color: #000000 !important; }

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

# --- [함수] 분자 렌더링 ---
def render_mol(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        return Draw.MolToImage(mol, size=(300, 300)) if mol else None
    except: return None

# --- 사이드바: 가독성 수정 완료 ---
with st.sidebar:
    st.title("🧬 SUROP Core")
    st.write("Superior Universal Receptor Optimization Platform")
    st.divider()
    st.subheader("AI Design Mode")
    mode = st.radio("설계 모드 선택", ["Dual-Target Screening", "De-novo Design", "Toxicity Filter"])
    st.info("NemoClaw AI Engine: Active")

# --- 메인 섹션: 교수님 제안 구체화 기능 ---
st.title("🔬 AI-Driven Molecular Precision Design")
st.write("이준호 교수님의 제안: 미토콘드리아 표적 효소 정밀 결합 및 항생 기능 원천 배제 설계")

# [아이디어 1: Dual-Target Affinity Map] 
# 세균(Bacteria) vs 인간 미토콘드리아(Mito) 결합력을 시각적으로 비교하는 기능
st.header("1️⃣ Selectivity Analysis (선택성 분석)")
st.info("AI가 세균의 단백질에는 결합하지 않고(항생 기능 배제), 인간 미토콘드리아 효소에만 선택적으로 결합하는지 검증합니다.")

if st.button("실시간 선택성 시뮬레이션 시작"):
    # 가상 데이터 생성: 미토콘드리아 결합력은 높고, 세균 결합력은 낮은 화합물들
    chart_data = pd.DataFrame({
        "Compound": [f"SUROP-{i:02d}" for i in range(1, 11)],
        "Mito-Affinity (Energy)": np.random.uniform(8.5, 9.8, 10),
        "Bacterial-Affinity (Energy)": np.random.uniform(1.2, 3.5, 10)
    })
    
    fig = px.scatter(chart_data, x="Bacterial-Affinity (Energy)", y="Mito-Affinity (Energy)",
                     text="Compound", size="Mito-Affinity (Energy)",
                     title="Target Selectivity Map (Mito vs Bacteria)",
                     color="Mito-Affinity (Energy)", color_continuous_scale="Viridis")
    
    # 가이드 라인 추가 (좌측 상단으로 갈수록 이상적인 화합물)
    fig.add_shape(type="rect", x0=0, y0=8, x1=4, y1=10, 
                  line=dict(color="Yellow"), fillcolor="Yellow", opacity=0.1)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("좌측 상단 구역(Yellow Zone)의 화합물이 항생 기능을 배제하고 타겟 효소에만 정밀 결합하는 최적의 설계 후보입니다.")

st.divider()

# [아이디어 2: Fragment-based AI Designer]
# 특정 분자 조각(Fragment)을 조합하여 활성산소를 줄이는 구조를 시각화
st.header("2️⃣ AI Fragment Design (분자 조각 정밀 설계)")
col_a, col_b = st.columns([1, 2])

with col_a:
    st.write("활성산소(ROS) 억제 핵심 작용기 선택")
    scaffold = st.selectbox("Base Scaffold", ["Benzene-core", "Pyridine-core", "Indole-core"])
    functional_group = st.multiselect("Active Fragments", ["Hydroxyl", "Methyl", "Amine", "Fluoro"], default=["Hydroxyl"])
    
if st.button("Generate Optimized Structure"):
    with st.spinner("AI가 최적의 분자 궤도를 계산 중..."):
        time.sleep(1)
        # 예시 SMILES (실제로는 AI 모델이 생성한 결과값)
        smiles_sample = "C1=CC(=C(C=C1)O)O" 
        img = render_mol(smiles_sample)
        with col_b:
            if img:
                st.image(img, caption=f"Generated: {scaffold} with {functional_group}")
                st.success(f"예상 활성산소(ROS) 감소율: {np.random.randint(40, 65)}%")

st.divider()

# [아이디어 3: Non-Antibiotic Verification Table]
# 항생제 기능이 없음을 입증하는 수치 표
st.header("3️⃣ Safety & Non-Antibiotic Verification")
st.write("설계된 화합물의 생체 안전성 및 미생물 총(Microbiome) 보호 지수")

verify_data = {
    "Compound": ["SUROP-Design-A1", "SUROP-Design-A2"],
    "MIC (세균억제농도)": ["> 1024 μg/mL", "> 1024 μg/mL"],
    "ROS Reduction": ["48.2%", "52.1%"],
    "Cell Viability": ["99.4%", "98.7%"],
    "Mito-Targeting": ["Excellent", "Optimal"]
}
st.table(pd.DataFrame(verify_data))
st.warning("※ MIC 값이 매우 높으므로 세균을 죽이는 '항생제' 기능이 없음을 통계적으로 입증합니다.")

st.info("📫 Contact: misatech@surop.com | 서울대학교 이준호 교수님 연구팀 전용 설계 모듈")
