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

# kite_ai_web2_fixed.py
# KITE-AI Web 2.0 — Fixed full app (Option A: single hard-coded model)
# Hard-coded OpenRouter key (as requested)
# NOTE: Hard-coding API keys is insecure for public repos. Keep this file private.

import streamlit as st
import requests
import json
import time
import os
from difflib import get_close_matches

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="KITE-AI Web 2.0", page_icon="🤖", layout="wide")

# ----------------------------
# THEME / STYLES (dark red neon)
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
header[data-testid="stHeader"] { background: linear-gradient(90deg,#2b0000,#4a0000,#2b0000); color: #FF4C4C; }

/* chat bubbles */
.chat-box { padding: 12px 18px; margin: 8px 0; border-radius: 14px; max-width: 85%; font-size: 16px; line-height: 1.4; white-space: pre-wrap; }
.user-msg { background-color: #B00000; color: white; margin-left: auto; text-align: right; }
.bot-msg { background-color: #f5f5f5; color: #222; margin-right: auto; text-align: left; }

/* chat container */
.chat-container {
    max-height: 520px;
    overflow-y: auto;
    padding: 14px;
    border-radius: 12px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,60,60,0.08);
}

/* buttons */
.stButton>button { border-radius: 10px; padding: 8px 14px; }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HARD-CODED OPENROUTER KEY & MODEL (Option A)
# ----------------------------
OPENROUTER_API_KEY = "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"
OPENROUTER_MODEL = "tngtech/deepseek-r1t2-chimera:free"
OPENROUTER_HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

# ----------------------------
# APP LAYOUT
# ----------------------------
col1, col2 = st.columns([3, 1])

with col1:
    st.title("🤖 KITE-AI Web Companion")
    st.subheader("CPE Student Assistant — Chatbot (fixed model)")
    st.markdown("Ask about professors, engineering topics, or general questions. Professor info is available offline.")
with col2:
    st.markdown("**Model:**")
    st.info(OPENROUTER_MODEL)

# ----------------------------
# TEACHER DATABASE (lookup keys are lowercase)
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
# SESSION STATE: chat history, cache, rate-limits
# ----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of dicts: {"role": "user"/"assistant", "text": "..."}
if "api_cache" not in st.session_state:
    # load persistent cache from disk if available
    cache_file = "chat_cache.json"
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                st.session_state.api_cache = json.load(f)
        except Exception:
            st.session_state.api_cache = {}
    else:
        st.session_state.api_cache = {}
if "last_request_time" not in st.session_state:
    st.session_state.last_request_time = 0.0

# ----------------------------
# HELPERS
# ----------------------------
def check_professor_query(user_input):
    """Return professor info string if user asked about professor (fuzzy contains)."""
    # exact or fuzzy matching: check if any professor key present in sentence
    lower = user_input.lower()
    for key, info in teachers_info.items():
        if key in lower or info["name"].lower() in lower:
            return f"👨‍🏫 **{info['name']}**\n**Subject:** {info['subject']}\n**Office:** {info['office']}"
    # also try fuzzy partial matches using difflib
    matches = get_close_matches(lower, list(teachers_info.keys()), n=1, cutoff=0.6)
    if matches:
        info = teachers_info[matches[0]]
        return f"👨‍🏫 **{info['name']}**\n**Subject:** {info['subject']}\n**Office:** {info['office']}"
    return None

def save_cache():
    try:
        with open("chat_cache.json", "w", encoding="utf-8") as f:
            json.dump(st.session_state.api_cache, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def call_openrouter(user_input):
    """Call OpenRouter with the hard-coded key and fixed model.
       Handles rate-limit (simple throttling), errors, and caching."""
    # check cache first
    if user_input in st.session_state.api_cache:
        return st.session_state.api_cache[user_input], "cache"

    # rate-limit: allow one request every 2.5 seconds (adjust as needed)
    now = time.time()
    if now - st.session_state.last_request_time < 2.5:
        return "⚠️ Too many requests locally — please wait a few seconds.", "local-rate"

    body = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "You are KITE-AI, a friendly AI assistant for Computer Engineering students."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        resp = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=OPENROUTER_HEADERS, json=body, timeout=30)
        st.session_state.last_request_time = time.time()
        resp.raise_for_status()
        data = resp.json()
        # defensive access
        reply = None
        try:
            reply = data["choices"][0]["message"]["content"]
        except Exception:
            reply = json.dumps(data)
        # save to cache
        st.session_state.api_cache[user_input] = reply
        save_cache()
        return reply, "api"
    except requests.exceptions.HTTPError as e:
        code = None
        try:
            code = e.response.status_code
        except Exception:
            code = None
        if code == 401:
            return "⚠️ OpenRouter unauthorized (401). Check your API key or model access.", "error"
        if code == 429:
            return "⚠️ OpenRouter rate limit reached (429). Try again later.", "error"
        return f"⚠️ OpenRouter HTTP error: {e}", "error"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Connection error: {e}", "error"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}", "error"

# ----------------------------
# MAIN CHAT UI (single-column)
# ----------------------------
st.markdown("### 💬 Chat (KITE-AI)")
st.markdown("Ask about professors or general CPE topics. Professor info works offline; AI replies require the OpenRouter key.")

# chat container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
# display current session chat history
for msg in st.session_state.chat_history:
    role_class = "user-msg" if msg["role"] == "user" else "bot-msg"
    # escape HTML content but maintain newlines (Streamlit auto-escapes, using markdown with unsafe)
    st.markdown(f"<div class='chat-box {role_class}'>{msg['text']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# unique input widget keys to avoid duplicate IDs
user_text = st.text_input("Type your message here:", key="kite_chat_input")
col_a, col_b, col_c = st.columns([1,1,6])
with col_a:
    send = st.button("Send", key="kite_send_button")
with col_b:
    clear = st.button("Clear chat", key="kite_clear_button")
# small status column for manual actions
with col_c:
    st.write("")  # placeholder, keeps layout consistent

# handle clear chat
if clear:
    st.session_state.chat_history = []
    st.experimental_rerun()

# when user sends
if send and user_text:
    # append user message
    st.session_state.chat_history.append({"role": "user", "text": st.markdown(user_text) or user_text})
    # display immediately (optimistic)
    st.experimental_rerun()  # rerun to show the user message in container

# The code above does an immediate rerun after appending user message so the UI updates.
# The following block handles the actual response generation after rerun (when send button no longer fresh)
# We use a hidden flag in session_state to detect we need to create a reply.
if "pending_reply" not in st.session_state:
    st.session_state.pending_reply = None

# If last message is from user and not yet replied to, generate reply
if st.session_state.chat_history:
    last = st.session_state.chat_history[-1]
    if last["role"] == "user" and (st.session_state.pending_reply is None or st.session_state.pending_reply != last["text"]):
        st.session_state.pending_reply = last["text"]
        user_query = last["text"]

        # Try professor lookup first
        prof_answer = check_professor_query(user_query)
        if prof_answer:
            st.session_state.chat_history.append({"role": "assistant", "text": prof_answer})
            st.session_state.pending_reply = None
            st.experimental_rerun()

        # Not a professor query: call OpenRouter
        with st.spinner("🤖 KITE-AI is thinking..."):
            reply_text, source = call_openrouter(user_query)

        # Append reply
        st.session_state.chat_history.append({"role": "assistant", "text": reply_text})
        st.session_state.pending_reply = None
        st.experimental_rerun()

# ----------------------------
# FOOTER: show cache size & controls
# ----------------------------
st.markdown("---")
cache_info_col1, cache_info_col2 = st.columns([4,1])
with cache_info_col1:
    cached = len(st.session_state.api_cache)
    st.markdown(f"**Cache:** {cached} entries (saved to `chat_cache.json`)")
with cache_info_col2:
    if st.button("Clear cache", key="kite_clear_cache"):
        st.session_state.api_cache = {}
        save_cache()
        st.success("Cache cleared.")

# helpful debug (small, collapsible)
with st.expander("Debug (technical)"):
    st.write("Last request time:", st.session_state.last_request_time)
    st.write("Cache keys (showing up to 10):", list(st.session_state.api_cache.keys())[:10])
    st.write("Chat history length:", len(st.session_state.chat_history))
    st.write("OpenRouter model:", OPENROUTER_MODEL)




# -------------------- ABOUT --------------------
elif menu == "📘 About":
    st.header("📘 About KITE-AI Web 2.0")
    st.markdown("""
    <div style="
        background: rgba(40,0,0,0.6); 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 0 25px rgba(255,60,60,0.3);
        color: #FFEAEA;
        font-size: 16px;
        line-height: 1.6;
    ">
    <strong>Developed for:</strong> Computer Engineering 2nd Year<br>
    <strong>Purpose:</strong> To integrate Engineering problem-solving and basic AI simulations<br>
    <strong>Modules Included:</strong>
    <ul>
        <li>Task Manager</li>
        <li>Physics & Electrical Calculators</li>
        <li>Unit Converters</li>
        <li>AI Demos (Logic Gates, Perceptron)</li>
        <li>Student Chatbot</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)


































