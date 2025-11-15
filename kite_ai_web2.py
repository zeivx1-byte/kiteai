# kite_ai_web2.py
# Streamlit Web Version of KITE-AI (Integrated for CPE 2nd Year)
# Includes Physics, Circuits, AI Toolkit, Task Manager, and CPE Chatbot

import streamlit as st
import numpy as np
import os

# --- Modern Sophisticated UI Theme ---
st.set_page_config(page_title="KITE-AI Web 2.0", page_icon="🤖", layout="wide")
# --- Small Header Icon ---
icon_url = "https://raw.githubusercontent.com/zeivx1-byte/kiteai/main/568672685_718166897320759_4217860298229868715_n.jpg"

st.markdown(f"""
    <div style="
        display: flex;
        justify-content: center;
        align-items: center;
        padding-top: 5px;
        padding-bottom: 10px;
    ">
        <img src="{icon_url}" style="
            width: 70px;
            height: 70px;
            border-radius: 50%;
            box-shadow: 0 0 15px rgba(255,60,60,0.5);
            border: 2px solid rgba(255,255,255,0.3);
        ">
    </div>
""", unsafe_allow_html=True)


# === GLOBAL THEME (Dark Neon Style + Red Header) ===
st.markdown("""
<style>
/* === GLOBAL BACKGROUND === */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #0a0a0f 0%, #101520 60%, #0b0c10 100%);
    color: white !important;
    font-family: 'Segoe UI', sans-serif;
}

/* === HEADER FIX === */
header[data-testid="stHeader"] {
    background: linear-gradient(90deg, #2b0000, #4a0000, #2b0000);
    color: #FF4C4C !important;
    box-shadow: 0 0 25px rgba(255, 60, 60, 0.3);
    border-bottom: 1px solid rgba(255, 80, 80, 0.4);
}

/* === SIDEBAR === */
[data-testid="stSidebar"] {
    background: rgba(30, 0, 0, 0.8);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255, 50, 50, 0.2);
}
[data-testid="stSidebar"] * {
    color: #FFD6D6 !important;
}

/* === HEADINGS === */
h1, h2, h3, h4 {
    color: #FF4C4C !important;
    text-shadow: 0 0 25px rgba(255, 60, 60, 0.5);
}

/* === BUTTONS === */
button[kind="primary"] {
    background: linear-gradient(135deg, #B00000, #FF0000);
    color: white !important;
    border-radius: 12px;
    border: none;
    box-shadow: 0 0 15px rgba(255, 60, 60, 0.3);
    transition: all 0.2s ease-in-out;
}
button[kind="primary"]:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(255, 80, 80, 0.6);
}
button {
    background-color: rgba(40, 0, 0, 0.8) !important;
    color: #FF4C4C !important;
    border: 1px solid rgba(255, 50, 50, 0.4);
    border-radius: 10px;
    transition: 0.3s;
}
button:hover {
    background-color: rgba(70, 0, 0, 0.9) !important;
    box-shadow: 0 0 20px rgba(255, 60, 60, 0.4);
}

/* === SIDEBAR TITLE === */
[data-testid="stSidebarNav"]::before {
    content: "🔥 KITE-AI SYSTEM";
    margin-left: 15px;
    margin-top: 10px;
    font-size: 20px;
    font-weight: 700;
    color: #FF4C4C;
    text-shadow: 0 0 25px rgba(255, 80, 80, 0.6);
}

/* === FOOTER HIDDEN === */
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Sidebar Menu ---
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🗂️ Task Manager", "⚙️ Physics Calculator",
     "📏 Unit Converter", "🔌 Electrical Assistant",
     "💬 CPE Chatbot", "📘 About"]
)

# -------------------- HOME --------------------
# -------------------- HOME --------------------
if menu == "🏠 Home":
    bg_url = "https://raw.githubusercontent.com/zeivx1-byte/kiteai/main/BSU.jpg"

    # --- Hero Banner ---
    st.markdown(f"""
    <style>
    .hero {{
        position: relative;
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
        height: 550px;
        border-radius: 15px;
        text-align: center;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 0 30px rgba(255,60,60,0.4);
    }}
    .overlay {{
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.5);
        border-radius: 15px;
    }}
    .hero-content {{
        position: relative;
        z-index: 1;
        padding: 20px;
    }}
    .hero h1 {{
        font-size: 55px;
        font-weight: 800;
        color: #FF4C4C;
        text-shadow: 0 0 25px rgba(255,60,60,0.7);
    }}
    .hero h3 {{
        font-size: 22px;
        background: rgba(255, 0, 0, 0.6);
        display: inline-block;
        padding: 10px 25px;
        border-radius: 10px;
        color: white;
        font-weight: 600;
        box-shadow: 0 0 20px rgba(255,60,60,0.4);
    }}
    .vision {{
        margin-top: 60px;
        padding: 30px;
        background: rgba(40, 0, 0, 0.6);
        border-radius: 15px;
        box-shadow: 0 0 25px rgba(255, 60, 60, 0.3);
        text-align: center;
    }}
    .vision h2 {{
        color: #FF4C4C;
        text-shadow: 0 0 20px rgba(255,60,60,0.5);
        font-size: 34px;
        margin-bottom: 15px;
    }}
    .vision p {{
        color: #FFEAEA;
        font-size: 18px;
        line-height: 1.6;
        margin: 0 auto;
        max-width: 850px;
    }}
    </style>
    """, unsafe_allow_html=True)

    # --- Hero Section ---
    st.markdown("""
    <div class="hero">
        <div class="overlay"></div>
        <div class="hero-content">
            <h1>WELCOME TO THE KITE WEB COMPANION</h1>
            <h3>Empowering Computer Engineering Students with Essential Tools</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- VISION Section ---
    st.markdown("""
    <div class="vision">
        <h2>Our VISION</h2>
        <p>
        At <strong>COMKITE</strong>, we are dedicated to revolutionizing the learning experience 
        for Computer Engineering students. Our goal is to provide a comprehensive suite of 
        computational tools and resources to enhance their academic journey and prepare them 
        for real-world challenges.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- TASK MANAGER --------------------
elif menu == "🗂️ Task Manager":
    st.header("🗂️ Task Manager")

    task_file = "tasks.txt"

    def load_tasks():
        if os.path.exists(task_file):
            with open(task_file, "r") as f:
                return [line.strip() for line in f.readlines()]
        return []

    def save_tasks(tasks):
        with open(task_file, "w") as f:
            for t in tasks:
                f.write(t + "\n")

    tasks = load_tasks()
    new_task = st.text_input("Add new task:")
    if st.button("Add Task"):
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            st.success(f"Task added: {new_task}")
        else:
            st.warning("Enter a task first!")

    if tasks:
        st.subheader("Your Tasks:")
        for i, t in enumerate(tasks):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.write(f"{i+1}. {t}")
            with col2:
                if st.button("❌", key=f"del_{i}"):
                    tasks.pop(i)
                    save_tasks(tasks)
                    st.experimental_rerun()
    else:
        st.info("No tasks added yet.")

# -------------------- PHYSICS CALCULATOR --------------------
elif menu == "⚙️ Physics Calculator":
    st.header("⚙️ Physics Calculator")
    options = st.selectbox("Choose a formula:", [
        "Force (F = m * a)",
        "Work (W = F * d)",
        "Power (P = W / t)",
        "Kinetic Energy (KE = 0.5 * m * v²)",
        "Potential Energy (PE = m * g * h)"
    ])

    if options == "Force (F = m * a)":
        m = st.number_input("Mass (kg)", 0.0)
        a = st.number_input("Acceleration (m/s²)", 0.0)
        if st.button("Compute Force"):
            st.success(f"Force = {m * a:.2f} N")

    elif options == "Work (W = F * d)":
        F = st.number_input("Force (N)", 0.0)
        d = st.number_input("Distance (m)", 0.0)
        if st.button("Compute Work"):
            st.success(f"Work = {F * d:.2f} J")

    elif options == "Power (P = W / t)":
        W = st.number_input("Work (J)", 0.0)
        t = st.number_input("Time (s)", 0.0)
        if st.button("Compute Power"):
            if t != 0:
                st.success(f"Power = {W / t:.2f} W")
            else:
                st.error("Time cannot be zero.")

    elif options == "Kinetic Energy (KE = 0.5 * m * v²)":
        m = st.number_input("Mass (kg)", 0.0)
        v = st.number_input("Velocity (m/s)", 0.0)
        if st.button("Compute KE"):
            st.success(f"Kinetic Energy = {0.5 * m * v ** 2:.2f} J")

    elif options == "Potential Energy (PE = m * g * h)":
        m = st.number_input("Mass (kg)", 0.0)
        g = st.number_input("Gravity (m/s²)", 9.81)
        h = st.number_input("Height (m)", 0.0)
        if st.button("Compute PE"):
            st.success(f"Potential Energy = {m * g * h:.2f} J")

# -------------------- UNIT CONVERTER --------------------
elif menu == "📏 Unit Converter":
    st.header("📏 Unit Converter")
    conv_type = st.selectbox("Select Conversion Type:", [
        "Length (m ↔ ft)",
        "Mass (kg ↔ lb)",
        "Temperature (°C ↔ °F)",
        "Speed (km/h ↔ mph)"
    ])

    if conv_type == "Length (m ↔ ft)":
        m = st.number_input("Meters", 0.0)
        st.write(f"{m} m = {m * 3.28084:.2f} ft")

    elif conv_type == "Mass (kg ↔ lb)":
        kg = st.number_input("Kilograms", 0.0)
        st.write(f"{kg} kg = {kg * 2.20462:.2f} lb")

    elif conv_type == "Temperature (°C ↔ °F)":
        c = st.number_input("Temperature (°C)", 0.0)
        st.write(f"{c}°C = {(c * 9/5) + 32:.2f}°F")

    elif conv_type == "Speed (km/h ↔ mph)":
        kmh = st.number_input("Speed (km/h)", 0.0)
        st.write(f"{kmh} km/h = {kmh * 0.621371:.2f} mph")

# -------------------- ELECTRICAL ASSISTANT --------------------
elif menu == "🔌 Electrical Assistant":
    st.header("🔌 Electrical Circuit Assistant")
    option = st.selectbox("Choose Calculation:", [
        "Ohm's Law (V = I * R)",
        "Power (P = V * I)",
        "Series Resistance",
        "Parallel Resistance"
    ])

    if option == "Ohm's Law (V = I * R)":
        I = st.number_input("Current (A)", 0.0)
        R = st.number_input("Resistance (Ω)", 0.0)
        st.write(f"Voltage = {I * R:.2f} V")

    elif option == "Power (P = V * I)":
        V = st.number_input("Voltage (V)", 0.0)
        I = st.number_input("Current (A)", 0.0)
        st.write(f"Power = {V * I:.2f} W")

    elif option == "Series Resistance":
        resistors = st.text_input("Enter resistances (comma-separated):")
        if resistors:
            try:
                values = [float(r.strip()) for r in resistors.split(",")]
                st.success(f"Total Resistance = {sum(values):.2f} Ω")
            except:
                st.error("Invalid input.")

    elif option == "Parallel Resistance":
        resistors = st.text_input("Enter resistances (comma-separated):")
        if resistors:
            try:
                values = [float(r.strip()) for r in resistors.split(",")]
                total = 1 / sum(1/r for r in values if r != 0)
                st.success(f"Total Resistance = {total:.2f} Ω")
            except:
                st.error("Invalid input.")


# -------------------- CPE CHATBOT --------------------
elif menu == "💬 CPE Chatbot":
    st.header("💬 CPE Student ChatBot")
    st.markdown("Ask me anything about Computer Engineering 2nd Year!")

    # --- Chatbot Styling ---
    st.markdown("""
    <style>
    .chat-message {
        border-radius: 12px;
        padding: 12px 18px;
        margin: 8px 0;
        max-width: 85%;
        line-height: 1.5;
        font-size: 16px;
    }
    .chat-message.user {
        background-color: #FF4C4C;
        color: white;
        margin-left: auto;
        text-align: right;
        box-shadow: 0 0 15px rgba(255,60,60,0.5);
    }
    .chat-message.assistant {
        background-color: #f5f5f5;
        color: #222;
        margin-right: auto;
        text-align: left;
        box-shadow: 0 0 15px rgba(255,255,255,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Teacher Database ---
    teachers_info = {
        "prof jennifer l. marasigan": {"name": "Prof. Jennifer L. Marasigan",
                                       "subject": "CpE 403 - Computer Engineering as a Discipline",
                                       "office": "CICS 2nd Flr"},
        # Add other professors here
    }

    # --- Chat history & API cache ---
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "api_cache" not in st.session_state:
        st.session_state.api_cache = {}  # key: question, value: answer

    # --- User input ---
    user_input = st.text_input("You:", placeholder="Ask something...")

    if user_input:
        from difflib import get_close_matches
        import requests
        import os

        # --- Check teacher database first ---
        user_lower = user_input.lower()
        response_text = "🤔 I'm not sure yet. You can ask your class representative."

        closest = get_close_matches(user_lower, teachers_info.keys(), n=1, cutoff=0.6)
        if closest:
            info = teachers_info[closest[0]]
            response_text = f"**{info['name']}**\nSubject: {info['subject']}\nOffice: {info['office']}"
        else:
            # --- Check if cached ---
            if user_input in st.session_state.api_cache:
                response_text = st.session_state.api_cache[user_input]
            else:
                # --- Call OpenRouter ---
                OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your_api_key_here")
                headers = {
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "HTTP-Referer": "https://kite-ai-web",
                    "X-Title": "KITE-AI Chatbot"
                }
                payload = {
                    "model": "meta-llama/llama-3.3-70b-instruct:free",
                    "messages": [
                        {"role": "system", "content": 
                         "You are KITE-AI, a friendly AI assistant for Computer Engineering students."},
                        {"role": "user", "content": user_input}
                    ]
                }
                try:
                    with st.spinner("KITE-AI is thinking..."):
                        response = requests.post(
                            "https://openrouter.ai/api/v1/chat/completions",
                            headers=headers,
                            json=payload,
                            timeout=8
                        )
                        response.raise_for_status()
                        data = response.json()
                        response_text = data["choices"][0]["message"]["content"]
                        # --- Save to cache ---
                        st.session_state.api_cache[user_input] = response_text
                except requests.exceptions.RequestException as e:
                    response_text = (
                        "⚠️ KITE-AI couldn't reach OpenRouter.\n"
                        "You can still ask about professors, or try again later.\n"
                        f"(Error: {e})"
                    )
                except Exception as e:
                    response_text = f"⚠️ Unexpected error: {e}"

        # --- Save to chat history ---
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": response_text})

    # --- Display chat history ---
    for msg in st.session_state.chat_history:
        role_class = "user" if msg["role"]=="user" else "assistant"
        st.markdown(f'<div class="chat-message {role_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# -------------------- ABOUT --------------------
elif menu == "📘 About":
    st.header("📘 About KITE-AI Web 2.0")
    st.markdown("""
    **Developed for:** Computer Engineering 2nd Year  
    **Purpose:** To integrate Engineering problem-solving and basic AI simulations  
    **Modules Included:**  
    - Task Manager  
    - Physics & Electrical Calculators  
    - Unit Converters  
    - AI Demos (Logic Gates, Perceptron)  
    - Student Chatbot  
    """)











