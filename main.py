import os
import streamlit as st

st.title("Streamlit Password Testing")
def check_password():
    def login_form():
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        if st.session_state["password"] == os.getenv(st.session_state["username"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
            del st.session_state["username"] # Don't store the password.
        else:
            st.session_state["password_correct"] = False


    if st.session_state.get("password_correct", False):
        return True


    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.



x = st.number_input("Insert a number", min_value=0, max_value=100, format="%i", step=1)
y = st.number_input("Exponent", min_value=0, max_value=100, format="%i", step=1)
z = x**y

st.write("The new value is", z)
