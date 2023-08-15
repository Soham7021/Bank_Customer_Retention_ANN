import numpy as np
import streamlit as st
import pickle
from keras.models import load_model

loaded_model = load_model('my_model.h5')
df = pickle.load(open('df.pkl','rb'))

st.title("Bank Customer Retention")

Credit = st.number_input('Credit Score', value=0, step=1, format="%d")
Gender = st.selectbox('Sex',['Male','Female'])
Age = st.number_input('Age', value=0, step=1, format="%d")
Tenure = st.number_input('Tenure', value=0, step=1, format="%d")
Balance = st.number_input('Balance', value=0, step=1, format="%d")
No_Of_Prod = st.selectbox('No_Of_Prod',df['NumOfProducts'].unique())
Credit_Card = st.selectbox('Credit_Card',['Have','Not Have'])
is_active_member = st.selectbox('IsActiveMember',['Yes','No'])
Salary = st.number_input('Salary', value=0, step=1, format="%d")

if st.button('Model Analysis'):
    if Credit_Card == 'Have':
        Credit_Card = 1
    else:
        Credit_Card = 0

    if is_active_member == 'Yes':
        is_active_member = 1
    else:
        is_active_member = 0

    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0

    query = np.array([Credit,Gender,Age,Tenure,Balance,No_Of_Prod,Credit_Card,is_active_member,Salary])
    query = query.reshape(1,9)

    result = loaded_model.predict(query)[0]
    if result==1:
        st.title("The predicted ans by model : May not Leave")
    else:
        st.title("The predicted ans by model : Will leave")

