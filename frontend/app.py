import streamlit as st
import requests

API_URL = "https://msio-backend.onrender.com"

st.set_page_config(page_title="MSIO Dashboard", layout="centered")

if "token" not in st.session_state:
    st.session_state["token"] = None

def login():
    st.title("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Lozinka", type="password")
    if st.button("Login"):
        res = requests.post(f"{API_URL}/login", json={"email": email, "password": password})
        if res.status_code == 200:
            st.session_state["token"] = res.json()["access_token"]
            st.success("Uspešan login ✅")
            st.experimental_rerun()
        else:
            st.error("Pogrešan email ili lozinka.")

def register():
    st.title("📝 Registracija")
    username = st.text_input("Korisničko ime")
    email = st.text_input("Email")
    password = st.text_input("Lozinka", type="password")
    if st.button("Registruj se"):
        res = requests.post(f"{API_URL}/register", json={
            "username": username, "email": email, "password": password
        })
        if res.status_code == 200:
            st.success("Uspešna registracija! Prijavi se sada.")
        else:
            st.error("Email već postoji!")

def signal_feed():
    st.title("📈 MSIO Signal Feed")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔄 Refresh"):
            st.experimental_rerun()
    with col2:
        if st.button("🚪 Logout"):
            st.session_state["token"] = None
            st.experimental_rerun()

    headers = {"Authorization": f"Bearer {st.session_state['token']}"}
    res = requests.get(f"{API_URL}/signals/my", headers=headers)
    if res.status_code == 200:
        for sig in res.json()["signals"]:
            st.info(f"{sig['symbol']} → {sig['direction'].upper()} ({round(sig['confidence']*100)}%)")
    else:
        st.error("Greška pri preuzimanju signala.")

# === RENDER LOGIKA ===
if st.session_state["token"]:
    signal_feed()
else:
    option = st.radio("Odaberi:", ["Login", "Registracija"])
    login() if option == "Login" else register()
