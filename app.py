
import streamlit as st

st.set_page_config(
    page_title="점수 확인 및 성취도 개인 가이드",
    page_icon="📚",
    layout="centered"
)

# 과목별 점수
scores = {
    "과학": 45,
    "영어": 98,
    "수학": 92,
    "국어": 85,
    "사회": 72
}

st.title("📚 점수 확인 및 성취도 개인 가이드")
st.write("이름과 과목을 선택하고 성적을 확인하세요!")

# 입력 화면
with st.form("score_form"):
    name = st.text_input("이름을 입력하세요")

    subject = st.selectbox(
        "과목을 선택하세요",
        ["과학", "영어", "수학", "국어", "사회"]
    )

    submitted = st.form_submit_button("결과 확인하기")

# 결과 출력
if submitted:
    if not name.strip():
        st.warning("이름을 입력해 주세요!")

    else:
        score = scores[subject]

        # 성취도 계산
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "D"

        st.divider()
        st.subheader("📊 성적 확인 결과")

        st.write("👤 이름:", name)
        st.write("📖 과목:", subject)
        st.metric("점수", f"{score}점")
        st.metric("성취도", grade)

        # 위험도 확인
        if score <= 50:
            st.error("위험도 점수: 2점")
            st.warning(
                "학습 주의! 해당 과목을 복습하고 "
                "학습 관리에 신경 써 주세요."
            )
        else:
            st.success("위험도 점수: 0점")
            st.info("좋은 학습 상태를 유지하세요!")

        st.progress(score / 100)

