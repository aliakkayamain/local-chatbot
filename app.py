import streamlit as st
from streamlit_app.ui import show_ui

def main():
    st.set_page_config(page_title="DeepSeekR1", layout="centered")
    show_ui()

if __name__ == "__main__":
    main()