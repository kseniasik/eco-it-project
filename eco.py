import streamlit as st

# 1. Налаштування сторінки
st.set_page_config(page_title="Еко-Портал 2026", layout="wide")

# 2. Стан чату для розділу "Інше питання"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 3. Налаштування шрифтів та Sidebar (Зелений фон як на image_38653b.jpg)
st.sidebar.markdown('<p style="font-size:20px; font-weight:bold;">⚙️ Налаштування</p>', unsafe_allow_html=True)
font_choice = st.sidebar.selectbox("Оберіть шрифт інтерфейсу:", ["Tahoma", "Default", "Serif"])

fonts = {"Tahoma": "Tahoma, sans-serif", "Default": "sans-serif", "Serif": "serif"}

st.markdown(f"""
    <style>
    * {{ font-family: {fonts[font_choice]} !important; }}
    [data-testid="stSidebar"] {{ background-color: #e8f5e9 !important; border-right: 1px solid #c8e6c9; }}
    .stApp {{ background-color: white; }}
    .eco-card {{
        background: #fdfdfd;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 25px;
        margin: 10px 0;
        display: flex;
        align-items: center;
        gap: 20px;
    }}
    .main-text {{ font-size: 16px; line-height: 1.8; text-align: justify; color: #2d3436; }}
    h1 {{ color: #1b5e20; font-size: 32px; }}
    </style>
    """, unsafe_allow_html=True)

# 4. Еко-Меню (всі пункти як на скріншоті)
st.sidebar.markdown('<p style="font-size:20px; font-weight:bold; margin-top:20px;">🌸 Еко-Меню</p>', unsafe_allow_html=True)
st.sidebar.write("Оберіть тему для обговорення:")

topic = st.sidebar.radio(
    "Меню",
    [
        "🏠 Головна", "♻️ Як сортувати сміття?", "🌲 Захист лісів", 
        "🦋 Біорізноманіття", "💧 Вода - життя", "☀️ Еко-енергія", 
        "🍎 Еко-харчування", "👗 Стала мода", "🚜 Транспорт", 
        "🌳 Дика природа", "📂 Дослідження", "💬 Інше питання"
    ],
    label_visibility="collapsed"
)

# Функція для генерації 2000 слів (імітація для коду, в реалі тут будуть твої тексти)
def get_huge_text(title):
    base_text = f"Це детальний науковий звіт на тему {title}. " * 150 
    return f"# {title}\n\n" + base_text + "\n\n" + base_text

# 5. Контент тем
if topic != "💬 Інше питання":
    # Картинка зверху як на скріншоті
    st.image("https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=1200")
    
    # Блок з іконкою машинки (як на image_38653b.jpg)
    st.markdown(f"""
    <div class="eco-card">
        <img src="https://cdn-icons-png.flaticon.com/512/11013/11013833.png" width="60">
        <div>
            <p style="font-weight:bold; margin:0;"># Розділ: {topic}</p>
            <p style="margin:0; font-size:14px;">Ця тема детально розкриває вплив людства на конкретну сферу екології. Обсяг інформації відповідає вимогам наукового дослідження (2000+ слів).</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Величезний текст
    st.markdown(f'<div class="main-text">{get_huge_text(topic)}</div>', unsafe_allow_html=True)
    
    # Нижня картинка
    st.image("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1200")

else:
    # РОЗДІЛ "ІНШЕ ПИТАННЯ"
    st.title("💬 Інтерактивний чат з Еко-Помічником")
    st.write("Тут ви можете запитати про що завгодно, і отримати розгорнуту наукову відповідь.")
    
    for m in st.session_state.chat_history:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])

# 6. Поле вводу (працює завжди)
if prompt := st.chat_input("Напишіть своє питання про екологію..."):
    # Додаємо питання в історію
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # Генеруємо відповідь на 2000 слів
    huge_answer = f"### Повна аналітична відповідь на питання: {prompt}\n\n" + ("Ось детальні дані... " * 200)
    st.session_state.chat_history.append({"role": "assistant", "content": huge_answer})
    
    # Якщо ми в розділі "Інше питання", то просто оновлюємо
    # Якщо ми в іншій темі - можна або перекинути в чат, або показати відповідь спливаючим вікном
    st.rerun()
