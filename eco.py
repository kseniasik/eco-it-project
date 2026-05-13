import streamlit as st

# Налаштування сторінки та стилів (зелена тема)
st.set_page_config(page_title="Еко-Портал", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #f0fdf4; }
    .st-emotion-cache-16idsys p { color: #166534; font-weight: bold; }
    .stButton>button { background-color: #22c55e; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# База знань та картинки для тем
eco_data = {
    "Як сортувати сміття?": {
        "text": "Розділяйте папір, пластик, скло та метал. Мийте тару перед викиданням!",
        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=400"
    },
    "Що можна зробити для збереження біорізноманіття?": {
        "text": "Відновлюйте екосистеми, саджайте місцеві рослини та відмовтеся від пестицидів.",
        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=400"
    },
    "Що може зробити дитина для збереження природи?": {
        "text": "Вимикай воду під час чищення зубів, бережи папір та не сміти в лісі!",
        "img": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=400"
    },
    "Чому для збереження біосфери необхідно охороняти біорізноманіття?": {
        "text": "Це забезпечує стабільність клімату, чисту воду та їжу для всіх людей.",
        "img": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400"
    },
    "Яка роль заповідних територій у збереженні біологічного різноманіття?": {
        "text": "Заповідники — це 'сейфи' дикої природи, де рідкісні види захищені від людини.",
        "img": "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?q=80&w=400"
    },
    "Як можна досліджувати природу?": {
        "text": "Використовуйте спостереження, польові щоденники та цифрові додатки (як iNaturalist).",
        "img": "https://images.unsplash.com/photo-1551029506-0807df4e2031?q=80&w=400"
    },
    "Як співіснують людина і природа від минулого дотепер?": {
        "text": "Від повної залежності ми перейшли до великого впливу на клімат. Час повертати баланс!",
        "img": "https://images.unsplash.com/photo-1518173946687-a4c8a9ba332f?q=80&w=400"
    },
    "Як можна зберегти довкілля та ще й зекономити?": {
        "text": "Енергоефективні лампи, багаторазові сумки та відмова від зайвого споживання.",
        "img": "https://images.unsplash.com/photo-1473116763249-2faaef81ccda?q=80&w=400"
    },
    "Як поводитися в разі зустрічі з дикими тваринами?": {
        "text": "Зберігай спокій, не роби різких рухів, не годуй їх і повільно відходь.",
        "img": "https://images.unsplash.com/photo-1535941323137-1deca9959e75?q=80&w=400"
    },
    "Інше питання...": {
        "text": "Я слухаю! Напиши будь-яке інше екологічне питання в чат.",
        "img": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=400"
    }
}

# Бічна панель
st.sidebar.title("🌸 Еко-Меню")
topic = st.sidebar.radio("Оберіть тему для обговорення:", list(eco_data.keys()))

# Кнопка з квіточкою (меню файлів)
with st.sidebar.expander("🌸 Файли та медіа"):
    st.write("📁 Відправити файл")
    st.write("📸 Зробити відео або фото")
    st.write("☁️ Додати з Google Диска")

st.title("🌱 Інтерактивний Еко-Помічник")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Автоматична відповідь при зміні теми
if "current_topic" not in st.session_state or st.session_state.current_topic != topic:
    st.session_state.current_topic = topic
    ai_resp = eco_data[topic]
    st.session_state.messages.append({
        "role": "assistant", 
        "content": ai_resp["text"], 
        "image": ai_resp["img"]
    })

# Відображення чату
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"], width=300)

# Поле вводу
if prompt := st.chat_input("Запитай щось додатково..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        final_text = f"Твоє питання '{prompt}' дуже важливе для екології {topic}! Я вивчаю це..."
        st.markdown(final_text)
        st.session_state.messages.append({"role": "assistant", "content": final_text})
