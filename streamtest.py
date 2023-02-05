import streamlit as st
import json
import requests

st.title('Basic calculator App')
option=st.selectbox('What operation do you want to perform ?',('Addition','Subtraction','Multiplication','Division'))

st.write("Select the number from the slider below...")
x=st.slider("X",0,1000,20)
y=st.slider("Y",0,1000,30)

inputs={
    "operation": option,
    "x":x,
    "y":y
}
if st.button('calculate'):
    res=requests.post(url="http://localhost:8000/calculate",data=json.dumps(inputs))
    st.subheader(f"response from api= {res.text}")