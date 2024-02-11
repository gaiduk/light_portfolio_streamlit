import streamlit as st
import pandas


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

st.write("Below you can see some of the applications I've created in Python. Feel free to contact me")

col3, empty_col, col4 = st.columns([1.6, 0.4, 1.6])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if (index + 1) % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write("[Source Code](https://github.com/gaiduk/light_portfolio_streamlit)")

with col4:
    for index, row in df.iterrows():
        if (index + 1) % 2 != 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write("[Source Code](https://github.com/gaiduk/light_portfolio_streamlit)")

