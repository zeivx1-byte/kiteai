# kite_ai_web3.py
# Fully upgraded KITE-AI Web Companion v3.0
# Streamlit App for CPE 2nd Year Students

import streamlit as st
import os
import json
import time
import requests
from difflib import get_close_matches

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="KITE-AI Web Companion", page_icon="🤖", layout="wide")

# ----------------------------
# HARD-CODED OPENROUTER CONFIG
# ----------------------------
OPENROUTER_API_KEY = "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"
OPENROUTER_MODEL = "tngtech/deepseek-r1t2-chimera:free"
OPENROUTER_HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# ----------------------------
# TEACHER DATABASE (lookup lowercase)
# ----------------------------
teachers_info = {
    # 2101
    "prof jennifer l. marasigan": {"name": "Prof. Jennifer L. Marasigan", "subject": "CpE 403 - Computer Engineering as a Discipline", "office": "CICS 2nd Flr"},
    "prof christia a. manalo": {"name": "Prof. Christia A. Manalo", "subject": "ENGG 403 - Computer-Aided Design", "office": "AEB 4th Flr"},
    "prof maria carmela m. carandang": {"name": "Prof. Maria Carmela M. Carandang", "subject": "PATHFit 3 - Traditional and Recreational Games", "office": "FDC 103"},
    "prof giovanni c. sarcilla": {"name": "Prof. Giovanni C. Sarcilla", "subject": "ENGG 404 - Engineering Economics", "office": "AEB 2nd Flr"},
    "prof monique a. coliat": {"name": "Prof. Monique A. Coliat", "subject": "EE 423 - Fundamentals of Electrical Engineering", "office": "AEB 4th Flr"},
    "prof joyce ann g. acob": {"name": "Prof. Joyce Ann G. Acob", "subject": "CpE 404 - Programming Logic and Design", "office": "CICS 2nd Flr"},
    "prof mercedita d. ocampo": {"name": "Prof. Mercedita D. Ocampo", "subject": "CpE 405 - Discrete Mathematics", "office": "CICS 2nd Flr"},
    "prof jhon kenneth a. de los reyes": {"name": "Prof. Jhon Kenneth A. De Los Reyes", "subject": "MATH 403 - Engineering Data Analysis", "office": "AEB 4th Flr"},
    "prof charley b. leuterio": {"name": "Prof. Charley B. Leuterio", "subject": "MATH 404 - Differential Equations", "office": "AEB 4th Flr"},
    # 2105
    "prof malvin roix orense": {"name": "Prof. Malvin Roix Orense", "subject": "ENGG 404 - Engineering Economics", "office": "TBA"},
    "prof anthony hernandez": {"name": "Prof. Anthony Hernandez", "subject": "CpE 404 - Programming Logic and Design", "office": "TBA"},
    "prof kristine bejasa": {"name": "Prof. Kristine Bejasa", "subject": "EE 423 - Fundamentals of Electrical Engineering", "office": "TBA"},
    "prof laila hernandez": {"name": "Prof. Laila Hernandez", "subject": "CpE 403 - Computer Engineering as a Discipline", "office": "TBA"},
    "prof ericka vabes ruolda": {"name": "Prof. Ericka Vabes Ruolda", "subject": "ENGG 403 - Computer-Aided Design", "office": "TBA"},
    "prof ryan banua": {"name": "Prof. Ryan Banua", "subject": "MATH 403 - Engineering Data Analysis", "office": "TBA"}
}

# ----------------------------
# SESSION STATE
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "api_cache" not in st.session_state:
    cache_file = "chat_cache.json"
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                st.session_state.api_cache = json.load(f)
        except:
            st.session_state.api_cache = {}
    else:
        st.session_state.api_cache = {}
if "last_request_time" not in st.session_state:
    st.session_state.last_request_time = 0.0
if "pending_reply" not in st.session_state:
    st.session_state.pending_reply = None

# ----------------------------
# STYLES
# ----------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background: radial-gradient(circle at top left, #0a0a0f 0%, #101520 60%, #0b0c10 100%); color: #FFEAEA; font-family: 'Segoe UI', sans-serif;}
header[data-testid="stHeader"] {background: linear-gradient(90deg,#2b0000,#4a0000,#2b0000); color: #FF4C4C;}
.stButton>button {border-radius: 10px; padding: 8px 14px;}
.chat-container {max-height: 500px; overflow-y:auto; padding:10px; border-radius:12px; background: rgba(255,255,255,0.03); border:1px solid rgba(255,60,60,0.08);}
.chat-box {padding:12px 18px; margin:8px 0; border-radius:14px; max-width:85%; font-size:16px; line-height:1.4; white-space:pre-wrap;}
.user-msg {background-color: #B00000; color:white; margin-left:auto; text-align:right;}
.bot-msg {background-color: #f5f5f5; color:#222; margin-right:auto; text-align:left;}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HELPERS
# ----------------------------
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

def save_cache():
    try:
        with open("chat_cache.json", "w", encoding="utf-8") as f:
            json.dump(st.session_state.api_cache, f, ensure_ascii=False, indent=2)
    except:
        pass

def call_openrouter(user_input):
    if user_input in st.session_state.api_cache:
        return st.session_state.api_cache[user_input], "cache"
    now = time.time()
    if now - st.session_state.last_request_time < 2.5:
        return "⚠️ Too many requests locally — wait a few seconds.", "local-rate"
    body = {"model": OPENROUTER_MODEL, "messages":[{"role":"system","content":"You are KITE-AI, a friendly AI for Computer Engineering students."},{"role":"user","content":user_input}]}
    try:
        resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=OPENROUTER_HEADERS, json=body, timeout=30)
        st.session_state.last_request_time = time.time()
        resp.raise_for_status()
        data = resp.json()
        reply = data.get("choices",[{}])[0].get("message",{}).get("content","")
        st.session_state.api_cache[user_input] = reply
        save_cache()
        return reply, "api"
    except requests.exceptions.HTTPError as e:
        code = e.response.status_code if e.response else None
        if code == 401: return "⚠️ Unauthorized (401). Check API key.", "error"
        if code == 429: return "⚠️ Rate limit (429). Try again later.", "error"
        return f"⚠️ HTTP error: {e}", "error"
    except Exception as e:
        return f"⚠️ Connection error: {e}", "error"

# ----------------------------
# SIDEBAR MENU
# ----------------------------
menu = st.sidebar.radio("Navigation", ["🏠 Home", "🗂️ Task Manager", "⚙️ Physics Calculator",
                                      "📏 Unit Converter", "🔌 Electrical Assistant", "💬 CPE Chatbot", "📘 About"])

# ----------------------------
# HOME
# ----------------------------
if menu=="🏠 Home":
    st.title("🤖 KITE-AI Web Companion")
    st.markdown("Empowering CPE students with essential tools and AI assistance.")

# ----------------------------
# TASK MANAGER
# ----------------------------
elif menu=="🗂️ Task Manager":
    st.header("🗂️ Task Manager")
    task_file = "tasks.txt"
    def load_tasks():
        if os.path.exists(task_file):
            with open(task_file,"r") as f: return [line.strip() for line in f.readlines()]
        return []
    def save_tasks(tasks):
        with open(task_file,"w") as f: [f.write(t+"\n") for t in tasks]
    tasks = load_tasks()
    new_task = st.text_input("Add new task:")
    if st.button("Add Task") and new_task:
        tasks.append(new_task); save_tasks(tasks); st.success(f"Task added: {new_task}")
    if tasks:
        for i,t in enumerate(tasks):
            col1,col2=st.columns([5,1])
            with col1: st.write(f"{i+1}. {t}")
            with col2:
                if st.button("❌",key=f"del_{i}"): tasks.pop(i); save_tasks(tasks); st.experimental_rerun()
    else: st.info("No tasks yet.")

# ----------------------------
# PHYSICS CALCULATOR
# ----------------------------
elif menu=="⚙️ Physics Calculator":
    st.header("⚙️ Physics Calculator")
    opt = st.selectbox("Choose a formula:", ["Force (F=m*a)", "Work (W=F*d)", "Power (P=W/t)", "KE (0.5*m*v²)", "PE (m*g*h)"])
    if opt=="Force (F=m*a)":
        m=st.number_input("Mass (kg)");a=st.number_input("Acceleration (m/s²)")
        if st.button("Compute Force"): st.success(f"F={m*a:.2f} N")
    elif opt=="Work (W=F*d)":
        F=st.number_input("Force (N)");d=st.number_input("Distance (m)")
        if st.button("Compute Work"): st.success(f"W={F*d:.2f} J")
    elif opt=="Power (P=W/t)":
        W=st.number_input("Work (J)");t=st.number_input("Time (s)")
        if st.button("Compute Power"): st.success(f"P={W/t:.2f} W" if t!=0 else "Time cannot be zero")
    elif opt=="KE (0.5*m*v²)":
        m=st.number_input("Mass (kg)");v=st.number_input("Velocity (m/s)")
        if st.button("Compute KE"): st.success(f"KE={0.5*m*v**2:.2f} J")
    elif opt=="PE (m*g*h)":
        m=st.number_input("Mass (kg)");g=st.number_input("Gravity",9.81);h=st.number_input("Height (m)")
        if st.button("Compute PE"): st.success(f"PE={m*g*h:.2f} J")

# ----------------------------
# UNIT CONVERTER
# ----------------------------
elif menu=="📏 Unit Converter":
    st.header("📏 Unit Converter")
    conv = st.selectbox("Conversion Type",["Length (m↔ft)","Mass (kg↔lb)","Temp (°C↔°F)","Speed (km/h↔mph)"])
    if conv=="Length (m↔ft)":
        m=st.number_input("Meters"); st.write(f"{m} m = {m*3.28084:.2f} ft")
    elif conv=="Mass (kg↔lb)":
        kg=st.number_input("Kilograms"); st.write(f"{kg} kg = {kg*2.20462:.2f} lb")
    elif conv=="Temp (°C↔°F)":
        c=st.number_input("Celsius"); st.write(f"{c}°C = {(c*9/5)+32:.2f}°F")
    elif conv=="Speed (km/h↔mph)":
        kmh=st.number_input("Speed km/h"); st.write(f"{kmh} km/h = {kmh*0.621371:.2f} mph")

# ----------------------------
# ELECTRICAL ASSISTANT
# ----------------------------
elif menu=="🔌 Electrical Assistant":
    st.header("🔌 Electrical Assistant")
    opt=st.selectbox("Choose:",["Ohm's Law","Power","Series Resistance","Parallel Resistance"])
    if opt=="Ohm's Law":
        I=st.number_input("Current (A)");R=st.number_input("Resistance (Ω)")
        st.write(f"Voltage = {I*R:.2f} V")
    elif opt=="Power":
        V=st.number_input("Voltage");I=st.number_input("Current"); st.write(f"P={V*I:.2f} W")
    elif opt=="Series Resistance":
        vals=st.text_input("Enter resistances comma-separated")
        if vals:
            try: vals=[float(x) for x in vals.split(",")]; st.success(f"Total={sum(vals):.2f} Ω")
            except: st.error("Invalid input")
    elif opt=="Parallel Resistance":
        vals=st.text_input("Enter resistances comma-separated")
        if vals:
            try: vals=[float(x) for x in vals.split(",")]; st.success(f"Total={1/sum(1/v for v in vals if v!=0):.2f} Ω")
            except: st.error("Invalid input")

# ----------------------------
# CPE CHATBOT
# ----------------------------
elif menu=="💬 CPE Chatbot":
    st.header("💬 CPE Chatbot")
    st.markdown("Ask about professors or general CPE topics. Offline professor info always works; AI requires OpenRouter key.")
    # Chat container
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        cls="user-msg" if msg["role"]=="user" else "bot-msg"
        st.markdown(f"<div class='chat-box {cls}'>{msg['text']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    # Input
    user_text=st.text_input("Type here", key="chat_input")
    col1,col2=st.columns([1,1])
    with col1: send=st.button("Send")
    with col2: clear=st.button("Clear chat")
    if clear: st.session_state.chat_history=[]; st.experimental_rerun()
    if send and user_text:
        st.session_state.chat_history.append({"role":"user","text":user_text})
        st.experimental_rerun()
    # generate reply
    if st.session_state.chat_history:
        last=st.session_state.chat_history[-1]
        if last["role"]=="user" and st.session_state.pending_reply!=last["text"]:
            st.session_state.pending_reply=last["text"]
            prof_ans=check_professor_query(last["text"])
            if prof_ans:
                st.session_state.chat_history.append({"role":"assistant","text":prof_ans})
                st.session_state.pending_reply=None; st.experimental_rerun()
            with st.spinner("🤖 KITE-AI is thinking..."):
                reply,_=call_openrouter(last["text"])
            st.session_state.chat_history.append({"role":"assistant","text":reply})
            st.session_state.pending_reply=None; st.experimental_rerun()

# ----------------------------
# ABOUT
# ----------------------------
elif menu=="📘 About":
    st.header("📘 About KITE-AI")
    st.markdown("""
    Developed for CPE 2nd Year Students.  
    Modules included:
    - Task Manager
    - Physics & Electrical Calculators
    - Unit Converters
    - AI Chatbot with professor lookup
    """)
