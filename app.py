import streamlit as st
import pandas as pd
import time
import numpy as np

# 1. 페이지 기본 설정 및 테마 (다크 모드 지향)
st.set_page_config(
    page_title="SUROP | AI Drug Discovery Platform",
    page_icon="🧬",
    layout="wide"
)

# 커스텀 CSS: 폰트 및 색상 강조
st.markdown("""
    <style>
    .main { background-color: #0c1a2e; }
    .stMetric { background-color: #162a47; padding: 15px; border-radius: 10px; border-left: 5px solid #ffe135; }
    h1, h2, h3 { color: #ffe135 !important; }
    .stProgress > div > div > div > div { background-color: #ffe135; }
    </style>
    """, unsafe_allow_safe_html=True)

# --- 사이드바: 플랫폼 로고 및 상태 ---
with st.sidebar:
    st.title("🧬 SUROP")
    st.info("**S**uperior **U**niversal **R**eceptor **O**ptimization **P**latform")
    st.divider()
    st.success("System Status: **Active**")
    st.write("v1.2.0-Alpha (NemoClaw Engine)")

# --- 메인 섹션 1: 헤더 ---
st.title("Aging Target Protein: In-Silico Discovery")
st.subheader("AI기반 차세대 노화 억제 및 비항생제성 화합물 발굴 플랫폼")

# --- 메인 섹션 2: 3대 핵심 기술 시각화 (3개 컬럼) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Binding Affinity (Avg)", value="98.2%", delta="Top 1%")
    st.write("**DiffDock Engine**")
    st.caption("확산 모델 기반 고정밀 3D 분자 도킹 시뮬레이션")

with col2:
    st.metric(label="Safety Pass Rate", value="Pass", delta="Toxic Free")
    st.write("**Toxicity Predictor**")
    st.caption("간/심장 독성 및 ADMET 예측 엔진 탑재")

with col3:
    st.metric(label="Anti-Bacterial", value="Negative", delta="Gut Safety")
    st.write("**Anti-Bacterial Check**")
    st.caption("장내 미생물 보호를 위한 비항생제성 검증")

st.divider()

# --- 메인 섹션 3: 실시간 시뮬레이션 데모 ---
st.header("🔬 Real-time Discovery Simulation")
if st.button('플랫폼 분석 시작 (Start AI Screening)'):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(101):
        time.sleep(0.02)
        progress_bar.progress(i)
        status_text.text(f"Scanning Library... {i}% 완료")
    
    st.balloons()
    
    # 가상 분석 데이터 생성
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("### 🧬 Target: Aging Protein (C. elegans Model)")
        # 차트 예시 (스크리닝 빈도)
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Affinity', 'Safety', 'Solubility'])
        st.line_chart(chart_data)
    
    with c2:
        st.write("### ✅ Screening Results")
        st.success("Targeting: IGF-1 Receptor")
        st.warning("Candidate Found: 1,240,000+")
        st.info("Filtered Top 5 Candidates")

st.divider()

# --- 메인 섹션 4: 최종 후보 물질 (Top 5) ---
st.header("🏆 Final Candidate Compounds (Top 5)")
st.write("서울대 이준호 교수님 연구팀에 즉시 제공 가능한 고효율 화합물 리스트")

# 5개의 화합물 카드 배치
comp_cols = st.columns(5)
compound_names = ["SUROP-A01 (Nano-Banana)", "SUROP-A02", "SUROP-A03", "SUROP-A04", "SUROP-A05"]

for i, col in enumerate(comp_cols):
    with col:
        st.image("https://via.placeholder.com/150/162a47/ffe135?text=Molecule+Structure", use_container_width=True)
        st.write(f"**{compound_names[i]}**")
        st.markdown("**Stock:** `In-Stock` ✅")
        st.button(f"Data Sheet {i+1}", key=f"btn_{i}")

# --- 하단: 연락처 및 제안 ---
st.divider()
st.info("📫 **Collaboration Inquiry**: 이준호 교수님 연구팀과의 공동 연구 및 생체 검증(In-vivo) 제안을 위해 구축된 전용 페이지입니다.")
st.write("Contact: misatech@surop.com | [형님 성함/직함]")
