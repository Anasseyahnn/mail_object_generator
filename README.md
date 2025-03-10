# 📧 Email Subject Generator | Générateur de Lignes d'Objet


Une application web qui utilise l'IA pour générer des lignes d'objet efficaces pour vos emails. Fini les "Re:", "Suivi" ou "Important" ! Obtenez des lignes d'objet qui incitent réellement à l'ouverture de vos messages.

## 🌟 Fonctionnalités

- ✨ Interface utilisateur moderne et intuitive
- 🤖 Génération de lignes d'objet pertinentes avec GPT-4/GPT-3.5
- 📝 Analyse contextuelle du contenu de l'email
- 📊 Historique des générations récentes
- 🎨 Design responsive adapté à tous les appareils
- 🔑 Gestion flexible des clés API OpenAI
- 🌐 Support multilingue (l'application analyse le contenu dans n'importe quelle langue)

## 📸 Capture d'écran

![image](https://github.com/user-attachments/assets/affa5a4c-f132-4f4e-ac10-b5eb06bffbc3)

## 🚀 Installation

### Prérequis

- Python 3.7 ou supérieur
- Une clé API OpenAI

### Installation en local

```bash
# Cloner le dépôt
git clone https://github.com/votre-username/email-subject-generator.git
cd email-subject-generator

# Installer les dépendances
pip install -r requirements.txt

# Configurer la clé API
cp .env.example .env
# Puis modifier le fichier .env avec votre clé API

# Lancer l'application
streamlit run app.py
```

## 🔧 Configuration

Il existe plusieurs façons de configurer votre clé API :

1. **Via le fichier `.env`** :
   ```
   OPENAI_API_KEY=votre_clé_api_ici
   ```

2. **Via l'interface utilisateur** :
   Entrez votre clé API directement dans le panneau latéral de l'application.

3. **Via les secrets Streamlit** (pour déploiement) :
   Configurez `OPENAI_API_KEY` dans les secrets de votre déploiement Streamlit Cloud.

## 📝 Utilisation

1. Ouvrez l'application dans votre navigateur
2. Configurez votre clé API OpenAI si ce n'est pas déjà fait
3. Saisissez le contenu de votre email dans la zone de texte 
4. Cliquez sur "Générer une ligne d'objet"
5. Copiez la suggestion générée et utilisez-la pour votre email

## 💡 Conseils d'utilisation

- Pour des résultats optimaux, incluez l'ensemble du contenu de l'email
- L'application fonctionne mieux avec des emails bien structurés
- Vous pouvez régénérer plusieurs fois pour obtenir différentes suggestions
- Utilisez GPT-4 pour les résultats les plus précis ou GPT-3.5 pour plus de rapidité

## 🌐 Déploiement

Cette application peut facilement être déployée sur Streamlit Cloud :

```bash
# Assurez-vous que votre dépôt contient :
# - app.py
# - requirements.txt
# - .streamlit/config.toml (optionnel pour la personnalisation)

# Puis suivez les instructions sur https://streamlit.io/cloud
```

N'oubliez pas de configurer vos secrets (OPENAI_API_KEY) dans les paramètres du déploiement !

## 🛠️ Architecture du projet

```
.
├── app.py                  # Application Streamlit principale
├── requirements.txt        # Dépendances Python
├── .env.example            # Exemple de fichier de configuration
└── README.md               # Documentation
```

## 🔄 Contributions

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork ce dépôt
2. Créer une nouvelle branche (`git checkout -b feature/amélioration`)
3. Commiter vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amélioration`)
5. Ouvrir une Pull Request

## 🙏 Remerciements

- [OpenAI](https://openai.com/) pour leur API GPT
- [Streamlit](https://streamlit.io/) pour leur excellent framework
-  Monsieur Ed Enseignant a Udemy 
- Tous les contributeurs et utilisateurs de ce projet

---

Développé avec ❤️ par [Me contacter](https://anasseyahnn.github.io/Anasseyahnn-wbs/contact.html)
Acceder à l'application:  [Voir l'application](https://mail-object-generator.streamlit.app/)

*Besoin d'aide ou vous avez des questions ? N'hésitez pas à ouvrir une issue !*
