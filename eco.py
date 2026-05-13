import streamlit as st

st.set_page_config(page_title="Eco-AI Portal", layout="wide")

# Бічна панель (як на твоему скріншоті image_3a41f7.png)
st.sidebar.title("🌿 Навігація")
topic = st.sidebar.radio(
    "Оберіть біологічну тему:",
    ("Ботаніка", "Зоологія", "Екологія")
)

st.title(f"Чат з Еко-ІІ: Тема {topic}")

# Створюємо просту базу знань для ІІ
responses = {
    "Ботаніка": "Я допоможу розпізнати рослини. Запитай мене про фотосинтез або рідкісні квіти!",
    "Зоологія": "Я знаю все про тварин. Хочеш дізнатися про міграцію птахів чи захист панд?",
    "Екологія": "Сортування сміття — це важливо! Запитай, куди здати батарейки або як зменшити кількість пластику."
}

# Чат-інтерфейс
if "messages" not in st.session_state:
    st.session_state.messages = []

# Відображення історії чату
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Поле для введення питання
if prompt := st.chat_input("Напиши своє питання..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Відповідь ІІ (базується на обраній темі)
    with st.chat_message("assistant"):
        response = f"Як твій еко-помічник у темі **{topic}**, скажу: {responses[topic]} Твоє питання про '{prompt}' дуже цікаве!"
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
