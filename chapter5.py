import streamlit as st
import requests

st.title("Currency Converter from INR")
amount = st.number_input("Enter amount in INR: ", min_value=1)

target_currency = st.selectbox("Select target currency: ", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        rates = data['rates'][target_currency]
        converted_amount = amount * rates
        st.success(f"{amount} INR is equal to {converted_amount:.2f} {target_currency}")
    else:
        st.error("Error fetching exchange rates. Please try again later.")
