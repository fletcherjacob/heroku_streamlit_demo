import streamlit as st
import os


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
            if submit_pwd == st.session_state["password"]:
                st.session_state["password_correct"] = True

            else:
                st.session_state["password_correct"] = False

        except:
            st.session_state["password_correct"] = False
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]

        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()


# Configs
st.set_page_config(page_title="Test Simulation ", layout="wide")

"""
# Test Dashboard
-An Interactive Dashboard
"""

x = st.number_input("Insert a number", min_value=0, max_value=100, format="%i", step=1)
y = st.number_input("Exponent", min_value=0, max_value=100, format="%i", step=1)
z = x**y


st.write("The new value is", z)


# Create a file uploader and read the uploaded file
