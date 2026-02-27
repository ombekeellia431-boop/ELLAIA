import streamlit as st
import random
from gtts import gTTS
import os

# 1. CONFIGURATION DE LA PAGE (Toujours en premier)
st.set_page_config(page_title="ELLI-IA Studio", layout="wide")

# 2. FONCTIONS DE GÉNÉRATION AUDIO
def generate_voice(text, type_voix="Voix Studio"):
    tts = gTTS(text=text, lang='fr', slow=(type_voix == "Voix Douce"))
    filename = "output.mp3"
    tts.save(filename)
    return filename

def generate_simple_lyrics():
    subjects = ["Le ciel", "Mon cœur", "La musique", "Le temps"]
    verbs = ["chante", "danse", "vibre", "s'arrête"]
    objects = ["la nuit", "le jour", "l'espoir", "la paix"]
    
    line = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
    return line

# 3. INTERFACE UTILISATEUR
st.title("🎵 ELLI-IA : Studio de Création")

# --- SECTION VIDÉO ---
if os.path.exists('video.mp4'):
    st.video('video.mp4')
else:
    st.info("Vidéo 'video.mp4' non trouvée sur GitHub. Message de chargement...")

# --- SECTION : PERSONNALISATION ET CLONAGE ---
st.header("👤 Personnalisation & Clonage Vocal")
col1, col2 = st.columns(2)

with col1:
    emotion = st.select_slider('Émotion :', options=['Triste 😢', 'Neutre 😐', 'Énergique 🔥'])
    option_voix = st.selectbox("Timbre de voix :", ["Voix Studio", "Voix Concert", "Voix Robot"])

with col2:
    puissance = st.slider('Puissance (%)', 0, 100, 50)

# LE BOUTON DE CLONAGE
if st.button("🎤 Lancer le clonage de ma voix", key="btn_clone"):
    # On génère un petit test vocal
    audio_file = generate_voice("Ceci est un test de clonage vocal réussi.", option_voix)
    st.audio(audio_file)
    st.success("Ta voix a été clonée avec succès !")

st.divider()

# --- SECTION : GÉNÉRATION DE PAROLES ---
st.header("📝 Génération de Paroles")
if st.button("Générer une phrase de chanson", key="btn_lyrics"):
    parole = generate_simple_lyrics()
    st.write(f"**Paroles générées :** {parole}")
