import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Еко-Портал", layout="wide")

# ПЕРЕДВИБІР ШРИФТУ НА БІЧНІЙ ПАНЕЛІ
st.sidebar.title("⚙️ Налаштування")
font_choice = st.sidebar.selectbox(
    "Оберіть шрифт інтерфейсу:",
    ["Default", "Serif (Classic)", "Monospace (Tech)", "Tahoma (Clean)"]
)

# Словник шрифтів
fonts = {
    "Default": "sans-serif",
    "Serif (Classic)": "'Georgia', serif",
    "Monospace (Tech)": "'Courier New', monospace",
    "Tahoma (Clean)": "'Tahoma', sans-serif"
}
selected_font = fonts[font_choice]

# ОНОВЛЕНА СТИЛІЗАЦІЯ (Telegram-style та шрифти)
st.markdown(f"""
    <style>
    .stApp {{ 
        background-color: #f0fdf4; 
        font-family: {selected_font};
    }}
    [data-testid="stSidebar"] {{ background-color: #dcfce7; min-width: 320px; }}
    
    /* Стиль повідомлень як у месенджерах */
    .chat-bubble {{
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        display: flex;
        align-items: flex-start;
        gap: 15px;
    }}
    .user-bubble {{ background-color: #e2fceb; border: 1px solid #bcf0d1; }}
    .bot-bubble {{ background-color: #ffffff; border: 1px solid #e5e7eb; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
    
    /* Аватарки */
    .avatar {{
        width: 45px;
        height: 45px;
        border-radius: 50%;
        object-fit: cover;
        flex-shrink: 0;
    }}
    
    .main-article {{ font-size: 17px; line-height: 1.8; color: #1f2937; }}
    h1, h2, h3 {{ color: #064e3b !important; font-family: {selected_font}; }}
    </style>
    """, unsafe_allow_html=True)

# ПОВНА БАЗА ДАНИХ (12 ТЕМ)
eco_database = {
    "🏠 Головна": {
        "text": "Привіт! Я твій персональний еко-асистент. Тут ти знайдеш відповіді на всі запитання про порятунку планети. Обирай тему зліва або пиши в чат!",
        "img": "https://images.unsplash.com/photo-1518173946687-a4c8a9ba332f?q=80&w=1200"
    },
    "♻️ Як сортувати сміття?": {
        "text": "# Сортування відходів\\nСортування сміття — це фундамент цивілізованого суспільства. Кожна тонна макулатури рятує 17 дерев. Сортуйте пластик, скло та папір окремо!",
        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=1200"
    },
    "🌲 Захист лісів": {
        "text": "# Бережіть ліс\\nЛіси — це легені планети. Одне дерево виробляє кисень для двох людей. Відмовся від зайвого паперу та підтримуй висадку дерев.",
        "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200"
    },
    "🦋 Біорізноманіття": {
        "text": "# Світ тварин\\nЗбереження кожного виду комах чи птахів критичне для екосистеми. Пам'ятай: без бджіл не буде врожаю!",
        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=1200"
    },
    "💧 Вода - життя": {
        "text": "# Економія води\\nЛише 0.5% води на Землі придатні для пиття. Вимикай кран, коли чистиш зуби — це економить до 10 літрів на хвилину.",
        "img": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?q=80&w=1200"
    },
    "☀️ Еко-енергія": {
        "text": "# Зелена енергія\\nСонце та вітер — невичерпні джерела. Переходь на LED-лампи, вони споживають у 10 разів менше електрики.",
        "img": "https://images.unsplash.com/photo-1509391366360-fe5bb629550d?q=80&w=1200"
    },
    "🍎 Еко-харчування": {
        "text": "# Свідома тарілка\\nКупуй локальні та сезонні продукти. Це зменшує викиди вуглецю від транспортування їжі літаками.",
        "img": "https://images.unsplash.com/photo-1498837167922-ddd27525d352?q=80&w=1200"
    },
    "👗 Стала мода": {
        "text": "# Менше речей — більше сенсу\\nІндустрія моди забруднює воду. Обирай секонд-хенди та якісні речі з натуральних тканин.",
        "img": "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?q=80&w=1200"
    },
    "🚲 Транспорт": {
        "text": "# Рухайся екологічно\\nВелосипед або піша прогулянка — найкращий вибір для подорожей на короткі відстані.",
        "img": "https://images.unsplash.com/photo-1507035895480-2b3156c31fc8?q=80&w=1200"
    },
    "🐾 Дика природа": {
        "text": "# Повага до тварин\\nНе годуй диких тварин людською їжею. Це шкодить їхньому здоров'ю та природним інстинктам.",
        "img": "https://images.unsplash.com/photo-1535941323137-1deca9959e75?q=80&w=1200"
    },
    "🔎 Дослідження": {
        "text": "# Стань еко-вченим\\nВикористовуй додатки для розпізнавання рослин. Досліджуй природу свого рідного краю щодня!",
        "img": "https://images.unsplash.com/photo-1551029506-0807df4e2031?q=80&w=1200"
    },
    "💬 Інше питання": {
        "text": "Тут ти можеш запитати будь-що! Я проаналізую твій запит і дам максимально розгорнуту відповідь.",
        "img": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=1200"
    }
}

# БІЧНА ПАНЕЛЬ ТЕМИ
st.sidebar.title("🌸 Еко-Меню")
topic = st.sidebar.radio("Оберіть тему:", list(eco_database.keys()))

# ІНТЕРФЕЙС
st.title("🌱 Інтерактивний Еко-Портал v6.0")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Оновлення при виборі теми
if "current_topic" not in st.session_state or st.session_state.current_topic != topic:
    st.session_state.current_topic = topic
    res = eco_database[topic]
    st.session_state.messages.append({"role": "assistant", "content": res["text"], "image": res["img"]})

# ВІДОБРАЖЕННЯ ЧАТУ (З ІКОНКАМИ)
user_icon = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
bot_icon = "https://cdn-icons-png.flaticon.com/512/11013/11013833.png"

for msg in st.session_state.messages:
    role_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    icon_url = user_icon if msg["role"] == "user" else bot_icon
    
    st.markdown(f"""
        <div class="chat-bubble {role_class}">
            <img src="{icon_url}" class="avatar">
            <div class="main-article">{msg["content"]}</div>
        </div>
    """, unsafe_allow_html=True)
    
    if "image" in msg:
        st.image(msg["image"], use_container_width=True)

# ВВЕДЕННЯ ПИТАННЯ
if prompt := st.chat_input("Напишіть своє питання тут..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()
