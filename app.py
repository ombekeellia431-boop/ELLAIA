import streamlit as st
from st_audiorec import st_audiorec
import io


# Injection du CSS pour garder votre design
st.markdown("""
<style>
    :root { --primary: #2ecc71; --dark: #2c3e50; --light: #ecf0f1; }
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: var(--light); }
    .header { background: var(--dark); color: white; padding: 20px; text-align: center; border-radius: 10px; }
</style>
<div class="header">
    <h1>Studio Player Pro</h1>
</div>
""", unsafe_allow_html=True)

st.write("Bienvenue dans votre application de traitement audio !")

# Ajoutez ici le reste de votre logique Python (boutons, enregistrement, etc.)


