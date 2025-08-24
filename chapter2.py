import streamlit as st

st.title("Simple App")

if st.button("Click me"):
    st.success("Button clicked!")

add_something = st.checkbox("Add something")

if add_something:
    st.write("You added something!")

add_type = st.radio("Choose a type:", ['Type A', 'Type B', 'Type C'])

if add_type:
    st.write(f"You selected {add_type}")

slider = st.slider("Select a value:", 0, 100, 25)
st.write(f"You selected {slider}")

num_input = st.number_input("Enter a number:", 0, 100, 10)
st.write(f"You entered {num_input}")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}!")


dob = st.date_input("Select your date of birth:")
st.write(f"You selected {dob}")

