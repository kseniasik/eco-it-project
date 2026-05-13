import streamlit as st
from openai import OpenAI

# 1. Підключення ШІ (Твій ключ)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    st.error("Будь ласка, додайте OPENAI_API_KEY у Secrets!")
# Налаштування сторінки
st.set_page_config(page_title="Еко-Портал", layout="wide")

# Налаштування шрифтів через Sidebar
st.sidebar.title("⚙️ Налаштування")
font_choice = st.sidebar.selectbox("Оберіть шрифт інтерфейсу:", ["Default", "Serif", "Monospace", "Tahoma"])
fonts = {"Default": "sans-serif", "Serif": "serif", "Monospace": "monospace", "Tahoma": "Tahoma"}
f = fonts[font_choice]

# CSS для Telegram-стилю
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

# БАЗА ДАНИХ (Статті залишаються для бази знань бота)
eco_database = {
    "🏠 Головна": {
        "text": """# Ласкаво просимо до Еко-Порталу! 🌱\nТут ви знайдете все про екологію та сталий розвиток.""",
        "img": "https://images.unsplash.com/photo-1518173946687-a4c8a9ba332f?q=80&w=1200"
    },
    "♻️ Як сортувати сміття?": {
        "text": """# Глобальна стратегія сортування ♻️\nПластик (1-5), макулатура та скло — ваші кроки до чистої планети.""",
        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=1200"
    },
    "🌲 Захист лісів": {
        "text": """# Ліси як фундамент стабільності 🌲\nДерева — легені планети, що поглинають CO2.""",
        "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200"
    },
    "🦋 Біорізноманіття": {
        "text": """# Шосте масове вимирання 🦋\nКожен вид важливий для балансу екосистеми.""",
        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=1200"
    }
}

all_topics = ["🏠 Головна", "♻️ Як сортувати сміття?", "🌲 Захист лісів", "🦋 Біорізноманіття", "💬 Інше питання"]

# Sidebar Навігація
st.sidebar.title("🌸 Еко-Меню")
topic = st.sidebar.radio("Оберіть тему:", all_topics)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Очищення та зміна теми
if "current_topic" not in st.session_state or st.session_state.current_topic != topic:
    st.session_state.current_topic = topic
    if topic != "💬 Інше питання":
        res = eco_database[topic]
        st.session_state.messages = [{"role": "assistant", "content": res["text"], "image": res["img"]}]
    else:
        st.session_state.messages = [{"role": "assistant", "content": "# 💬 Питання та відповіді\nЗапитайте мене про будь-що, що стосується екології!"}]

# Відображення чату
u_icon = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
b_icon = "https://cdn-icons-png.flaticon.com/512/11013/11013833.png"

for msg in st.session_state.messages:
    icon = u_icon if msg["role"] == "user" else b_icon
    st.markdown(f"""
        <div class="chat-bubble">
            <img src="{icon}" class="avatar">
            <div class="main-article">{msg["content"]}</div>
        </div>
    """, unsafe_allow_html=True)
    if "image" in msg:
        st.image(msg["image"], use_container_width=True)

# ЛОГІКА РЕАЛЬНОГО ШІ
if prompt := st.chat_input("Напишіть своє питання про екологію..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("ШІ генерує розгорнуту відповідь..."):
        try:
            # Запит до OpenAI
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Ти — професійний еколог-експерт. Твої відповіді мають бути дуже розгорнутими (не менше 500 слів), структурованими за допомогою Markdown, з використанням заголовків, списків та наукових фактів. Пиши українською мовою."},
                    {"role": "user", "content": prompt}
                ]
            )
            ai_response = response.choices[0].message.content
        except Exception as e:
            ai_response = f"Помилка підключення: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    st.rerun()
