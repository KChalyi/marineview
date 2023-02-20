import streamlit as st
import pandas as pd
import openpyxl
st.title("Таблица куколдов")
name=st.text_input("Имя смотрящего",' ')
df2=pd.read_excel("./test.xlsx")
st.dataframe(df2)
st.write(f"Привет куколд {name}!")
x=st.slider("Select an integer x",0,10,1)
y=st.slider("Select an integer y",0,10,1)
df=pd.DataFrame({"x":[x],"y":[y],"x+y":[x+y]},index=["addition row"])
st.write(df)
