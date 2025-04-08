# app.py (User Guesses)

import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title="🎮 Guess the Number Game", page_icon="🔢")

# Add a colorful title
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: white;
        background-color: #FF5733;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    <div class="title">🎮 Guess the Number Game 🔢</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful header
st.markdown(
    """
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #33FF57;
        text-align: center;
    }
    </style>
    <div class="header">✨ Can You Guess the Secret Number? ✨</div>
    """,
    unsafe_allow_html=True
)

# Initialize the secret number in session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

# Initialize the number of attempts in session state
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Add instructions
st.markdown(
    """
    <style>
    .instructions {
        font-size: 20px;
        color: #33A8FF;
        text-align: center;
    }
    </style>
    <div class="instructions">🎯 I'm thinking of a number between 1 and 100. Can you guess it?</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful input box for the user's guess
guess = st.number_input(
    "🔢 Enter your guess (1-100):",
    min_value=1,
    max_value=100,
    value=50,
    step=1
)

# Add a button to submit the guess
if st.button("🚀 Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.secret_number:
        feedback_message = "⬆️ Too low! Try a higher number."
        st.markdown(
            """
            <style>
            .feedback {{
                font-size: 25px;
                font-weight: bold;
                color: #FF3333;
                text-align: center;
            }}
            </style>
            <div class="feedback">{}</div>
            """.format(feedback_message),
            unsafe_allow_html=True
        )
    elif guess > st.session_state.secret_number:
        feedback_message = "⬇️ Too high! Try a lower number."
        st.markdown(
            """
            <style>
            .feedback {{
                font-size: 25px;
                font-weight: bold;
                color: #FF3333;
                text-align: center;
            }}
            </style>
            <div class="feedback">{}</div>
            """.format(feedback_message),
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <style>
            .success {{
                font-size: 30px;
                font-weight: bold;
                color: #33FF57;
                text-align: center;
            }}
            </style>
            <div class="success">🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts. 🎉</div>
            """,
            unsafe_allow_html=True
        )
        # Reset the game
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0

# Display the number of attempts
st.markdown(
    f"""
    <style>
    .attempts {{
        font-size: 20px;
        color: #FFA500;
        text-align: center;
    }}
    </style>
    <div class="attempts">📊 Number of attempts: {st.session_state.attempts}</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 20px;
        color: #33C1FF;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    <div class="footer">🚀 Thanks for playing the Guess the Number Game! 🚀</div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h5 style="color: red; font-weight: bold; text-align: center; margin-top: 20px;">
        ✏️📚 Author: Azmat Ali 📚✏️
    </h5>
    """,
    unsafe_allow_html=True
)