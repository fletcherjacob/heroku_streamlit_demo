import streamlit as st
import os

# Configs
st.set_page_config(page_title="Test Simulation ", layout="wide")

# Main dashboard content
st.title("Test Dashboard - An Interactive Dashboard")


# PWD
def check_password():

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        try:
            submit_pwd = os.getenv(st.session_state["username"])
            st.write(submit_pwd)
            # if submit_pwd == st.session_state["password"]:
            #     st.session_state["password_correct"] = True
            # else:
            #     st.session_state["password_correct"] = False
        except KeyError as e:
            print(e)

            # KeyError occurs when session_state["username"] or session_state["password"] is not found
            st.session_state["password_correct"] = False

        if "password" in st.session_state:
            del st.session_state["password"]
        if "username" in st.session_state:
            del st.session_state["username"]

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()


x = st.number_input("Insert a number", min_value=0, max_value=100, format="%i", step=1)
y = st.number_input("Exponent", min_value=0, max_value=100, format="%i", step=1)
z = x**y

st.write("The new value is", z)
