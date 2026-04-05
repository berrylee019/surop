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

# 2. 커스텀 CSS (옵션 명칭 수정 완료: unsafe_allow_html)
custom_css = """
    <style>
    .main { background-color: #0c1a2e; }
    div[data-testid="stMetric"] { background-color: #162a47; padding: 15px; border-radius: 10px; border-left: 5px solid #ffe135; }
    h1, h2, h3 { color: #ffe135 !important; }
    div.stProgress > div > div > div > div { background-color: #ffe135; }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- 사이드바: SUROP 정체성 강조 ---
with st.sidebar:
    st.title("🧬 SUROP")
    st.info("**S**uperior **U**niversal **R**eceptor **O**ptimization **P**latform")
    st.divider()
    st.success("System Status: **Active**")
    st.write("v1.2.0-Alpha (NemoClaw Engine)")

# --- 메인 섹션: 타이틀 ---
st.title("Aging Target Protein: In-Silico Discovery")
st.subheader("AI기반 차세대 노화 억제 및 비항생제성 화합물 발굴 플랫폼")

# --- 메인 섹션: 3대 핵심 지표 ---
col1, col2, col3 = st.columns(3)
col1.metric("Binding Affinity (Avg)", "98.2%", "Top 1%")
col2.metric("Safety Pass Rate", "Pass", "Toxic Free")
col3.metric("Anti-Bacterial", "Negative", "Gut Safety")

st.divider()

# --- 실시간 스크리닝 시뮬레이션 데모 ---
st.header("🔬 Real-time Discovery Simulation")
if st.button('플랫폼 분석 시작 (Start AI Screening)'):
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01) # 시뮬레이션 속도
        progress_bar.progress(i)
    st.balloons()
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### 🧬 Target: Aging Protein (C. elegans Model)")
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Affinity', 'Safety'])
        st.line_chart(chart_data)
    with c2:
        st.write("### ✅ Screening Results")
        st.success("Targeting: IGF-1 Receptor")
        st.info("Filtered Top 5 Candidates")

st.divider()

# --- 하단: 최종 후보 물질 리스트 ---
st.header("🏆 Final Candidate Compounds (Top 5)")
st.write("서울대 이준호 교수님 연구팀 제공용 리스트")
comp_cols = st.columns(5)
for i, col in enumerate(comp_cols):
    with col:
        st.code(f"SUROP-A0{i+1}", language="text")
        st.write("Stock: `In-Stock` ✅")
        st.button(f"Data Sheet {i+1}", key=f"btn_{i}")

st.info("📫 **Collaboration Inquiry**: 이준호 교수님 연구팀과의 공동 연구 및 생체 검증(In-vivo) 제안을 위한 전용 페이지입니다.")
