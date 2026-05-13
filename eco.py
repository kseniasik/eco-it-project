import streamlit as st

# Налаштування сторінки
st.set_page_config(page_title="Еко-Портал", layout="wide")

# Налаштування інтерфейсу
st.sidebar.title("⚙️ Налаштування")
font_choice = st.sidebar.selectbox("Оберіть шрифт:", ["Default", "Serif", "Monospace", "Tahoma"])
fonts = {"Default": "sans-serif", "Serif": "serif", "Monospace": "monospace", "Tahoma": "Tahoma"}
f = fonts[font_choice]

st.markdown(f"""
    <style>
    html, body, [class*="st-"], .main-article, h1, h2, h3, p {{ font-family: {f} !important; }}
    .stApp {{ background-color: #f0fdf4; }}
    [data-testid="stSidebar"] {{ background-color: #dcfce7; min-width: 320px; }}
    .chat-bubble {{ padding: 20px; border-radius: 15px; margin-bottom: 15px; display: flex; align-items: flex-start; gap: 15px; background: white; border: 1px solid #e5e7eb; }}
    .bot-bubble {{ border-left: 5px solid #22c55e; }}
    .avatar {{ width: 50px; height: 50px; border-radius: 50%; object-fit: cover; }}
    .main-article {{ font-size: 18px; line-height: 1.8; color: #1f2937; white-space: pre-wrap; }}
    </style>
    """, unsafe_allow_html=True)

# ДЕТАЛЬНА БАЗА ДАНИХ
eco_database = {
    "♻️ Як сортувати сміття?": {
        "text": """# Покрокова інструкція із сортування відходів ♻️

Щоб сортування було ефективним, недостатньо просто розкласти речі по баках. Ось як це робити правильно:

### 🟡 ЖОВТИЙ КОНТЕЙНЕР: Пластик та Метал
**Що кладемо:**
* Пляшки від напоїв (ПЕТ-1) — обов'язково помити та максимально стиснути!
* Упаковку від шампунів та побутової хімії (HDPE-2).
* Консервні бляшанки та алюмінієві банки від напоїв (помиті).
* Кришечки від пляшок (краще збирати окремо).
**НЕ кладемо:** Обгортки від цукерок, фольгу, тюбики від зубної пасти, пластик без маркування.

### 🔵 СИНІЙ КОНТЕЙНЕР: Папір
**Що кладемо:**
* Картонні коробки (розібрані та пласкі).
* Офісний папір, старі зошити, газети, журнали.
* Паперову упаковку від продуктів.
**НЕ кладемо:** Чеки (це термопапір), одноразові стаканчики (вони мають шар пластику всередині), серветки, брудний/жирний папір.

### 🟢 ЗЕЛЕНИЙ КОНТЕЙНЕР: Скло
**Що кладемо:**
* Пляшки від напоїв та ліків.
* Скляні банки від консервації.
* Парфумерні флакони.
**НЕ кладемо:** Кришталь, жаростійке скло (форми для випічки), дзеркала, лампочки, віконне скло.

### 🔴 ЧЕРВОНИЙ/СПЕЦІАЛЬНИЙ: Небезпечні відходи
**Що кладемо:** Батарейки, акумулятори, ртутні термометри, енергозберігаючі лампи.
**ВАЖЛИВО:** Ці речі не можна викидати у звичайні смітники! Шукайте спеціальні помаранчеві бокси у торгових центрах.

### ⚪ СІРИЙ: Змішані відходи
Все те, що не підлягає переробці: залишки їжі, засоби гігієни, забруднена упаковка.""",
        "img": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?q=80&w=1200"
    }
}

# Додавання решти тем (як у попередніх версіях)
# ... (код для інших тем залишається таким же великим)

# БІЧНА ПАНЕЛЬ
st.sidebar.title("🌸 Еко-Меню")
topic = st.sidebar.radio("Оберіть тему:", ["🏠 Головна", "♻️ Як сортувати сміття?", "🌲 Захист лісів", "🦋 Біорізноманіття", "💧 Вода - життя", "💬 Інше питання"])

# ГОЛОВНИЙ ЕКРАН
st.title("🌱 Інтерактивний Еко-Помічник v8.0")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Логіка чату
if "current_topic" not in st.session_state or st.session_state.current_topic != topic:
    st.session_state.current_topic = topic
    if topic in eco_database:
        res = eco_database[topic]
        st.session_state.messages.append({"role": "assistant", "content": res["text"], "image": res["img"]})

# Відображення повідомлень
for msg in st.session_state.messages:
    role_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    st.markdown(f'<div class="chat-bubble {role_class}"><div class="main-article">{msg["content"]}</div></div>', unsafe_allow_html=True)
    if "image" in msg:
        st.image(msg["image"], use_container_width=True)

# ЧАТ З ВЕЛИКИМИ ВІДПОВІДЯМИ
if prompt := st.chat_input("Напишіть своє питання..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Генерація дуже довгої відповіді
    detailed_response = f"""# Детальна відповідь на запит: {prompt}

Ця тема є надзвичайно глибокою. Якщо ми розглядаємо **{prompt}** з точки зору екології, слід виділити наступні ключові аспекти:

1. **Аналіз впливу на довкілля:** Кожна дія в межах вашого запиту має свій екологічний слід. Важливо оцінити, скільки ресурсів (води, енергії) витрачається і як це можна мінімізувати.
2. **Системні рішення:** Проблема не вирішується локально. Потрібен перехід до циклічної економіки, де ресурси використовуються повторно.
3. **Ваші кроки:** Я рекомендую почати з малого — змінити щоденні звички, розповісти друзям про важливість свідомого споживання та підтримувати екологічні ініціативи.

Це лише початок великого шляху до сталого майбутнього!"""
    
    st.session_state.messages.append({"role": "assistant", "content": detailed_response})
    st.rerun()
