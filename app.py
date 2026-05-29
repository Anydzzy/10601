import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="💘 두근두근 연애코치",
    page_icon="💕",
    layout="centered"
)

# CSS 꾸미기
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #ffe6f2, #fff5f9);
}

.main-title {
    text-align: center;
    font-size: 45px;
    color: #ff4d88;
    font-weight: bold;
}

.sub-text {
    text-align: center;
    color: #ff80aa;
    font-size: 18px;
}

.advice-box {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    border: 3px dashed #ff99bb;
    color: #444;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="main-title">💘 두근두근 연애코치 💘</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">오늘의 연애 고민을 말해줘 ✨</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# 기분 선택
mood = st.selectbox(
    "🌈 지금 기분은 어때?",
    ["😊 설레는 중", "🥺 슬픈 중", "😡 삐진 상태", "🤔 헷갈리는 중", "😍 사랑 가득"]
)

# 고민 입력
user_text = st.text_area(
    "💌 고민을 적어줘",
    placeholder="예: 썸남이 답장이 느려요..."
)

# 코칭 데이터
happy_advice = [
    "오늘은 웃는 얼굴 하나만으로도 매력이 폭발해 ✨",
    "좋아하는 사람에게 가볍게 안부 연락해봐 💌",
    "행복한 에너지는 사랑을 더 끌어당겨 💕"
]

sad_advice = [
    "너무 혼자 끙끙 앓지 마 🥺",
    "답장이 늦다고 마음까지 멀어진 건 아닐 수도 있어 💭",
    "오늘은 스스로를 먼저 아껴주자 🌷"
]

angry_advice = [
    "잠깐 진정하고 말하면 더 예쁘게 전달돼 🌸",
    "서운한 건 참지 말고 부드럽게 표현해봐 💬",
    "감정보다 마음을 설명해주는 게 중요해 💕"
]

confused_advice = [
    "헷갈릴 땐 상대 행동보다 '꾸준함'을 봐 👀",
    "좋아하면 티가 난다… 진짜로 😌",
    "너를 불안하게만 하는 사랑은 쉬어가도 돼 🌙"
]

love_advice = [
    "사랑할 때의 너는 정말 반짝여 ✨",
    "오늘은 애정 표현을 조금 더 해봐 💖",
    "예쁜 말 한마디가 관계를 더 깊게 만들어 🌸"
]

# 버튼
if st.button("💕 연애 코칭 받기"):

    if user_text.strip() == "":
        st.warning("고민을 먼저 적어줘 💌")

    else:
        if mood == "😊 설레는 중":
            result = random.choice(happy_advice)

        elif mood == "🥺 슬픈 중":
            result = random.choice(sad_advice)

        elif mood == "😡 삐진 상태":
            result = random.choice(angry_advice)

        elif mood == "🤔 헷갈리는 중":
            result = random.choice(confused_advice)

        else:
            result = random.choice(love_advice)

        st.balloons()

        st.markdown(
            f"""
            <div class="advice-box">
            💘 연애 코칭 결과 💘 <br><br>
            {result}
            <br><br>
            📝 네 고민: {user_text}
            </div>
            """,
            unsafe_allow_html=True
        )

# 하단 문구
st.write("")
st.caption("made with 💖 using Streamlit")
