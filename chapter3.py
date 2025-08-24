import streamlit as st

st.title("Hello, Streamlit!")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    st.write("This is the first column.")
    button1 = st.button("Click me!")

with col2:
    st.header("Column 2")
    st.video("https://www.youtube.com/watch?v=JwSS70SZdyM", width=200)
    st.write("This is the second column.")
    button2 = st.button("No, click me!")

if button1:
    st.success("Button 1 clicked!")
if button2:
    st.success("Button 2 clicked!")


hihi = st.sidebar.text_input("Enter something:")
haha = st.sidebar.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.text(f'You entered: {hihi}, and you choose: {haha}')

with st.expander("More Info"):
    st.write("""
        1. This is the first item.
        2. This is the second item.
        3. This is the third item.
            """)