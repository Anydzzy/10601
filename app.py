import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="💘 Любовный Коуч",
    page_icon="💕",
    layout="centered"
)

# 스타일
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #ffe6f2, #fff5f9);
}

.title {
    text-align: center;
    font-size: 42px;
    color: #ff4d88;
    font-weight: bold;
}

.box {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    border: 3px dashed #ff99bb;
    color: #444;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">💘 Любовный Коуч 💘</div>', unsafe_allow_html=True)

st.write("")

# 기분 선택
mood = st.selectbox(
    "🌸 Как ты себя чувствуешь?",
    [
        "😊 Счастлив(а)",
        "🥺 Грустно",
        "😡 Злюсь",
        "🤔 Запутался(ась)",
        "😍 Влюблён(а)"
    ]
)

# 고민 입력
user_text = st.text_area(
    "💌 Напиши свою любовную проблему",
    placeholder="Например: Он долго не отвечает..."
)

# 러시아어 답변 데이터
happy = [
    "✨ Сегодня твоя улыбка особенно прекрасна!",
    "💖 Попробуй написать человеку, который тебе нравится.",
    "🌸 Твоя энергия притягивает любовь."
]

sad = [
    "🥺 Не переживай слишком сильно.",
    "💌 Медленный ответ не всегда значит потерю интереса.",
    "🌷 Сегодня позаботься о себе."
]

angry = [
    "🌸 Спокойный разговор решает многое.",
    "💬 Лучше мягко рассказать о своих чувствах.",
    "💕 Искренность важнее злости."
]

confused = [
    "👀 Смотри не на слова, а на постоянство.",
    "😌 Когда человек любит — это видно.",
    "🌙 Не бойся делать паузу."
]

love = [
    "💖 Любовь делает тебя ярче!",
    "✨ Сегодня отличный день для признания.",
    "🌸 Добрые слова укрепляют отношения."
]

# 버튼
if st.button("💕 Получить совет"):

    if user_text.strip() == "":
        st.warning("💌 Пожалуйста, напиши проблему!")

    else:

        if mood == "😊 Счастлив(а)":
            result = random.choice(happy)

        elif mood == "🥺 Грустно":
            result = random.choice(sad)

        elif mood == "😡 Злюсь":
            result = random.choice(angry)

        elif mood == "🤔 Запутался(ась)":
            result = random.choice(confused)

        else:
            result = random.choice(love)

        st.balloons()

        st.markdown(
            f"""
            <div class="box">
            💘 Любовный совет 💘
            <br><br>
            {result}
            <br><br>
            📝 Твоя проблема:
            <br>
            {user_text}
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("")
st.caption("made with 💖 and Russian vibes 🇷🇺")
