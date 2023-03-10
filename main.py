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

x = st.number_input('Insert a number', min_value = 0, max_value =100,format= '%i',step =1)
y = st.number_input('Exponent', min_value = 0, max_value =100,format= '%i',step =1)
z = x**y


st.write("The new value is",z)





# Create a file uploader and read the uploaded file
