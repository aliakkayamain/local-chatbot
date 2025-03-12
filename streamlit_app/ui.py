import streamlit as st
import requests
import re

def show_ui():
    # CSS ile üst menü, footer vb. gizleme
    hide_streamlit_style = """
    <style>
      #MainMenu {visibility: hidden;}
      header {visibility: hidden;}
      footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Sohbet geçmişini saklamak
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Başlık ve temizleme butonunu yan yana yerleştirme
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title("ChatBot - App")
    with col2:
        st.write("")
        st.write("")
        if st.button("Sohbeti Temizle"):
            st.session_state.messages = []
            st.rerun()

    # Mevcut sohbet geçmişini gösteriyoruz
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Kullanıcı mesaj girişi
    user_input = st.chat_input("Mesajınızı yazın...")

    if user_input:
        # Kullanıcının mesajını ekle ve göster
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Asistanın düşündüğünü göster
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Düşünüyor...")
        
        # API çağrısı
        try:
            api_url = "http://localhost:5000/api/chat"
            response = requests.post(api_url, json={"message": user_input}, timeout=30)
            if response.status_code == 200:
                data = response.json()
                response_text = data.get("response", "API yanıtı boş.")
            else:
                response_text = f"API hatası: {response.status_code} - {response.text}"
        except requests.exceptions.RequestException as e:
            response_text = f"API isteği sırasında hata oluştu: {str(e)}"

        # <think> ... </think> bloklarını temizle
        response_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL)

        # Asistanın yanıtını göster
        message_placeholder.markdown(response_text)
        
        # Yanıtı sohbet geçmişine ekle
        st.session_state.messages.append({"role": "assistant", "content": response_text})