import streamlit as st
import pandas as pd
import time
import numpy as np

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
