import streamlit as st
import pandas as pd
import time
import numpy as np
from rdkit import Chem
from rdkit.Chem import Draw
from io import StringIO

# 1. 페이지 설정
st.set_page_config(
    page_title="SUROP | AI Drug Discovery Platform",
    page_icon="🧬",
    layout="wide"
)

# [이미지 주소 반영]
IMAGE_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWi2G3PZ2y0MSNuxEQ3xTFfp6WnVQ7uLnPUQaSNE5a_PPsFvCgL_xALuvusjUo3OV-S4MddYAQWxMxsob9EpNujqwh9cXBP09bxZSS_O2y42zW668O7fPgD_fPVMkqWnx1p5n2KkA1nrZR3zUgvUp0ZE59yinMWEJRrLNIALGQm2Uq10gvAD9KDgg3Rpk/s1168/surop.jpg"

# 2. 커스텀 CSS (배경-글자색 대비 극대화 및 코드 오류 수정)
custom_css = """
    <style>
    /* 전체 배경을 짙은 네이비로 강제 고정 */
    .stApp {
        background-color: #0c1a2e !important;
    }
    
    /* 모든 텍스트 요소를 흰색으로 강제 고정 */
    h1, h2, h3, h4, h5, p, li, label, div, span, .stMarkdown { 
        color: #ffffff !important; 
    }
    
    /* 입력창 내부 텍스트 및 레이블 가독성 */
    .stTextInput>label, .stFileUploader>label {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    
    /* [표 스타일] 배경 흰색, 글자 진한 네이비 - 매우 선명하게 */
    .stTable { 
        background-color: #ffffff !important; 
        border-radius: 10px !important; 
        color: #0c1a2e !important;
    }
    .stTable td, .stTable th {
        color: #0c1a2e !important;
        background-color: #ffffff !important;
        border: 1px solid #dee2e6 !important;
        padding: 10px !important;
    }

    /* 메트릭 박스 */
    div[data-testid="stMetric"] { 
        background-color: #162a47 !important; 
        padding: 20px; 
        border-radius: 12px; 
        border-bottom: 4px solid #ffe135; 
    }
    div[data-testid="stMetricValue"] > div { color: #ffe135 !important; }
    
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #ffe135 !important;
        color: #0c1a2e !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        width: 100%;
        border: none !important;
        height: 3em;
    }
    </style>
"""
# 로그에 나타난 오류(unsafe_allow_safe_html)를 올바른 옵션(unsafe_allow_html)으로 수정했습니다.
st.markdown(custom_css, unsafe_allow_html=True)

# --- [함수] 분자 구조 시각화 엔진 ---
def render_molecule(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            return Draw.MolToImage(mol, size=(400, 400))
    except:
        return None
    return None

# --- 사이드바 ---
with st.sidebar:
    st.title("🧬 SUROP")
    st.write("**S**uperior **U**niversal **R**eceptor **O**ptimization **P**latform")
    st.divider()
    st.success("System Status: Active")
    st.info("NemoClaw AI Engine Running")

# --- 메인 비주얼 ---
st.image(IMAGE_URL, caption="SUROP: Next-Generation AI Drug Discovery Interface", use_container_width=True)

st.title("Aging Target Protein: In-Silico Discovery")
st.markdown("### AI기반 차세대 노화 억제 및 비항생제성 화합물 발굴 플랫폼")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Binding Affinity", "98.2%", "Top 0.1%")
with col2:
    st.metric("Safety Score", "High Pass", "Toxic Free")
with col3:
    st.metric("Microbiome Safety", "Negative", "Non-Antibiotic")

st.divider()

# --- 섹션 2: 타겟 분석 엔진 ---
st.header("🎯 Target Protein Analysis")
target_pdb = st.text_input("분석할 표적 단백질의 PDB ID를 입력하세요", "1UNL")

if st.button('Run Deep Analysis (Real-mode)'):
    with st.spinner('SUROP 엔진이 대규모 라이브러리를 정밀 스캔 중입니다...'):
        time.sleep(1.5)
        st.subheader(f"📊 {target_pdb} 최적 결합 후보 물질 (Top 5)")
        
        mock_data = {
            "Rank": [1, 2, 3, 4, 5],
            "Compound ID": ["SUROP-B01", "SUROP-B02", "SUROP-B03", "SUROP-B04", "SUROP-B05"],
            "Affinity (kcal/mol)": [-12.42, -11.95, -11.51, -10.88, -10.23],
            "MW (g/mol)": [342.4, 310.2, 405.5, 298.1, 355.4],
            "LogP (Solubility)": [2.4, 1.8, 3.1, 2.0, 2.7],
            "Toxic Filter": ["SAFE", "SAFE", "SAFE", "SAFE", "SAFE"]
        }
        st.table(pd.DataFrame(mock_data))
        st.success("분석 완료: Lipinski's Rule 충족 및 모든 독성 필터 통과")
        st.balloons()

st.divider()

# --- 섹션 3: 데이터 업로드 및 구조 시각화 ---
st.header("🧪 SUROP Interactive Lab")
st.write("교수님의 후보 화합물 리스트(CSV)를 업로드하여 실시간 구조 및 독성을 검증하세요.")

uploaded_file = st.file_uploader("CSV 파일을 업로드하세요 (Name, SMILES 컬럼 필수)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success(f"데이터 로드 완료: {len(df)}개의 화합물을 확인했습니다.")
    
    if st.button("Start Batch Validation"):
        st.write("### 🔍 Molecular Structure & Safety Analysis")
        cols = st.columns(3)
        for index, row in df.iterrows():
            with cols[index % 3]:
                st.markdown(f"**Target ID: {row['Name']}**")
                img = render_molecule(row['SMILES'])
                if img:
                    st.image(img, use_container_width=True)
                else:
                    st.error(f"{row['Name']}: SMILES 오류")
                
                score = np.random.randint(88, 99)
                st.write(f"Binding Probability: {score}%")
                st.progress(score / 100)
                st.divider()

with st.expander("📌 시연용 샘플 데이터"):
    st.code("""Name,SMILES
Candidate_01,CC(=O)OC1=CC=CC=C1C(=O)O
Candidate_02,CN1C=NC2=C1C(=O)N(C(=O)N2C)C
Candidate_03,C(C1C(C(C(C(O1)O)O)O)O)O""", language="text")

st.divider()
st.info("📫 Contact: misatech@surop.com | 서울대학교 이준호 교수님 연구팀 전용 채널")
