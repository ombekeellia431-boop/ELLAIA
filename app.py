import streamlit as st

# Configuration de la page
st.set_page_config(page_title="ELLI-IA : Studio de Création", layout="centered")

# Titre Principal
st.title("🎵 ELLI-IA : Studio de Création")

# --- SECTION 1 : PERSONNALISATION & CLONAGE ---
st.header("👤 Personnalisation & Clonage Vocal")

col1, col2 = st.columns(2)

with col1:
    emotion = st.select_slider(
        "Émotion :",
        options=["Triste 😢", "Neutre 😐", "Joyeux 😊", "Énervé 😠"],
        value="Neutre 😐"
    )

with col2:
    puissance = st.slider("Puissance (%)", 0, 100, 50)

timbre = st.selectbox("Timbre de voix :", ["Voix Studio", "Voix Naturelle", "Voix Radio"])

# Zone pour l'enregistrement direct
st.write("### 🎤 Enregistrer votre voix")
audio_value = st.audio_input("Enregistrez un échantillon pour le clonage")

if st.button("🚀 Lancer le clonage de ma voix", type="primary"):
    if audio_value:
        st.success("Analyse de l'échantillon en cours...")
    else:
        st.warning("Veuillez d'abord enregistrer ou charger un fichier audio.")

st.markdown("---")

# --- SECTION 2 : GÉNÉRATION DE PAROLES ---
st.header("📝 Génération de Paroles")

# Zone de texte libre (C'est ici la place pour mettre tes paroles !)
paroles_utilisateurs = st.text_area(
    "Écrivez vos paroles ici :", 
    placeholder="Ex: Dans la nuit étoilée, je cherche la mélodie...",
    height=150
)

col_buttons = st.columns(2)

with col_buttons[0]:
    if st.button("🪄 Générer par l'IA"):
        # Ici on simule une génération
        st.info("L'IA suggère : 'Sous le ciel de velours, les ombres s'effacent.'")

with col_buttons[1]:
    if st.button("💾 Valider mes paroles"):
        if paroles_utilisateurs:
            st.success("Paroles enregistrées avec succès !")
        else:
            st.error("La zone de texte est vide.")

# Affichage final
if paroles_utilisateurs:
    st.subheader("Aperçu du projet :")
    st.info(f"**Paroles retenues :** {paroles_utilisateurs}")
