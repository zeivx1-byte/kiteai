# kite_ai_web2_fixed_full.py
# Streamlit Web Version of KITE-AI Web 2.0
# Fully updated with dark neon red theme, working images, and fixed chatbot

import streamlit as st
import numpy as np
import os
import json
import requests
import time
from difflib import get_close_matches

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="KITE-AI Web 2.0", page_icon="🤖", layout="wide")

# ----------------------------
# GLOBAL STYLES (Dark Neon Red)
# ----------------------------
st.markdown("""
<style>
/* background */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top left, #0a0a0f 0%, #101520 60%, #0b0c10 100%);
    color: #FFEAEA;
    font-family: 'Segoe UI', sans-serif;
}

/* header */
header[data-testid="stHeader"] { 
    background: linear-gradient(90deg,#2b0000,#4a0000,#2b0000); 
    color: #FF4C4C; 
}

/* sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a0000 0%, #3b0000 100%);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255,50,50,0.3);
}
[data-testid="stSidebar"] * {
    color: #FFD6D6 !important;
}
[data-testid="stSidebarNav"]::before {
    content: "🔥 KITE-AI SYSTEM";
    margin-left: 15px;
    margin-top: 10px;
    font-size: 20px;
    font-weight: 700;
    color: #FF4C4C;
}

/* buttons */
button[kind="primary"] {
    background: linear-gradient(135deg, #B00000, #FF0000);
    color: white !important;
    border-radius: 12px;
    border: none;
    box-shadow: 0 0 15px rgba(255, 60, 60,0.4);
}
button[kind="primary"]:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(255,80,80,0.6);
}
button, .stButton>button {
    background-color: rgba(40,0,0,0.8) !important;
    color: #FF4C4C !important;
    border: 1px solid rgba(255,50,50,0.4);
    border-radius: 10px;
    transition: 0.3s;
}
button:hover, .stButton>button:hover {
    background-color: rgba(70,0,0,0.9) !important;
    box-shadow: 0 0 20px rgba(255,60,60,0.4);
}

/* headings */
h1, h2, h3, h4 { color: #FF4C4C !important; text-shadow: 0 0 25px rgba(255,60,60,0.5); }

/* chat bubbles */
.chat-box { padding: 12px 18px; margin: 8px 0; border-radius: 14px; max-width: 85%; font-size: 16px; line-height: 1.4; white-space: pre-wrap; }
.user-msg { background-color: #B00000; color: white; margin-left: auto; text-align: right; }
.bot-msg { background-color: #f5f5f5; color: #222; margin-right: auto; text-align: left; }
.chat-container { max-height: 520px; overflow-y: auto; padding: 14px; border-radius: 12px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,60,60,0.08); }

/* hide footer */
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# SIDEBAR MENU
# ----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🗂️ Task Manager", "⚙️ Physics Calculator",
     "📏 Unit Converter", "🔌 Electrical Assistant", "💬 CPE Chatbot", "📘 About"]
)

# ----------------------------
# HOME PAGE
# ----------------------------
if menu == "🏠 Home":
    bg_url = "https://upload.wikimedia.org/wikipedia/commons/9/97/Batangas_State_University_logo.png"
    st.markdown(f"""
    <div style="
        position: relative;
        background-image: url('{bg_url}');
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
    ">
        <div style='position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);border-radius:15px;'></div>
        <div style='position:relative;z-index:1;'>
            <h1 style='font-size:55px;font-weight:800;color:#FF4C4C;text-shadow:0 0 25px rgba(255,60,60,0.7);'>WELCOME TO THE KITE WEB COMPANION</h1>
            <h3 style='font-size:22px;background:rgba(255,0,0,0.6);display:inline-block;padding:10px 25px;border-radius:10px;color:white;font-weight:600;'>Empowering Computer Engineering Students with Essential Tools</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Vision
    st.markdown("""
    <div style='margin-top:60px;padding:30px;background:rgba(40,0,0,0.6);border-radius:15px;box-shadow:0 0 25px rgba(255,60,60,0.3);text-align:center;'>
        <h2>Our VISION</h2>
        <p>
        At <strong>COMKITE</strong>, we are dedicated to revolutionizing the learning experience 
        for Computer Engineering students. Our goal is to provide a comprehensive suite of 
        computational tools and resources to enhance their academic journey and prepare them 
        for real-world challenges.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# TASK MANAGER
# ----------------------------
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

# ----------------------------
# PHYSICS CALCULATOR
# ----------------------------
elif menu == "⚙️ Physics Calculator":
    st.header("⚙️ Physics Calculator")
    options = st.selectbox("Choose a formula:", [
        "Force (F = m * a)", "Work (W = F * d)", "Power (P = W / t)",
        "Kinetic Energy (KE = 0.5 * m * v²)", "Potential Energy (PE = m * g * h)"
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

# ----------------------------
# UNIT CONVERTER
# ----------------------------
elif menu == "📏 Unit Converter":
    st.header("📏 Unit Converter")
    conv_type = st.selectbox("Select Conversion Type:", [
        "Length (m ↔ ft)", "Mass (kg ↔ lb)", "Temperature (°C ↔ °F)", "Speed (km/h ↔ mph)"
    ])
    if conv_type == "Length (m ↔ ft)":
        m = st.number_input("Meters", 0.0)
        st.write(f"{m} m = {m * 3.28084:.2f} ft")
    elif conv_type == "Mass (kg ↔ lb)":
        kg = st.number_input("Kilograms", 0.0)
        st.write(f"{kg} kg = {kg * 2.20462:.2f} lb")
    elif conv_type == "Temperature (°C ↔ °F)":
        c = st.number_input("Temperature (°C)", 0.0)
        st.write(f"{c}°C = {(c*9/5)+32:.2f}°F")
    elif conv_type == "Speed (km/h ↔ mph)":
        kmh = st.number_input("Speed (km/h)", 0.0)
        st.write(f"{kmh} km/h = {kmh*0.621371:.2f} mph")

# ----------------------------
# ELECTRICAL ASSISTANT
# ----------------------------
elif menu == "🔌 Electrical Assistant":
    st.header("🔌 Electrical Circuit Assistant")
    option = st.selectbox("Choose Calculation:", ["Ohm's Law (V = I * R)", "Power (P = V * I)", "Series Resistance", "Parallel Resistance"])
    if option == "Ohm's Law (V = I * R)":
        I = st.number_input("Current (A)", 0.0)
        R = st.number_input("Resistance (Ω)", 0.0)
        st.write(f"Voltage = {I*R:.2f} V")
    elif option == "Power (P = V * I)":
        V = st.number_input("Voltage (V)", 0.0)
        I = st.number_input("Current (A)", 0.0)
        st.write(f"Power = {V*I:.2f} W")
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

# ----------------------------
# CPE CHATBOT
# ----------------------------
elif menu == "💬 CPE Chatbot":
    st.header("💬 CPE Chatbot (KITE-AI)")

    OPENROUTER_API_KEY = "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"
    OPENROUTER_MODEL = "tngtech/deepseek-r1t2-chimera:free"
    OPENROUTER_HEADERS = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}

    # Professor info
    teachers_info = {
        # 2101
        "prof jennifer l. marasigan": {"name":"Prof. Jennifer L. Marasigan","subject":"CpE 403 - Computer Engineering as a Discipline","office":"CICS 2nd Flr"},
        "prof christia a. manalo": {"name":"Prof. Christia A. Manalo","subject":"ENGG 403 - Computer-Aided Design","office":"AEB 4th Flr"},
        "prof maria carmela m. carandang": {"name":"Prof. Maria Carmela M. Carandang","subject":"PATHFit 3 - Traditional and Recreational Games","office":"FDC 103"},
        "prof giovanni c. sarcilla": {"name":"Prof. Giovanni C. Sarcilla","subject":"ENGG 404 - Engineering Economics","office":"AEB 2nd Flr"},
        "prof monique a. coliat": {"name":"Prof. Monique A. Coliat","subject":"EE 423 - Fundamentals of Electrical Engineering","office":"AEB 4th Flr"},
        "prof joyce ann g. acob": {"name":"Prof. Joyce Ann G. Acob","subject":"CpE 404 - Programming Logic and Design","office":"CICS 2nd Flr"},
        "prof mercedita d. ocampo": {"name":"Prof. Mercedita D. Ocampo","subject":"CpE 405 - Discrete Mathematics","office":"CICS 2nd Flr"},
        "prof jhon kenneth a. de los reyes": {"name":"Prof. Jhon Kenneth A. De Los Reyes","subject":"MATH 403 - Engineering Data Analysis","office":"AEB 4th Flr"},
        "prof charley b. leuterio": {"name":"Prof. Charley B. Leuterio","subject":"MATH 404 - Differential Equations","office":"AEB 4th Flr"},
        # 2105
        "prof malvin roix orense": {"name":"Prof. Malvin Roix Orense","subject":"ENGG 404 - Engineering Economics","office":"TBA"},
        "prof anthony hernandez": {"name":"Prof. Anthony Hernandez","subject":"CpE 404 - Programming Logic and Design","office":"TBA"},
        "prof kristine bejasa": {"name":"Prof. Kristine Bejasa","subject":"EE 423 - Fundamentals of Electrical Engineering","office":"TBA"},
        "prof laila hernandez": {"name":"Prof. Laila Hernandez","subject":"CpE 403 - Computer Engineering as a Discipline","office":"TBA"},
        "prof ericka vabes ruolda": {"name":"Prof. Ericka Vabes Ruolda","subject":"ENGG 403 - Computer-Aided Design","office":"TBA"},
        "prof ryan banua": {"name":"Prof. Ryan Banua","subject":"MATH 403 - Engineering Data Analysis","office":"TBA"}
    }

    # session states
    if "chat_history" not in st.session_state: st.session_state.chat_history = []
    if "api_cache" not in st.session_state: st.session_state.api_cache = {}
    if "last_request_time" not in st.session_state: st.session_state.last_request_time = 0.0
    if "pending_reply" not in st.session_state: st.session_state.pending_reply = None

    # helpers
    def check_professor_query(user_input):
        lower = user_input.lower()
        for key, info in teachers_info.items():
            if key in lower or info["name"].lower() in lower:
                return f"👨‍🏫 **{info['name']}**\n**Subject:** {info['subject']}\n**Office:** {info['office']}"
        matches = get_close_matches(lower, list(teachers_info.keys()), n=1, cutoff=0.6)
        if matches:
            info = teachers_info[matches[0]]
            return f"👨‍🏫 **{info['name']}**\n**Subject:** {info['subject']}\n**Office:** {info['office']}"
        return None

   
