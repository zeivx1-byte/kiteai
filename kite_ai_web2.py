# kite_ai_web2.py
# Streamlit Web Version of KITE-AI (Integrated for CPE 2nd Year)
# Includes Physics, Circuits, AI Toolkit, Task Manager, and CPE Chatbot
echo "# kiteai" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/zeivx1-byte/kiteai.git
git push -u origin main

import streamlit as st
import numpy as np
import os

# --- Modern Sophisticated UI Theme ---
st.set_page_config(page_title="KITE-AI Web 2.0", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
        /* Main App Background */
        [data-testid="stAppViewContainer"] {
            background: radial-gradient(circle at top left, #0a0a0f 0%, #101520 60%, #0b0c10 100%);
            color: white !important;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: rgba(25, 25, 35, 0.7);
            backdrop-filter: blur(15px);
            border-right: 1px solid rgba(0, 194, 255, 0.2);
        }

        /* Headings */
        h1, h2, h3, h4 {
            color: #00E0FF !important;
            text-shadow: 0 0 20px rgba(0, 224, 255, 0.3);
        }

        /* Cards & Inputs */
        .stMarkdown, .stTextInput, .stNumberInput, .stSelectbox, .stTextArea {
            background-color: rgba(255,255,255,0.05);
            border-radius: 10px;
            padding: 10px;
        }

        /* Buttons */
        button[kind="primary"] {
            background: linear-gradient(135deg, #00C2FF, #0066FF);
            color: white !important;
            border-radius: 12px;
            border: none;
            box-shadow: 0 0 15px rgba(0,194,255,0.3);
            transition: all 0.2s ease-in-out;
        }
        button[kind="primary"]:hover {
            transform: scale(1.05);
            box-shadow: 0 0 25px rgba(0,194,255,0.6);
        }

        /* Sidebar Text */
        [data-testid="stSidebarNav"]::before {
            content: "🧠 KITE-AI SYSTEM";
            margin-left: 15px;
            margin-top: 10px;
            font-size: 20px;
            font-weight: 600;
            color: #00E0FF;
            text-shadow: 0 0 20px rgba(0,224,255,0.4);
        }

        /* Chat Bubbles */
        .user-bubble {
            background-color: #00C2FF;
            color: black;
            padding: 10px 15px;
            border-radius: 18px 18px 0 18px;
            margin: 5px;
            max-width: 70%;
            align-self: flex-end;
        }
        .bot-bubble {
            background-color: #1f2a40;
            color: #e0e0e0;
            padding: 10px 15px;
            border-radius: 18px 18px 18px 0;
            margin: 5px;
            max-width: 70%;
            align-self: flex-start;
        }

        /* Footer */
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div style='text-align:center;'>
    <h1 style='font-size:45px; color:#00E0FF;'>KITE-AI Web 2.0</h1>
    <h3 style='color:#BBBBBB;'>Computer Engineering Smart Assistant</h3>
    <p style='color:gray;'>A fusion of Engineering Calculators, AI Simulations, and Student Utilities</p>
    <hr style='border: 1px solid rgba(0,224,255,0.3); width:80%; margin:auto;'>
</div>
""", unsafe_allow_html=True)

# --- Sidebar Menu ---
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🗂️ Task Manager", "⚙️ Physics Calculator", "📏 Unit Converter",
     "🔌 Electrical Assistant", "🧠 AI Toolkit", "💬 CPE Chatbot", "📘 About"]
)

# -------------------- HOME --------------------
if menu == "🏠 Home":
    st.header("🏠 Welcome to KITE-AI Web 2.0")
    st.markdown("""
    Explore AI-integrated Engineering Tools:
    - ⚙️ Physics Calculator  
    - 📏 Unit Converter  
    - 🔌 Electrical Circuit Assistant  
    - 🧠 AI Toolkit  
    - 🗂️ Task Manager  
    """)

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

# -------------------- AI TOOLKIT --------------------
elif menu == "🧠 AI Toolkit":
    st.header("🧠 AI Toolkit")
    tool = st.selectbox("Choose AI Module:", [
        "Logic Gates",
        "Number Converter",
        "Matrix Operations",
        "Perceptron Demo"
    ])

    # Logic Gates
    if tool == "Logic Gates":
        st.subheader("Logic Gate Simulator")
        a = st.selectbox("Input A", [0, 1])
        b = st.selectbox("Input B", [0, 1])
        gate = st.selectbox("Gate", ["AND", "OR", "XOR", "NOT"])
        if gate == "AND":
            st.success(f"Output: {a & b}")
        elif gate == "OR":
            st.success(f"Output: {a | b}")
        elif gate == "XOR":
            st.success(f"Output: {a ^ b}")
        elif gate == "NOT":
            st.success(f"Output: {int(not a)}")

    # Number Converter
    elif tool == "Number Converter":
        num = st.text_input("Enter number:")
        base = st.selectbox("Base", [2, 8, 10, 16])
        if num:
            try:
                dec = int(num, base)
                st.write(f"Decimal: {dec}")
                st.write(f"Binary: {bin(dec)[2:]}")
                st.write(f"Octal: {oct(dec)[2:]}")
                st.write(f"Hex: {hex(dec)[2:].upper()}")
            except:
                st.error("Invalid number.")

    # Matrix Operations
    elif tool == "Matrix Operations":
        st.subheader("Matrix Addition")
        A = st.text_area("Matrix A (e.g., 1 2, 3 4)")
        B = st.text_area("Matrix B (e.g., 5 6, 7 8)")
        if st.button("Add Matrices"):
            try:
                A_mat = np.array([list(map(float, row.split())) for row in A.split(",")])
                B_mat = np.array([list(map(float, row.split())) for row in B.split(",")])
                if A_mat.shape == B_mat.shape:
                    st.success(f"Result:\n{A_mat + B_mat}")
                else:
                    st.error("Matrix sizes must match.")
            except:
                st.error("Invalid matrix input.")

    # Perceptron Demo
    elif tool == "Perceptron Demo":
        st.subheader("Perceptron Demo (AND Gate)")
        X = np.array([[0,0],[0,1],[1,0],[1,1]])
        Y = np.array([0,0,0,1])
        lr = st.slider("Learning Rate", 0.01, 1.0, 0.1)
        epochs = st.slider("Epochs", 1, 50, 10)
        if st.button("Train"):
            w = np.zeros(2)
            b = 0
            for _ in range(epochs):
                for xi, target in zip(X, Y):
                    y_pred = 1 if np.dot(w, xi) + b >= 0 else 0
                    w += lr * (target - y_pred) * xi
                    b += lr * (target - y_pred)
            st.success(f"Weights: {w}, Bias: {b:.3f}")

# -------------------- CPE CHATBOT --------------------
elif menu == "💬 CPE Chatbot":
    st.header("💬 CPE Student ChatBot")
    st.markdown("Ask me anything about Computer Engineering 2nd Year!")

    user_input = st.text_input("You:", placeholder="e.g., Where is Engr. Cruz's office?")
    responses = {
        "teacher": "Most CPE professors can be found in the College of Engineering Faculty Room, 2nd floor.",
        "engr cruz": "Engr. Cruz usually handles Digital Systems and can be found in Room 204.",
        "engr de los reyes": "Engr. De los Reyes often teaches on the 4th floor CEAF Building — check the Circuit Lab.",
        "class schedule": "CPE 2nd year usually has major subjects from 8:00 AM to 5:00 PM.",
        "project": "Major projects are often submitted through Google Classroom or the department office.",
        "subject": "CPE 2nd year subjects include Logic Circuits, Data Structures, Computer Organization, and AI Fundamentals.",
        "adviser": "Your class adviser can be contacted through the CPE Faculty Messenger Group or during office hours.",
        "office": "The CPE Department Office is located near the Dean’s Office, College of Engineering Building.",
        "requirement": "Requirements include attendance, lab projects, quizzes, and final exams for each subject.",
        "exam": "Midterms usually happen around Week 8; Finals on Week 16."
    }

    if user_input:
        response = "I'm not sure yet, but you can ask your class representative for details."
        user_text = user_input.lower()

        for key, reply in responses.items():
            if key in user_text:
                response = reply
                break

        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(response)

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
