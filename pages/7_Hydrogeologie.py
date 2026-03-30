import streamlit as st
from utils.menu import show_menu

show_menu()

st.title("🪨  Hydrogéologie")

with st.form("form_hydrogeologie"):

    

    submitted = st.form_submit_button("Valider")


if submitted: 
    st.sucess("Configuration sauvegardée !")