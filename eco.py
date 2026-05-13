import streamlit as st

# Повне налаштування стилів
st.set_page_config(page_title="Еко-Портал", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f0fdf4; }
    [data-testid="stSidebar"] { background-color: #dcfce7; }
    .st-emotion-cache-16idsys p, .st-ae { color: #166534 !important; font-weight: bold; }
    h1, h2, h3 { color: #14532d !important; }
    .stButton>button { background-color: #22c55e; color: white; border-radius: 10px; width: 100%; }
    .stChatInputContainer { background-color: #ffffff; border: 2px solid #22c55e; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# Розширена база даних
eco_data = {
    "Як сортувати сміття?": {
        "text": """**Інструкція зі сортування сміття:**
* **Пластик:** Тільки маркування 1, 2, 4, 5. Обов'язково мити та стискати.
* **Папір:** Чистий картон та офісний папір. Не кидайте чеки та серветки.
* **Скло:** Банки та пляшки без кришок.
* **Метал:** Алюмінієві бляшанки та жерстяні банки від консервів.""",
        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=600"
    },
    "Як очистити воду?": {
        "text": """**Методи очищення води вдома:**
1. **Кип'ятіння:** Найпростіший спосіб вбити бактерії (кип'ятити не менше 5-10 хв).
2. **Фільтрація:** Використання вугільних фільтрів-глечиків для видалення хлору.
3. **Відстоювання:** Дозволяє випаруватися хлору та осісти важким часткам (мінімум 6-8 годин).
4. **Заморожування:** "Тала вода" вважається чистішою, оскільки лід витісняє домішки.""",
        "img": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?q=80&w=600"
    },
    "Захист лісів": {
        "text": """**Чому важливо берегти ліси?**
Ліси — це легені планети та дім для 80% сухопутних мешканців. Що ти можеш зробити:
* Використовуй менше паперу та здавай макулатуру.
* Не розпалюй багаття у невстановлених місцях.
* Висаджуй дерева під час волонтерських акцій.""",
        "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=600"
    }
}

# БІЧНА ПАНЕЛЬ
st.sidebar.title("🌸 Еко-Меню")
topic = st.sidebar.radio("Оберіть тему:", list(eco_data.keys()) + ["Інше питання.."])

with st.sidebar.expander("🌸 Файли та медіа"):
    uploaded_file = st.file_uploader("📁 Завантажити", type=['png', 'jpg', 'pdf'])
    img_file = st.camera_input("📸 Камера")

# ГОЛОВНИЙ ЕКРАН
st.title("🌱 Інтерактивний Еко-Помічник")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Логіка автоматичних відповідей по темах
if "current_topic" not in st.session_state or st.session_state.current_topic != topic:
    if topic != "Інше питання..":
        st.session_state.current_topic = topic
        resp = eco_data[topic]
        st.session_state.messages.append({"role": "assistant", "content": resp["text"], "image": resp["img"]})

# Відображення чату
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"], width=600)

# ОБРОБКА ПИТАНЬ КОРИСТУВАЧА
if prompt := st.chat_input("Напишіть своє питання тут..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        p_low = prompt.lower()
        # Пошук ключових слів для розгорнутої відповіді
        if "вод" in p_low:
            data = eco_data["Як очистити воду?"]
            ans, img = data["text"], data["img"]
        elif "смітт" in p_low or "сортув" in p_low:
            data = eco_data["Як сортувати сміття?"]
            ans, img = data["text"], data["img"]
        elif "ліс" in p_low or "дерев" in p_low:
            data = eco_data["Захист лісів"]
            ans, img = data["text"], data["img"]
        else:
            ans = f"Дякую за питання про '{prompt}'! Це важлива екологічна тема. Рекомендую дослідити наукові статті про вплив людини на біосферу."
            img = "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=600"
        
        st.markdown(ans)
        st.image(img, width=600)
        st.session_state.messages.append({"role": "assistant", "content": ans, "image": img})
