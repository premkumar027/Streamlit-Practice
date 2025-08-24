import streamlit as st

st.title("Hello, World!")

st.write("Welcome to your first Streamlit app!")

st.subheader("This is a subheader")

st.text("This is some plain text.")

st.markdown("This is **Markdown** text.")

hui = st.selectbox("Choose an option:", ['haha', 'hihi', 'hoho'])
st.write(f'You choose {hui}, Excellent choice!')
st.success(f'Your {hui} is nice!')