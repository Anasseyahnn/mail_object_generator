import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Configuration de la page
st.set_page_config(
    page_title="Email Subject Generator",
    page_icon="✉️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour une belle interface
def local_css():
    st.markdown("""
    <style>
        /* Couleurs principales */
        :root {
            --primary: #4F46E5;
            --primary-light: #6366F1;
            --secondary: #10B981;
            --background: #F9FAFB;
            --card: #FFFFFF;
            --text: #1F2937;
            --text-light: #6B7280;
            --border: #E5E7EB;
        }

        /* Style global */
        .stApp {
            background-color: var(--background);
            color: var(--text);
        }

        /* Titre principal */
        .main-title {
            font-family: 'Helvetica', sans-serif;
            font-weight: 700;
            font-size: 2.5rem;
            color: var(--primary);
            margin-bottom: 1rem;
            text-align: center;
        }

        /* Sous-titre */
        .subtitle {
            font-family: 'Helvetica', sans-serif;
            font-weight: 400;
            font-size: 1.2rem;
            color: var(--text-light);
            margin-bottom: 2rem;
            text-align: center;
        }

        /* Carte principale */
        .card {
            background-color: var(--card);
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            margin-bottom: 2rem;
            border: 1px solid var(--border);
        }

        /* Zone de texte */
        .stTextArea textarea {
            border-radius: 8px;
            border: 1px solid var(--border);
            min-height: 200px;
            font-size: 1rem;
            padding: 1rem;
        }

        /* Bouton */
        .stButton button {
            background-color: var(--primary);
            color: white;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.75rem 1.5rem;
            border: none;
            transition: all 0.2s ease;
            width: 100%;
        }

        .stButton button:hover {
            background-color: var(--primary-light);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(79, 70, 229, 0.2);
        }

        /* Résultat */
        .result-card {
            background-color: var(--card);
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid var(--border);
            margin-top: 2rem;
            text-align: center;
        }

        .result-title {
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text);
            margin-bottom: 0.5rem;
        }

        .result-content {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--secondary);
            padding: 1rem;
            border-radius: 8px;
            background-color: rgba(16, 185, 129, 0.1);
            border: 1px dashed var(--secondary);
        }

        /* Séparateur */
        hr {
            margin: 2rem 0;
            border: none;
            height: 1px;
            background-color: var(--border);
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 1rem;
            color: var(--text-light);
            font-size: 0.9rem;
            margin-top: 2rem;
        }

        /* Sidebar */
        .css-1d391kg {
            background-color: var(--card);
        }

        /* Responsive */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2rem;
            }

            .card {
                padding: 1.5rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Appliquer le CSS
local_css()

# Fonction pour vérifier et charger la clé API
def load_api_key():
    # Essayer de charger depuis .env
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')

    # Si la clé n'est pas trouvée dans .env, essayer de la récupérer depuis Streamlit secrets
    if not api_key:
        try:
            api_key = st.secrets['OPENAI_API_KEY']
        except:
            pass

    return api_key

# Initialiser les variables de session si elles n'existent pas
if 'api_key' not in st.session_state:
    st.session_state.api_key = load_api_key() or ""
    
if 'api_key_status' not in st.session_state:
    st.session_state.api_key_status = None
    
if 'history' not in st.session_state:
    st.session_state.history = []

# Création de l'invite système
system_prompt = """
Vous êtes un assistant spécialisé dans la rédaction de lignes d'objet pour des e-mails. 
Votre tâche consiste à analyser le contenu d'un e-mail et à suggérer une ligne d'objet courte, 
claire et pertinente. La ligne d'objet doit refléter le contenu principal de l'e-mail et 
inciter le destinataire à l'ouvrir.
"""

# Création de l'Invite utilisateur
def user_prompt_for(email_content):
    user_prompt = f"Voici le contenu de l'e-mail :\n\n{email_content}\n\n"
    user_prompt += "Veuillez suggérer une ligne d'objet courte et appropriée pour cet e-mail."
    return user_prompt

# Création d'une fonction pour préparer les messages pour OpenAI
def messages_for(email_content):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(email_content)}
    ]

# Utilisation de l'API OpenAI pour suggérer une ligne d'objet
def suggest_subject(email_content, api_key, model="gpt-4"):
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages_for(email_content)
        )
        return response.choices[0].message.content, None
    except Exception as e:
        return None, str(e)

# Sidebar pour les paramètres et informations
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>⚙️ Paramètres</h2>", unsafe_allow_html=True)

    # Section de configuration de l'API
    st.markdown("### Configuration de l'API")

    # Option pour entrer la clé API directement
    api_key_input = st.text_input(
        "Clé API OpenAI",
        type="password",
        help="Entrez votre clé API OpenAI (commence par 'sk-')",
        value=st.session_state.api_key
    )

    # Bouton pour vérifier/enregistrer la clé API
    if st.button("Vérifier la clé API"):
        if api_key_input:
            if api_key_input.startswith(("sk-", "sk-proj-")):
                st.session_state.api_key = api_key_input
                st.session_state.api_key_status = "valid"
                st.success("Clé API valide et enregistrée!")
            else:
                st.session_state.api_key_status = "invalid"
                st.error("Format de clé API invalide. Elle doit commencer par 'sk-' ou 'sk-proj-'")
        else:
            # Essayer de charger depuis .env ou secrets
            loaded_key = load_api_key()
            if loaded_key:
                st.session_state.api_key = loaded_key
                st.session_state.api_key_status = "valid"
                st.success("Clé API chargée avec succès depuis le fichier .env ou les secrets!")
            else:
                st.session_state.api_key_status = "missing"
                st.error("Aucune clé API trouvée. Veuillez en entrer une.")

    st.markdown("---")

    # Informations sur les modèles
    st.markdown("### Modèles disponibles")
    model_option = st.selectbox(
        "Choisissez un modèle",
        ["gpt-4", "gpt-3.5-turbo"],
        index=0,
        help="GPT-4 est plus puissant mais plus coûteux. GPT-3.5-Turbo est plus rapide et moins cher."
    )

    st.markdown("---")

    # Informations sur l'application
    st.markdown("### À propos")
    st.markdown("""
    Cette application vous aide à générer des lignes d'objet efficaces pour vos e-mails 
    en utilisant l'IA. Entrez simplement le contenu de votre e-mail, et l'application 
    vous suggérera une ligne d'objet pertinente.
    """)

    st.markdown("---")

    # Footer du sidebar
    st.markdown("""
    <div class="footer">
        Créé avec ❤️ et Streamlit
    </div>
    """, unsafe_allow_html=True)

# Contenu principal
st.markdown('<h1 class="main-title">✉️ Générateur de Lignes d\'Objet</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Créez des lignes d\'objet efficaces pour vos e-mails grâce à l\'IA</p>',
            unsafe_allow_html=True)

# Carte principale
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### Contenu de l'e-mail")
st.markdown("Entrez le contenu de votre e-mail ci-dessous :")

# Zone de texte pour l'e-mail
email_content = st.text_area(
    "",
    height=250,
    placeholder="Bonjour,\n\nJ'espère que ce message vous trouve bien. Je souhaiterais vous informer que notre réunion prévue demain à 14h00 doit être reportée à vendredi à la même heure en raison d'un conflit d'horaire. Pourriez-vous me confirmer si ce nouveau créneau vous convient ?\n\nMerci d'avance pour votre compréhension.\n\nCordialement,\nMarie",
    label_visibility="collapsed"
)

# Bouton pour générer
generate_button = st.button("Générer une ligne d'objet")

st.markdown('</div>', unsafe_allow_html=True)

# Traitement de la demande
if generate_button:
    # Vérification de la présence du contenu
    if not email_content:
        st.error("Veuillez entrer le contenu de l'e-mail")
    else:
        # Vérification de la clé API
        api_key = st.session_state.api_key

        if not api_key:
            # Essayer de charger depuis .env ou secrets une dernière fois
            api_key = load_api_key()
            if api_key:
                st.session_state.api_key = api_key
            else:
                st.error("Aucune clé API trouvée. Veuillez configurer votre clé API dans le panneau latéral.")
                st.stop()

        # Animation de chargement
        with st.spinner('Génération de la ligne d\'objet en cours...'):
            # Appeler l'API OpenAI
            subject, error = suggest_subject(email_content, api_key, model_option)

            if error:
                st.error(f"Erreur lors de l'appel à l'API OpenAI: {error}")
            else:
                # Afficher le résultat
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown('<p class="result-title">Ligne d\'objet suggérée:</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="result-content">{subject}</p>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

                # Ajouter à l'historique
                st.session_state.history.append({
                    "email": email_content[:100] + "..." if len(email_content) > 100 else email_content,
                    "subject": subject
                })

# Afficher l'historique s'il existe
if st.session_state.history:
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown("### Historique des générations")

    for i, item in enumerate(reversed(st.session_state.history[-5:])):
        st.markdown(f"""
        <div style="padding: 1rem; margin-bottom: 1rem; border-radius: 8px; background-color: white; border: 1px solid #E5E7EB;">
            <p style="color: #6B7280; font-size: 0.8rem;">E-mail #{len(st.session_state.history) - i}</p>
            <p style="color: #1F2937; font-size: 1rem; margin-bottom: 0.5rem;"><b>Contenu:</b> {item["email"]}</p>
            <p style="color: #10B981; font-size: 1.1rem; font-weight: 600;"><b>Ligne d'objet:</b> {item["subject"]}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    © 2025 - Générateur de Lignes d'Objet - Tous droits réservés
</div>
""", unsafe_allow_html=True)
