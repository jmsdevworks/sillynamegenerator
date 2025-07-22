import streamlit as st
import random

first_names = [
    "Wacky", "Fluffy", "Zippy", "Bumpy", "Giggly",
    "Sneaky", "Dizzy", "Sparky", "Snazzy", "Goofy"
]

last_names = [
    "Bananaface", "Picklesniff", "Wobblebottom", "Gigglepants",
    "McDoodle", "Fluffernugget", "Jellybean", "Snickerdoodle",
    "Noodleman", "Chickencheeks"
]

def generate_silly_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    return f"{first} {last}"

st.title("🦄 Silly Name Generator")
st.write("Click the button to get your silly name!")

if st.button("Generate Silly Name!"):
    name = generate_silly_name()
    st.success(f"Your silly name is: **{name}**")