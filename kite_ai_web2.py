# kite_ai_web2.py
# Streamlit Web Version of KITE-AI 2.0 (Integrated for CPE 2nd Year)

import streamlit as st
import numpy as np
import os
import json
import requests
import time
from difflib import get_close_matches

# --- PAGE CONFIG ---
st.set_page_config(page_title="KITE-AI Web 2.0", page_icon="🤖", layout="wide")

# --- GLOBAL THEME ---
st.markdown("""
<style>
/* --- APP BACKGROUND --- */
[data-testid="stAppViewContainer"]{
    background: radial-gradient(circle at top left, #0a0a0f 0%, #101520 60%, #0b0c10 100%);
    color: white !important;
    font-family: 'Segoe UI', sans-serif;
}

/* --- HEADER --- */
header[data-testid="stHeader"] {
    background: linear-gradient(90deg, #2b0000, #4a0000, #2b0000);
    color: #FF4C4C !important;
    box-shadow: 0 0 25px rgba(255,60,60,0.3);
    border-bottom: 1px solid rgba(255,80,80,0.4);
}

/* --- SIDEBAR --- */
[data-testid="stSidebar"]{
    background: rgba(30,0,0,0.85);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255,50,50,0.3);
}
[data-testid="stSidebar"] *{
    color: #FFD6D6 !important;
}

/* --- SIDEBAR TITLE --- */
[data-testid="stSidebarNav"]::before{
    content:"🔥 KITE-AI SYSTEM";
    margin-left: 15px;
    margin-top: 10px;
    font-size: 20px;
    font-weight: 700;
    color: #FF4C4C;
    text-shadow: 0 0 25px rgba(255,80,80,0.6);
}

/* --- BUTTONS --- */
button[kind="primary"]{
    background: linear-gradient(135deg, #B00000, #FF0000);
    color:white !important;
    border-radius: 12px;
    border:none;
    box-shadow: 0 0 15px rgba(255,60,60,0.3);
    transition: 0.2s;
}
button[kind="primary"]:hover{
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(255,80,80,0.6);
}
button{
    background-color: rgba(40,0,0,0.8) !important;
    color:#FF4C4C !important;
    border: 1px solid rgba(255,50,50,0.4);
    border-radius:10px;
    transition:0.3s;
}
button:hover{
    background-color: rgba(70,0,0,0.9) !important;
    box-shadow:0 0 20px rgba(255,60,60,0.4);
}

/* --- HEADINGS --- */
h1,h2,h3,h4{
    color:#FF4C4C !important;
    text-shadow:0 0 25px rgba(255,60,60,0.5);
}

/* --- FOOTER HIDDEN --- */
footer{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# --- HEADER ICON ---
icon_url = "https://raw.githubusercontent.com/zeivx1-byte/kiteai/main/568672685_718166897320759_4217860298229868715_n.jpg"
st.markdown(f"""
<div style="display:flex; justify-content:center; align-items:center; padding:5px 0;">
<img src="{icon_url}" style="width:70px;height:70px;border-radius:50%;box-shadow:0 0 15px rgba(255,60,60,0.5);border:2px solid rgba(255,255,255,0.3);">
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR MENU ---
menu = st.sidebar.radio("Navigation", [
    "🏠 Home", "🗂️ Task Manager", "⚙️ Physics Calculator",
    "📏 Unit Converter", "🔌 Electrical Assistant",
    "💬 CPE Chatbot", "📘 About"
])

# ================= HOME =================
if menu == "🏠 Home":
    bg_url = "https://raw.githubusercontent.com/zeivx1-byte/kiteai/main/BSU.jpg"
    st.markdown(f"""
    <style>
    .hero {{
        position: relative;
        background-image: url('{bg_url}');
        background-size: cover;
        background-position: center;
        height: 550px;
        border-radius:15px;
        text-align:center;
        color:white;
        display:flex;
        flex-direction:column;
        justify-content:center;
        box-shadow:0 0 30px rgba(255,60,60,0.4);
    }}
    .overlay {{
        position:absolute;
        top:0; left:0;
        width:100%; height:100%;
        background:rgba(0,0,0,0.5);
        border-radius:15px;
    }}
    .hero-content {{
        position:relative; z-index:1; padding:20px;
    }}
    .hero h1{{font-size:55px; font-weight:800; color:#FF4C4C; text-shadow:0 0 25px rgba(255,60,60,0.7);}}
    .hero h3{{font-size:22px; background:rgba(255,0,0,0.6); display:inline-block; padding:10px 25px; border-radius:10px; color:white; font-weight:600; box-shadow:0 0 20px rgba(255,60,60,0.4);}}
    .vision {{margin-top:60px; padding:30px; background:rgba(40,0,0,0.6); border-radius:15px; box-shadow:0 0 25px rgba(255,60,60,0.3); text-align:center;}}
    .vision h2 {{color:#FF4C4C; text-shadow:0 0 20px rgba(255,60,60,0.5); font-size:34px; margin-bottom:15px;}}
    .vision p {{color:#FFEAEA; font-size:18px; line-height:1.6; max-width:850px; margin:0 auto;}}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <div class="overlay"></div>
        <div class="hero-content">
            <h1>WELCOME TO THE KITE WEB COMPANION</h1>
            <h3>Empowering Computer Engineering Students with Essential Tools</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)

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

# ================= TASK MANAGER =================
elif menu == "🗂️ Task Manager":
    st.header("🗂️ Task Manager")
    task_file = "tasks.txt"

    def load_tasks():
        return open(task_file).read().splitlines() if os.path.exists(task_file) else []

    def save_tasks(tasks):
        with open(task_file,"w") as f:
            f.writelines([t+"\n" for t in tasks])

    tasks = load_tasks()
    new_task = st.text_input("Add new task:")
    if st.button("Add Task"):
        if new_task: tasks.append(new_task); save_tasks(tasks); st.success(f"Task added: {new_task}")
        else: st.warning("Enter a task first!")

    if tasks:
        st.subheader("Your Tasks:")
        for i,t in enumerate(tasks):
            col1,col2 = st.columns([5,1])
            with col1: st.write(f"{i+1}. {t}")
            with col2:
                if st.button("❌", key=f"del_{i}"):
                    tasks.pop(i); save_tasks(tasks); st.experimental_rerun()
    else: st.info("No tasks added yet.")

# ================= PHYSICS CALCULATOR =================
elif menu == "⚙️ Physics Calculator":
    st.header("⚙️ Physics Calculator")
    formula = st.selectbox("Choose a formula:", ["Force", "Work", "Power","Kinetic Energy","Potential Energy"])
    if formula=="Force": m=st.number_input("Mass (kg)"); a=st.number_input("Accel (m/s²)")
    if formula=="Work": F=st.number_input("Force (N)"); d=st.number_input("Distance (m)")
    if formula=="Power": W=st.number_input("Work (J)"); t=st.number_input("Time (s)")
    if formula=="Kinetic Energy": m2=st.number_input("Mass (kg)"); v=st.number_input("Velocity (m/s)")
    if formula=="Potential Energy": m3=st.number_input("Mass (kg)"); g=st.number_input("Gravity",9.81); h=st.number_input("Height (m)")

    if st.button("Compute"):
        if formula=="Force": st.success(f"Force = {m*a:.2f} N")
        if formula=="Work": st.success(f"Work = {F*d:.2f} J")
        if formula=="Power": st.success(f"Power = {W/t:.2f} W" if t!=0 else "Time cannot be zero")
        if formula=="Kinetic Energy": st.success(f"KE = {0.5*m2*v**2:.2f} J")
        if formula=="Potential Energy": st.success(f"PE = {m3*g*h:.2f} J")

# ================= UNIT CONVERTER =================
elif menu == "📏 Unit Converter":
    st.header("📏 Unit Converter")
    conv_type = st.selectbox("Conversion Type:", ["Length (m↔ft)","Mass (kg↔lb)","Temp (°C↔°F)","Speed (km/h↔mph)"])
    if conv_type=="Length (m↔ft)":
        m=st.number_input("Meters"); st.write(f"{m} m = {m*3.28084:.2f} ft")
    if conv_type=="Mass (kg↔lb)":
        kg=st.number_input("Kilograms"); st.write(f"{kg} kg = {kg*2.20462:.2f} lb")
    if conv_type=="Temp (°C↔°F)":
        c=st.number_input("°C"); st.write(f"{c}°C = {c*9/5+32:.2f}°F")
    if conv_type=="Speed (km/h↔mph)":
        kmh=st.number_input("Speed km/h"); st.write(f"{kmh} km/h = {kmh*0.621371:.2f} mph")

# ================= ELECTRICAL ASSISTANT =================
elif menu == "🔌 Electrical Assistant":
    st.header("🔌 Electrical Assistant")
    option=st.selectbox("Select:",["Ohm's Law","Power","Series Res","Parallel Res"])
    if option=="Ohm's Law": I=st.number_input("Current (A)"); R=st.number_input("Resistance (Ω)"); st.write(f"Voltage = {I*R:.2f} V")
    if option=="Power": V=st.number_input("Voltage (V)"); I=st.number_input("Current (A)"); st.write(f"Power = {V*I:.2f} W")
    if option=="Series Res": r=st.text_input("Resistances (comma)"); 
        if r: st.write(f"Total = {sum([float(x) for x in r.split(',')]):.2f} Ω")
    if option=="Parallel Res": r=st.text_input("Resistances (comma)")
        if r: vals=[float(x) for x in r.split(',')]; total=1/sum(1/v for v in vals); st.write(f"Total = {total:.2f} Ω")

# ================= CPE CHATBOT =================
elif menu=="💬 CPE Chatbot":
    st.header("💬 CPE Chatbot")
    st.markdown("Ask about your 2nd Year professors or topics!")

    # --- TEACHER DATABASE ---
    teachers_info={
        "prof jennifer l. marasigan":{"name":"Prof. Jennifer L. Marasigan","subject":"CpE 403","office":"CICS 2nd Flr"},
        "prof christia a. manalo":{"name":"Prof. Christia A. Manalo","subject":"ENGG 403","office":"AEB 4th Flr"},
        "prof maria carmela m. carandang":{"name":"Prof. Maria Carmela M. Carandang","subject":"PATHFit 3","office":"FDC 103"},
        "prof giovanni c. sarcilla":{"name":"Prof. Giovanni C. Sarcilla","subject":"ENGG 404","office":"AEB 2nd Flr"},
    }

    if "chat_history" not in st.session_state: st.session_state.chat_history=[]
    if "api_cache" not in st.session_state: st.session_state.api_cache={}

    user_input = st.text_input("You:")

    if user_input:
        response_text="🤔 Not sure. Ask class rep."
        closest=get_close_matches(user_input.lower(), teachers_info.keys(),n=1,cutoff=0.6)
        if closest: info=teachers_info[closest[0]]; response_text=f"**{info['name']}**\nSubject: {info['subject']}\nOffice: {info['office']}"
        st.session_state.chat_history.append({"role":"user","content":user_input})
        st.session_state.chat_history.append({"role":"assistant","content":response_text})

    for msg in st.session_state.chat_history:
        role="user" if msg["role"]=="user" else "assistant"
        color="#FF4C4C" if role=="user" else "#f5f5f5"
        text_color="white" if role=="user" else "#222"
        st.markdown(f'<div style="background:{color}; color:{text_color}; border-radius:12px; padding:12px; margin:5px; max-width:85%; text-align:{"right" if role=="user" else "left"};">{msg["content"]}</div>',unsafe_allow_html=True)

# ================= ABOUT =================
elif menu=="📘 About":
    st.header("📘 About KITE-AI Web 2.0")
    st.markdown("""
    <div style="background: rgba(40,0,0,0.6); padding:20px; border-radius:15px; box-shadow:0 0 25px rgba(255,60,60,0.3); color:#FFEAEA; font-size:16px; line-height:1.6;">
    <strong>Developed for:</strong> Computer Engineering 2nd Year<br>
    <strong>Purpose:</strong> Integration of Engineering calculators and AI Chatbot<br>
    <strong>Modules:</strong>
    <ul>
        <li>Task Manager</li>
        <li>Physics & Electrical Calculators</li>
        <li>Unit Converters</li>
        <li>AI Demos</li>
        <li>Student Chatbot</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
