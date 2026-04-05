import streamlit as st
import pandas as pd
import time
import numpy as np
from rdkit import Chem
from rdkit.Chem import Draw

# 1. 페이지 설정
st.set_page_config(
    page_title="SUROP | AI Drug Discovery Platform",
    page_icon="🧬",
    layout="wide"
)

# [이미지 주소]
IMAGE_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWi2G3PZ2y0MSNuxEQ3xTFfp6WnVQ7uLnPUQaSNE5a_PPsFvCgL_xALuvusjUo3OV-S4MddYAQWxMxsob9EpNujqwh9cXBP09bxZSS_O2y42zW668O7fPgD_fPVMkqWnx1p5n2KkA1nrZR3zUgvUp0ZE59yinMWEJRrLNIALGQm2Uq10gvAD9KDgg3Rpk/s1168/surop.jpg"

# 2. 커스텀 CSS (사이드바 가독성 해결 핵심)
custom_css = """
    <style>
    /* 전체 앱 배경 */
    .stApp {
        background-color: #0c1a2e !important;
    }
    
    /* 메인 화면 텍스트 흰색 */
    h1, h2, h3, h4, h5, p, li, span, label, .stMarkdown { 
        color: #ffffff !important; 
    }

    /* [집중 수정] 사이드바 가독성: 배경은 밝게, 모든 글자는 아주 진하게 */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
    }
    section[data-testid="stSidebar"] * {
        color: #0c1a2e !important; /* 사이드바 내 모든 요소 글자색 강제 */
    }
    section[data-testid="stSidebar"] .stMarkdown p {
        font-weight: 600 !important;
    }

    /* 표(Table) 가독성: 흰색 배경에 검은 글씨 */
    div[data-testid="stTable"] {
        background-color: #ffffff !important;
        border-radius: 10px !important;
    }
    div[data-testid="stTable"] table {
        color: #000000 !important;
    }
    div[data-testid="stTable"] th {
        background-color: #e9ecef !important;
        color: #000000 !important;
        font-weight: bold !important;
    }
    div[data-testid="stTable"] td {
        color: #000000 !important;
        border: 1px solid #dee2e6 !important;
    }

    /* 버튼 및 업로드 섹션 */
    .stButton>button {
        background-color: #ffe135 !important;
        color: #000000 !important;
        font-weight: bold !important;
    }
    button[data-testid="stBaseButton-secondary"] {
        color: #000000 !important;
        background-color: #ffe135 !important;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- [함수] 분자 구조 시각화 ---
def render_molecule(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            return Draw.MolToImage(mol, size=(400, 400))
    except:
        return None
    return None

# --- 사이드바 (가독성 수정 대상) ---
with st.sidebar:
    st.title("🧬 SUROP")
    st.write("**S**uperior **U**niversal **R**eceptor **O**ptimization **P**latform")
    st.divider()
    st.write("### System Status")
    st.info("✅ Status: Active")
    st.write("### Engine Info")
    st.info("🚀 NemoClaw AI Running")

# --- 메인 섹션 ---
st.image(IMAGE_URL, caption="SUROP Platform Interface", use_container_width=True)

st.title("Aging Target Protein Analysis")
st.markdown("### AI기반 차세대 노화 억제 화합물 발굴 플랫폼")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Binding Affinity", "98.2%")
with col2:
    st.metric("Safety Score", "High Pass")
with col3:
    st.metric("Microbiome", "Safe")

st.divider()

# 분석 엔진 섹션
st.header("🎯 Target Analysis")
target_pdb = st.text_input("PDB ID 입력", "1UNL")

if st.button('Run Analysis'):
    with st.spinner('분석 중...'):
        time.sleep(1)
        mock_data = {
            "Rank": [1, 2, 3],
            "Compound ID": ["SUROP-01", "SUROP-02", "SUROP-03"],
            "Affinity": [-12.4, -11.9, -11.5],
            "Result": ["SAFE", "SAFE", "SAFE"]
        }
        st.table(pd.DataFrame(mock_data))

st.divider()

# 데이터 업로드 섹션
st.header("🧪 Interactive Lab")
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if st.button("Start Validation"):
        cols = st.columns(3)
        for index, row in df.iterrows():
            with cols[index % 3]:
                st.write(f"ID: {row['Name']}")
                img = render_molecule(row['SMILES'])
                if img: st.image(img)
                st.progress(np.random.randint(80, 100) / 100)
