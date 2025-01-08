import streamlit as st



def decitobin(a):
    n = int(a)
    bin = ""
    while n > 0 :
        r = n % 2 
        bin = str(r) + bin 
        n = n // 2
    return bin

def bintodeci(a):
    n = int(a)
    decimal = 0
    power = 0
    while n > 0:
        d = n % 10
        decimal += d * (2 ** power)
        n = n // 10
        power += 1
    return decimal


st.page_link("main.py", label="Num_Converter app",icon="⚓")

st.header("Number Converter")

mode = st.selectbox(
        "Select the Conversion Mode:",
        ("Decimal to Binary", "Binary to Decimal"))

if mode == "Decimal to Binary":

        n=st.number_input("Enter your decimal number to convert:")
        if n < 0:
            st.warning("Please enter a positive number")

        butn =st.button("Convert")
        if butn:
            st.warning(f"Binary of {n} is {decitobin(n)}")

elif mode == "Binary to Decimal":
        n=st.number_input("Enter your binary number to convert:")
        if n < 0:
            st.warning("Please enter a positive number")
        butn =st.button("Convert")
        if butn:
            st.warning(f"Decimal of {n} is {bintodeci(n)}")
else:
    st.warning("Please select a mode")


st.caption("Made by Jeet Prosad Mandal❤️")







