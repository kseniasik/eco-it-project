import streamlit as st

# 1. Налаштування сторінки
st.set_page_config(page_title="Еко-Портал 2026", layout="wide")

# 2. Налаштування шрифтів
st.sidebar.title("⚙️ Налаштування")
font_choice = st.sidebar.selectbox("Оберіть шрифт інтерфейсу:", ["Tahoma", "Default", "Serif", "Monospace"])
fonts = {"Tahoma": "Tahoma, sans-serif", "Default": "sans-serif", "Serif": "serif", "Monospace": "monospace"}
f = fonts[font_choice]

# 3. Стилізація
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

# 4. ВЕЛИКА БАЗА ДАНИХ
eco_database = {
    "🏠 Головна": {
        "text": """# Ласкаво просимо до Інтерактивного Еко-Порталу! 🌱
Цей проект — комплексна база знань для кожного, хто прагне змінити своє ставлення до довкілля. Сьогодні екологічна грамотність — це необхідна навичка для виживання людства. Наш портал допоможе розібратися у найскладніших питаннях: від молекулярного складу пластику до стратегій відновлення лісів.

**Чому це важливо?**
Ми живемо в епоху, коли людська діяльність стала головною силою, що змінює Землю. Темпи вимирання видів зросли, а температура планети піднімається. Але знання дозволяють нам зупинити катастрофу.""",
        "img": "https://images.unsplash.com/photo-1518173946687-a4c8a9ba332f?q=80&w=1200"
    },
    "♻️ Як сортувати сміття?": {
        "text": """# Глобальна стратегія сортування відходів ♻️
Сортування — перший крок до циркулярної економіки. Коли ми викидаємо пакет у загальний смітник, ми втрачаємо ресурси.

### 1. Пластик
* **PET (1):** Пляшки від води. Найкраще переробляються.
* **HDPE (2):** Щільний пластик від шампунів.
* **PP (5):** Контейнери від йогуртів.
**ПРАВИЛО:** Помити від залишків їжі та ОБОВ'ЯЗКОВО стиснути.

### 2. Макулатура
Тонна паперу економить 17 дерев та 26 000 літрів води.
* **Здаємо:** Картон, офісний папір, газети.
* **НЕ здаємо:** Чеки, серветки, стаканчики.

### 3. Небезпечні відходи
Батарейки та лампи отруюють 20 кв. метрів землі. Їх не можна кидати у звичайні баки!""",
        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=1200"
    },
    "🌲 Захист лісів": {
        "text": """# Ліси як фундамент стабільності 🌲
Ліси займають 31% суходолу, але ми втрачаємо площу з 27 футбольних полів щохвилини.

### Чому ліс важливий?
1. **Водний цикл:** Дерева діють як губки, утримуючи вологу.
2. **Легені планети:** Гектар лісу виділяє кисень для дихання 10-30 людей.

### Як допомогти?
Обирайте товари з маркуванням FSC та підтримуйте проекти з висадки дерев.""",
        "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200"
    }
}

# 5. Навігація
all_topics = ["🏠 Головна", "♻️ Як сортувати сміття?", "🌲 Захист лісів", "💬 Інше питання"]
topic = st.sidebar.radio("🌸 Еко-Меню:", all_topics)

if "messages" not in st.session_state:
    st.session_state.messages = []

# 6. ЛОГІКА ОНОВЛЕННЯ КОНТЕНТУ
if "current_topic" not in st.session_state or st.session_state.current_topic != topic:
    st.session_state.current_topic = topic
    if topic != "💬 Інше питання":
        # Відображаємо статтю з бази
        res = eco_database[topic]
        st.session_state.messages = [{"role": "assistant", "content": res["text"], "image": res["img"]}]
    else:
        # Режим чистого чату
        st.session_state.messages = [{"role": "assistant", "content": "# 💬 Задайте своє питання\nТут я відповім на будь-що про екологію!"}]

# 7. ВІДОБРАЖЕННЯ
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

# 8. ЧАТ-БОТ (Відповідь на конкретне питання)
if prompt := st.chat_input("Напишіть своє питання..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # ФОРМУЄМО ВІДПОВІДЬ БЕЗ ПРИВ'ЯЗКИ ДО СТАТТІ
    detailed_ans = f"""# Відповідь на питання: "{prompt}"

Ваш запит дуже важливий. Щодо **{prompt}**, можна виділити наступне:

1. **Суть проблеми:** Це напряму впливає на екосистему у 2026 році.
2. **Науковий погляд:** Останні дослідження показують, що свідомий підхід до цієї теми зменшує вуглецевий слід на 15-20%.
3. **Рекомендація:** Раджу звернути увагу на локальні еко-ініціативи, які працюють саме в цьому напрямку.

Бажаєте уточнити деталі щодо цього питання?"""
    
    st.session_state.messages.append({"role": "assistant", "content": detailed_ans})
    st.rerun()
