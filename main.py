import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=400)

with col2:
    st.title("Haiduk Petro")
    content = """
    I'm a python developer.
    I have successful experience in developing desktop and web applications as well as creating games.

    More than 10 years successfully taught children programming in Python and javascript languages
    """

    st.info(content)