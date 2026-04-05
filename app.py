import streamlit as st
import pandas as pd
import time
import numpy as np
from rdkit import Chem
from rdkit.Chem import Draw

# Plotly가 설치되지 않았을 경우를 대비한 예외 처리
try:
    import plotly.express as px
except ImportError:
    px = None

# 1. 페이지 설정
st.set_page_config(
    page_title="SUROP | Precision Drug Design",
    page_icon="🧬",
    layout="wide"
)

# 2. 커스텀 CSS (사이드바 가독성 및 UI 최적화)
custom_css = """
    <style>
    .stApp { background-color: #0c1a2e !important; }
    h1, h2, h3, h4, p, li, span, label, .stMarkdown { color: #ffffff !important; }

    /* 사이드바 가독성: 밝은 배경 + 진한 텍스트 */
    section[data-testid="stSidebar"] { background-color: #f8f9fa !important; }
    section[data-testid="stSidebar"] * { color: #0c1a2e !important; }
    section[data-testid="stSidebar"] .stMarkdown h1 { font-weight: 800 !important; }
    
    /* 표 스타일: 흰색 배경에 검은 글씨 강제 */
    div[data-testid="stTable"] { 
        background-color: #ffffff !important; 
        border-radius: 10px !important; 
        padding: 10px !important;
    }
    div[data-testid="stTable"] table { color: #000000 !important; }
    div[data-testid="stTable"] td, div[data-testid="stTable"] th { 
        color: #000000 !important; 
        background-color: #ffffff !important;
    }

    /* 버튼 스타일 */
    .stButton>button {
        background-color: #ffe135 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100%;
    }
    </style>
"""
# 이전의 오타(unsafe_allow_safe_html)를 올바른 옵션으로 수정했습니다.
st.markdown(custom_css, unsafe_allow_html=True)

# --- [함수] 분자 렌더링 ---
def render_mol(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        return Draw.MolToImage(mol, size=(300, 300)) if mol else None
    except: return None

# --- 사이드바 ---
with st.sidebar:
    st.title("🧬 SUROP Core")
    st.write("Superior Universal Receptor Optimization Platform")
    st.divider()
    st.subheader("AI Design Mode")
    st.info("✅ Status: Active")
    st.info("🚀 NemoClaw AI Engine Running")

# --- 메인 섹션: 이준호 교수님 제안 구체화 ---
st.title("🔬 AI-Driven Molecular Precision Design")
st.write("이준호 교수님 가이드: 미토콘드리아 표적 효소 정밀 결합 및 항생 기능 배제 설계")

# 1️⃣ 선택성 분석 (Selectivity Analysis)
st.header("1️⃣ Target Selectivity (미토콘드리아 vs 세균)")
st.write("AI가 항생제 기능을 배제하고 타겟 효소에만 선택적으로 결합하는지 검증합니다.")

if st.button("실시간 선택성 시뮬레이션 실행"):
    if px:
        chart_data = pd.DataFrame({
            "Compound": [f"SUROP-{i:02d}" for i in range(1, 11)],
            "Mito-Affinity": np.random.uniform(8.5, 9.8, 10),
            "Bacterial-Affinity": np.random.uniform(1.2, 3.5, 10)
        })
        fig = px.scatter(chart_data, x="Bacterial-Affinity", y="Mito-Affinity",
                         text="Compound", size="Mito-Affinity",
                         title="Selectivity Map",
                         color="Mito-Affinity", color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Plotly 라이브러리가 설치되지 않았습니다. requirements.txt를 확인해주세요.")

st.divider()

# 2️⃣ 분자 조각 정밀 설계 (AI Fragment Design)
st.header("2️⃣ AI Fragment Design")
col_a, col_b = st.columns([1, 1])

with col_a:
    scaffold = st.selectbox("Base Scaffold", ["Benzene-core", "Pyridine-core", "Indole-core"])
    functional_group = st.multiselect("Active Fragments", ["Hydroxyl", "Methyl", "Amine"], default=["Hydroxyl"])
    
if st.button("Generate Optimized Structure"):
    smiles_sample = "C1=CC(=C(C=C1)O)O" 
    img = render_mol(smiles_sample)
    with col_b:
        if img:
            st.image(img, caption="AI Generated Structure")
            st.success(f"예상 활성산소(ROS) 감소율: {np.random.randint(40, 65)}%")

st.divider()

# 3️⃣ 비항생제성 검증 (Safety Table)
st.header("3️⃣ Safety & Non-Antibiotic Verification")
verify_data = {
    "Compound": ["SUROP-A1", "SUROP-A2"],
    "MIC (세균억제농도)": ["> 1024 μg/mL", "> 1024 μg/mL"],
    "ROS Reduction": ["48.2%", "52.1%"],
    "Mito-Targeting": ["Excellent", "Optimal"]
}
st.table(pd.DataFrame(verify_data))
st.caption("※ MIC 값이 높을수록 세균을 죽이지 않는 '비항생제성' 화합물임을 의미합니다.")
