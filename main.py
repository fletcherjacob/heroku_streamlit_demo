import streamlit as st
import os

def check_password():
    """Verify user login credentials."""
    def login_form():
        """Display login form."""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in")

    def password_entered(form):
        """Check if password entered by user is correct."""
        username = form["username"]
        password = form["password"]
        submit_pwd = os.getenv(username)

        if submit_pwd == password:
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False
            st.error("😕 User not known or password incorrect")

    # Show login form
    login_form()

    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        return False
    else:
        return True

# Authenticate user
if not check_password():
    st.stop()

# Configure Streamlit page
st.set_page_config(page_title="Test Simulation", layout="wide")

# Main dashboard content
st.title("Test Dashboard - An Interactive Dashboard")

x = st.number_input("Insert a number", min_value=0, max_value=100, format="%i", step=1)
y = st.number_input("Exponent", min_value=0, max_value=100, format="%i", step=1)
z = x ** y

st.write("The new value is", z)
