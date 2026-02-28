import streamlit as st
from st_audiorec import st_audiorec
import io

# 1. Configuration de la page
st.set_page_config(page_title="Studio Player Pro", layout="centered")

# 2. Injection du design CSS (Votre ancien style HTML adapté pour Python)
st.markdown("""
<style>
    :root { 
        --primary: #2ecc71; 
        --dark: #2c3e50; 
        --light: #ecf0f1; 
    }
    .main {
        background-color: var(--light);
    }
    .header-container {
        background-color: var(--dark);
        color: white;
        padding: 30px;
        text-align: center;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .header-container h1 {
        margin: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: var(--primary);
        color: white;
        border-radius: 8px;
        width: 100%;
    }
</style>

<div class="header-container">
    <h1>Studio Player Pro</h1>
    <p>Bienvenue dans votre application de traitement audio !</p>
</div>
""", unsafe_allow_html=True)

# 3. Interface d'enregistrement
st.write("### 🎙️ Enregistreur Vocal")
st.info("Cliquez sur 'Start Recording' pour commencer, puis 'Stop' pour générer le fichier.")

# Utilisation du composant spécifié dans votre requirements.txt
wav_audio_data = st_audiorec()

# 4. Gestion du résultat
if wav_audio_data is not None:
    st.success("✅ Enregistrement terminé avec succès !")
    
    # Lecteur audio
    st.audio(wav_audio_data, format='audio/wav')
    
    # Bouton de téléchargement
    st.download_button(
        label="📥 Télécharger l'audio",
        data=wav_audio_data,
        file_name="mon_enregistrement.wav",
        mime="audio/wav"
    )

# 5. Section d'aide
with st.expander("ℹ️ Aide et instructions"):
    st.write("""
    1. Autorisez l'accès au micro dans votre navigateur.
    2. Enregistrez votre séquence.
    3. Écoutez le résultat ou téléchargez-le directement.
    """)



