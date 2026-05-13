import streamlit as st
import google.generativeai as genai

# 1. Налаштування Gemini (Беремо ключ із Secrets)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
  model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception:
    st.error("Будь ласка, додайте GEMINI_API_KEY у Secrets вашого додатка!")

# Налаштування сторінки
st.set_page_config(page_title="Еко-Портал", layout="wide")

# Налаштування шрифтів
st.sidebar.title("⚙️ Налаштування")
font_choice = st.sidebar.selectbox("Оберіть шрифт інтерфейсу:", ["Default", "Serif", "Monospace", "Tahoma"])
fonts = {"Default": "sans-serif", "Serif": "serif", "Monospace": "monospace", "Tahoma": "Tahoma"}
f = fonts[font_choice]

# CSS стиль (Telegram-стиль)
st.markdown(f"""
    <style>
    * {{ font-family: {f} !important; }}
    .stApp {{ background-color: #f0fdf4; }}
    [data-testid="stSidebar"] {{ background-color: #dcfce7; min-width: 320px; }}
    .chat-bubble {{
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;
        background: white;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        display: flex;
        gap: 20px;
    }}
    .avatar {{ width: 60px; height: 60px; border-radius: 50%; flex-shrink: 0; }}
    .main-article {{ 
        font-size: 18px !important; 
        line-height: 1.8 !important; 
        color: #1f2937; 
        text-align: justify;
        white-space: pre-wrap;
    }}
    h1, h2, h3 {{ color: #064e3b !important; font-weight: bold !important; }}
    </style>
    """, unsafe_allow_html=True)

# Функція для генерації контенту через Gemini
def generate_eco_content(topic_name):
    prompt = f"""
    Ти — провідний експерт-еколог. Напиши надзвичайно детальну науково-популярну статтю на тему: {topic_name}.
    ВИМОГИ:
    1. Текст має бути дуже великим (близько 1500-2000 слів).
    2. Використовуй заголовки (##), списки та наукові факти.
    3. Пиши українською мовою.
    4. Зроби статтю цікавою, з прикладами та прогнозами на майбутнє.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Помилка генерації: {str(e)}"

# Навігація
all_topics = ["🏠 Головна", "♻️ Як сортувати сміття?", "🌲 Захист лісів", "🦋 Біорізноманіття", "💬 Інше питання"]
st.sidebar.title("🌸 Еко-Меню")
topic = st.sidebar.radio("Оберіть тему:", all_topics)

# Збереження повідомлень (кеш)
if "messages" not in st.session_state:
    st.session_state.messages = {}

# Логіка відображення
st.title(f"🌱 Еко-Портал: {topic}")

if topic not in st.session_state.messages:
    with st.spinner("ШІ готує розгорнутий матеріал... зачекайте хвилинку"):
        st.session_state.messages[topic] = generate_eco_content(topic)

# Вивід результату
u_icon = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
b_icon = "https://cdn-icons-png.flaticon.com/512/11013/11013833.png"

st.markdown(f"""
    <div class="chat-bubble">
        <img src="{b_icon}" class="avatar">
        <div class="main-article">{st.session_state.messages[topic]}</div>
    </div>
""", unsafe_allow_html=True)

# Чат для довільних питань
if topic == "💬 Інше питання":
    if prompt := st.chat_input("Запитайте про екологію..."):
        with st.spinner("Геміні думає..."):
            answer = generate_eco_content(prompt)
            st.markdown(f"""
                <div class="chat-bubble">
                    <img src="{u_icon}" class="avatar">
                    <div class="main-article"><b>Ваше питання:</b> {prompt}</div>
                </div>
                <div class="chat-bubble">
                    <img src="{b_icon}" class="avatar">
                    <div class="main-article">{answer}</div>
                </div>
            """, unsafe_allow_html=True)
