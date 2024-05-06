import streamlit as st 
st.title("Biodiversity Insights Dashboard")
st.subheader("Exploring the key insights found from our group project")
st.subheader("navigation ")
import pandas as pd
df = pd.read_excel("c:/Users/aliya/OneDrive/Desktop/Data Science Project Lifecycle Coursework/individual courseowrk/4Lenses.xlsx")
st.write(df)
