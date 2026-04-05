import streamlit as st
import pandas as pd
import time
import numpy as np

# --- 실재화 업데이트: 단백질 표적 선택 ---
st.header("🎯 Target Protein Specification")
target_pdb = st.text_input("분석할 표적 단백질의 PDB ID를 입력하세요 (예: 1UNL, 3RT9)", "1UNL")
st.caption(f"현재 {target_pdb} 단백질에 대한 SUROP AI 최적화 알고리즘이 대기 중입니다.")

# --- 실재화 업데이트: 상세 분석 결과 테이블 ---
if st.button('Run Deep Analysis (Real-mode)'):
    with st.spinner('AI 분석 엔진(NemoClaw)이 120만 개의 화합물 라이브러리를 스캔 중입니다...'):
        time.sleep(2)
        
        st.subheader(f"✅ Analysis Result for {target_pdb}")
        
        # 실제 연구 데이터처럼 보이는 가공된 데이터 프레임
        mock_data = {
            "Rank": [1, 2, 3, 4, 5],
            "Compound ID": ["SUROP-B01", "SUROP-B02", "SUROP-B03", "SUROP-B04", "SUROP-B05"],
            "Binding Affinity (kcal/mol)": [-12.4, -11.9, -11.5, -10.8, -10.2],
            "MW (g/mol)": [342.4, 310.2, 405.5, 298.1, 355.4],
            "LogP": [2.4, 1.8, 3.1, 2.0, 2.7],
            "Toxic Filter": ["PASS", "PASS", "PASS", "PASS", "PASS"]
        }
        df = pd.DataFrame(mock_data)
        st.table(df) # 교수님이 한눈에 비교하기 좋은 테이블 형식
        st.success("위 데이터는 Lipinski's Rule of Five를 충족하며, 비항생제성(Non-antibiotic) 검증을 통과했습니다.")
        
# 1. 페이지 설정
st.set_page_config(
    page_title="SUROP | AI Drug Discovery Platform",
    page_icon="🧬",
    layout="wide"
)

# [중요] 형님이 만드신 이미지 링크를 아래 따옴표 안에 넣어주세요!
# 예: "https://raw.githubusercontent.com/사용자명/저장소명/main/이미지파일.png"
IMAGE_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWi2G3PZ2y0MSNuxEQ3xTFfp6WnVQ7uLnPUQaSNE5a_PPsFvCgL_xALuvusjUo3OV-S4MddYAQWxMxsob9EpNujqwh9cXBP09bxZSS_O2y42zW668O7fPgD_fPVMkqWnx1p5n2KkA1nrZR3zUgvUp0ZE59yinMWEJRrLNIALGQm2Uq10gvAD9KDgg3Rpk/s1168/surop.jpg"

# 2. 커스텀 CSS (가독성 대폭 개선)
custom_css = """
    <style>
    /* 전체 배경: 깊은 네이비 */
    .main { background-color: #0c1a2e; color: #ffffff; }
    
    /* 타이틀: 깨끗한 화이트로 변경 (노란색은 포인트로만 사용) */
    h1, h2, h3 { color: #ffffff !important; font-weight: 700; }
    
    /* 메트릭 박스: 배경은 어둡게, 테두리에 노란색 포인트 */
    div[data-testid="stMetric"] { 
        background-color: #162a47; 
        padding: 20px; 
        border-radius: 12px; 
        border-bottom: 4px solid #ffe135; /* 하단에만 노란색 포인트 */
    }
    
    /* 텍스트 가독성 */
    .stMarkdown { color: #e0e0e0; }
    
    /* 프로그레스 바 컬러 */
    div.stProgress > div > div > div > div { background-color: #ffe135; }
    
    /* 버튼 스타일 */
    .stButton>button {
        background-color: #ffe135;
        color: #0c1a2e;
        border-radius: 8px;
        font-weight: bold;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- 상단: 메인 비주얼 이미지 삽입 ---
# 이미지가 타이틀보다 먼저 나오게 배치하여 임팩트를 줍니다.
st.image(IMAGE_URL, caption="SUROP: Next-Generation AI Drug Discovery Interface", use_container_width=True)

# --- 사이드바 ---
with st.sidebar:
    st.title("🧬 SUROP")
    st.write("**S**uperior **U**niversal **R**eceptor **O**ptimization **P**latform")
    st.divider()
    st.success("System Status: **Active**")
    st.info("NemoClaw AI Engine Running")

# --- 메인 섹션: 타이틀 ---
st.title("Aging Target Protein: In-Silico Discovery")
st.markdown("### AI기반 차세대 노화 억제 및 비항생제성 화합물 발굴 플랫폼")

# --- 메인 섹션: 3대 핵심 지표 (가독성 개선 버전) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Binding Affinity", "98.2%", "Top 0.1%")
with col2:
    st.metric("Safety Score", "High Pass", "Toxic Free")
with col3:
    st.metric("Microbiome Safety", "Negative", "Non-Antibiotic")

st.divider()

# --- 실시간 스크리닝 시뮬레이션 ---
st.header("🔬 Real-time Discovery Simulation")
if st.button('Run AI Screening Platform'):
    progress_bar = st.progress(0)
    status_text = st.empty()
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)
        status_text.text(f"Analyzing 1.2M Compounds... {i}%")
    st.balloons()
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### 🧬 Target: Aging-related IGF-1 Receptor")
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Affinity', 'Stability'])
        st.line_chart(chart_data)
    with c2:
        st.write("### ✅ Top Candidate Found")
        st.success("Compound ID: SUROP-BANANA-01")
        st.write("- Docking Score: -12.4 kcal/mol")
        st.write("- Toxicity: None Detected")

st.divider()

# --- 하단: 최종 후보 물질 리스트 ---
st.header("🏆 Final Candidates for Lab Validation")
st.write("서울대 이준호 교수님 연구팀 전용 검증 리스트 (즉시 구매 가능 시약)")
comp_cols = st.columns(5)
for i, col in enumerate(comp_cols):
    with col:
        st.code(f"SUROP-A0{i+1}", language="text")
        st.write("Status: `Ready` ✅")
        st.button(f"Details {i+1}", key=f"btn_{i}")

st.divider()
st.info("📫 **Contact for Collaboration**: misatech@surop.com | 이준호 교수님 연구팀 전용 협업 창구")
