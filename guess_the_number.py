import random
import streamlit as st

st.set_page_config(page_title="Guess the Number", page_icon="🎯")

if 'x' not in st.session_state:
    st.session_state.x = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.win = False

st.title("Guess the Number")
st.write("I'm thinking of a number between 1 and 100. Try to guess it!")

guess = st.number_input("Your guess", min_value=1, max_value=100, value=1, step=1)

if st.button("Submit"):
    st.session_state.attempts += 1
    if guess == st.session_state.x:
        st.success(f"Congratulations! I love You {st.session_state.attempts} times.")
        st.session_state.win = True
    elif guess < st.session_state.x:
        st.warning("Too low! Try again.")
    else:
        st.warning("Too high! Try again.")

st.write(f"Attempts: {st.session_state.attempts}")

if st.session_state.win:
    if st.button("Play again"):
        st.session_state.x = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.win = False
        st.experimental_rerun()
