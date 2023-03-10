import streamlit as st

# Configs
st.set_page_config(
    page_title="Test Simulation ",
    layout='wide'
)

'''
# Test Dashboard
-An Interactive Dashboard
'''

x = st.number_input('Insert a number', format= '%i')
y = st.number_input('Exponent',format= '%i')
z = x**y


st.write("The new value is",z)





# Create a file uploader and read the uploaded file
