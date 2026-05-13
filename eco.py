import streamlit as st

# Налаштування стилів
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

# Детальна база даних тем
eco_data = {
    "Як сортувати сміття?": {
        "text": """**Правильне сортування сміття** передбачає очищення та розділення відходів на пластик, папір, скло, метал та органіку.

**Основні категорії:**
* **Пластик (жовтий контейнер):** Пляшки від напоїв (PET), побутової хімії (HDPE). **Важливо:** Стискайте пляшки! Не можна: PVC (3) або одноразовий посуд.
* **Папір (синій контейнер):** Газети, картон. Має бути сухим. Не можна: чеки, лотки для яєць, Tetra Pak.
* **Скло (зелений контейнер):** Банки, пляшки. Не можна: дзеркала, лампочки.
* **Метал:** Консервні банки. Помити від залишків їжі.
* **Небезпечні відходи:** Батарейки, лампи — здавати тільки у спеціальні пункти.""",
        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=600"
    },
    "Що можна зробити для збереження біорізноманіття?": {
        "text": """Збереження біорізноманіття — це захист стабільності нашої планети.
* **Відновлення:** Саджайте місцеві види дерев та кущів.
* **Еко-захист:** Відмовтеся від пестицидів, які вбивають корисних комах.
* **Свідоме споживання:** Обирайте товари без мікропластику.""",
        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=600"
    },
    "Що може зробити дитина для збереження природи?": {
        "text": """Кожна дитина — справжній еко-герой!
1. **Бережи ресурси:** Закривай воду, вимикай зайве світло.
2. **Нуль відходів:** Використовуй багаторазову пляшку для води та еко-сумку.
3. **Освіта:** Розповідай друзям про важливість збереження лісів.""",
        "img": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=600"
    }
    # Додай інші теми сюди за таким же шаблоном
}

# БІЧНА ПАНЕЛЬ
st.sidebar.title("🌸 Еко-Меню")
topic = st.sidebar.radio("Оберіть тему для обговорення:", list(eco_data.keys()))

# ПРАЦЮЮЧЕ МЕНЮ ФАЙЛІВ
with st.sidebar.expander("🌸 Файли та медіа"):
    # Завантаження з телефону або комп'ютера
    uploaded_file = st.file_uploader("📁 Завантажити файл", type=['png', 'jpg', 'pdf', 'docx'])
    if uploaded_file:
        st.sidebar.success(f"Файл {uploaded_file.name} завантажено!")
    
    # Зробити фото (працює на телефонах як селфі-камера)
    img_file = st.camera_input("📸 Зробити фото")
    if img_file:
        st.sidebar.image(img_file, caption="Ваше фото")

    st.write("☁️ [Відкрити мій Google Диск](https://drive.google.com)")

# ГОЛОВНИЙ ЕКРАН
st.title("🌱 Інтерактивний Еко-Помічник")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Автоматична відповідь при виборі теми
if "current_topic" not in st.session_state or st.session_state.current_topic != topic:
    st.session_state.current_topic = topic
    resp = eco_data[topic]
    st.session_state.messages.append({"role": "assistant", "content": resp["text"], "image": resp["img"]})

# Відображення чату
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"], width=500)

# Чат-ввід
if prompt := st.chat_input("Запитай щось додатково..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        final_text = f"Дякую за питання про '{prompt}'! Як ШІ-помічник, я раджу завжди перевіряти маркування на упаковці та дбати про довкілля щодня."
        st.markdown(final_text)
        st.session_state.messages.append({"role": "assistant", "content": final_text})
