import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Еко-Портал", layout="wide")

# Налаштування шрифтів через Sidebar
st.sidebar.title("⚙️ Налаштування")
font_choice = st.sidebar.selectbox(
    "Оберіть шрифт інтерфейсу:",
    ["Default", "Serif", "Monospace", "Tahoma"]
)

fonts = {
    "Default": "sans-serif",
    "Serif": "serif",
    "Monospace": "monospace",
    "Tahoma": "Tahoma"
}

f = fonts[font_choice]

# CSS
st.markdown(f"""
<style>
* {{
    font-family: {f} !important;
}}

.stApp {{
    background-color: #f0fdf4;
}}

[data-testid="stSidebar"] {{
    background-color: #dcfce7;
    min-width: 320px;
}}

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

.avatar {{
    width: 60px;
    height: 60px;
    border-radius: 50%;
    flex-shrink: 0;
}}

.main-article {{
    font-size: 18px !important;
    line-height: 1.8 !important;
    color: #1f2937;
    text-align: justify;
    white-space: pre-wrap;
}}

h1, h2, h3 {{
    color: #064e3b !important;
    font-weight: bold !important;
}}
</style>
""", unsafe_allow_html=True)

# База даних
eco_database = {

    "🏠 Головна": {
        "text": """# Ласкаво просимо до Інтерактивного Еко-Порталу! 🌱

Цей проект створений як комплексна база знань для кожного, хто прагне змінити своє ставлення до навколишнього середовища.

Почніть свою подорож до сталого життя вже сьогодні!""",

        "img": "https://images.unsplash.com/photo-1518173946687-a4c8a9ba332f?q=80&w=1200"
    },

    "♻️ Як сортувати сміття?": {
        "text": """# Глобальна стратегія сортування відходів ♻️

Сортування сміття — це перший і найважливіший крок до циркулярної економіки.

### Основні правила:
* Пластик потрібно мити
* Скло можна переробляти багато разів
* Батарейки не можна викидати у звичайне сміття
* Папір має бути чистим
""",

        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=1200"
    },

    "🌲 Захист лісів": {
        "text": """# Захист лісів 🌲

Ліси — це легені планети.

### Чому ліси важливі:
1. Виробляють кисень
2. Очищують повітря
3. Захищають ґрунти
4. Є домом для тварин
""",

        "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200"
    },

    "🦋 Біорізноманіття": {
        "text": """# Біорізноманіття 🦋

Біорізноманіття — це всі живі організми планети.

### Важливість:
* Запилення рослин
* Очищення води
* Підтримка екосистем
""",

        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=1200"
    }
}

# Додавання інших тем
all_topics = [
    "🏠 Головна",
    "♻️ Як сортувати сміття?",
    "🌲 Захист лісів",
    "🦋 Біорізноманіття",
    "💧 Вода - життя",
    "☀️ Еко-енергія",
    "🍎 Еко-харчування",
    "👗 Стала мода",
    "🚲 Транспорт",
    "🐾 Дика природа",
    "🔎 Дослідження",
    "💬 Інше питання"
]

for t in all_topics:
    if t not in eco_database:
        eco_database[t] = {
            "text": f"""# Розділ: {t}

Тут міститься інформація про екологію, захист природи та сучасні екологічні проблеми.""",

            "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200"
        }

# Sidebar
st.sidebar.title("🌸 Еко-Меню")

topic = st.sidebar.radio(
    "Оберіть тему для обговорення:",
    all_topics
)

# Заголовок
st.title("🌱 Еко-Портал: Велика база знань")

# Історія повідомлень
if "messages" not in st.session_state:
    st.session_state.messages = []

# Зміна теми
if (
    "current_topic" not in st.session_state
    or st.session_state.current_topic != topic
):
    st.session_state.current_topic = topic

    res = eco_database[topic]

    st.session_state.messages.append({
        "role": "assistant",
        "content": res["text"],
        "image": res["img"]
    })

# Іконки
u_icon = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
b_icon = "https://cdn-icons-png.flaticon.com/512/11013/11013833.png"

# Відображення повідомлень
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

# Чат
if prompt := st.chat_input("Напишіть своє питання про екологію..."):

    # Повідомлення користувача
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Логіка відповідей
    if topic == "💬 Інше питання":

        user_q = prompt.lower()

        if "пластик" in user_q:

            detailed_ans = """
# Пластик та екологія ♻️

Пластик є однією з найбільших екологічних проблем сучасності.

### Чому це небезпечно:
* пластик розкладається сотні років
* забруднює океани
* шкодить тваринам
* виділяє токсичні речовини

### Що можна зробити:
* використовувати екоторби
* купувати багаторазові пляшки
* сортувати сміття
* уникати одноразового посуду
"""

        elif "ліс" in user_q or "дерев" in user_q:

            detailed_ans = """
# Захист лісів 🌲

Ліси необхідні для життя на Землі.

### Основні функції:
* вироблення кисню
* очищення повітря
* збереження ґрунтів
* підтримка клімату

### Як допомогти:
* економити папір
* висаджувати дерева
* підтримувати природоохоронні проекти
"""

        elif "вода" in user_q:

            detailed_ans = """
# Вода та екологія 💧

Вода — один із найцінніших ресурсів планети.

### Проблеми:
* забруднення річок
* пластик в океанах
* нестача питної води

### Що робити:
* економити воду
* не забруднювати природу
* використовувати багаторазові пляшки
"""

        elif "енергія" in user_q or "сонце" in user_q:

            detailed_ans = """
# Еко-енергія ☀️

Відновлювана енергія допомагає зменшити забруднення.

### Джерела:
* сонячна енергія
* вітрова енергія
* гідроенергія

### Переваги:
* менше CO₂
* безпечніше для природи
* економія ресурсів
"""

        else:

            detailed_ans = f"""
# Відповідь на ваше питання 🌍

Ваше питання:
"{prompt}"

Це важлива екологічна тема.

### Основні екологічні принципи:
* зменшення забруднення
* сортування сміття
* економія ресурсів
* захист природи

### Корисні дії:
* використовувати багаторазові речі
* економити воду та електроенергію
* підтримувати екологічні ініціативи
"""

    else:
        detailed_ans = eco_database[topic]["text"]

    # Відповідь бота
    st.session_state.messages.append({
        "role": "assistant",
        "content": detailed_ans
    })

    st.rerun()
