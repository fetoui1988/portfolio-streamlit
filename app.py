import streamlit as st
import base64

st.set_page_config(
    page_title="Portfolio Atef Fetoui",
    layout="wide"
)

# =========================
# FONCTION IMAGE RONDE
# =========================
def image_ronde(path, size=180):
    with open(path, "rb") as file:
        img = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/jpeg;base64,{img}"
                 style="
                    width:{size}px;
                    height:{size}px;
                    border-radius:50%;
                    object-fit:cover;
                    border:4px solid white;
                    box-shadow:0 4px 15px rgba(0,0,0,0.25);
                 ">
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# CSS CARTES PROJETS
# =========================
st.markdown("""
<style>
.project-card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #ddd;
    height: 340px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: 0.3s;
    margin-bottom: 25px;
}

.project-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.20);
    background-color: #f0f7ff;
}

.project-title {
    font-size: 22px;
    font-weight: bold;
    color: #00458a;
    margin-bottom: 10px;
}

.project-tech {
    font-size: 14px;
    color: #555;
    margin-bottom: 15px;
}

.project-desc {
    font-size: 15px;
    color: #333;
    line-height: 1.5;
    margin-bottom: 20px;
}

.project-link {
    display: inline-block;
    padding: 10px 16px;
    background-color: #00458a;
    color: white !important;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
}

.project-link:hover {
    background-color: #002f5f;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
image_ronde("atefimage.jpg", 160)

st.sidebar.title("Atef Fetoui")
st.sidebar.write("Data Analyst – Finance & SAP")

menu = st.sidebar.radio(
    "Navigation",
    ["Accueil", "Présentation / CV", "Projets", "Contact"]
)

# =========================
# PAGE ACCUEIL
# =========================
def page_accueil():

    col1, col2 = st.columns([1, 2])

    with col1:
        image_ronde("atefimage.jpg", 280)

    with col2:
        st.title("Bienvenue sur mon portfolio")
        st.subheader("Atef Fetoui")
        st.write("**Data Analyst – Finance & SAP**")

        st.write("""
        Professionnel en finance et analyse de données, passionné par les technologies
        d’affaires, la visualisation de données et le développement d’applications
        interactives.

        Je développe des projets avec Python, SQL, Streamlit, Machine Learning,
        Power BI, Tableau et SAP afin de transformer les données en outils
        d’aide à la décision performants.

        Cette application portfolio a été entièrement réalisée par moi-même
        pour présenter mes compétences techniques, mes projets et mon parcours
        professionnel dans un environnement moderne et interactif.
        """)

        st.info("Utilisez le menu à gauche pour consulter mon CV, mes projets et mes informations de contact.")

    st.subheader("💡 Qualités professionnelles")

    st.write("""
    Je suis une personne motivée, rigoureuse et orientée vers l’apprentissage continu.
    J’aime résoudre des problèmes complexes, analyser des données et développer
    des solutions pratiques capables d’améliorer la performance des organisations.

    Grâce à mon parcours en finance, en technologie d’affaires et en analyse
    de données, je possède une vision multidisciplinaire qui me permet de comprendre
    autant les enjeux financiers que les besoins technologiques d’une entreprise.

    Je suis également reconnu pour ma capacité d’adaptation, mon autonomie,
    ma persévérance et mon intérêt pour les nouvelles technologies comme
    l’intelligence artificielle, le machine learning, les systèmes ERP et
    les outils de visualisation avancée.
    """)

# =========================
# PAGE CV
# =========================
def page_cv():

    st.title("📄 Présentation / CV")

    st.header("🎯 Objectif professionnel")

    st.write("""
    Professionnel en finance titulaire d’un MBA, spécialisé en analyse de données,
    machine learning et systèmes SAP. Expérience en exploitation de données financières,
    modélisation, analyse de performance et optimisation des processus pour soutenir
    la prise de décision stratégique.
    """)

    st.header("💻 Compétences techniques")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Python")
        st.progress(85)

        st.write("SQL")
        st.progress(80)

        st.write("Streamlit")
        st.progress(80)

        st.write("Machine Learning")
        st.progress(80)

    with col2:
        st.write("Excel avancé")
        st.progress(90)

        st.write("Analyse financière")
        st.progress(85)

        st.write("Power BI")
        st.progress(78)

        st.write("Tableau")
        st.progress(80)

        st.write("SAP")
        st.progress(75)

    st.header("🛠️ Autres compétences")

    st.markdown("""
    - Analyse financière
    - Modélisation financière
    - Gestion de portefeuille
    - SAP (MM, SD, FI)
    - Power BI
    - Tableau
    - SQL Server
    - Python pour la science des données
    - Machine Learning
    - Visualisation de données
    - Analyse prédictive
    - Excel avancé
    - Gestion de bases de données
    """)

    st.header("📌 Expériences professionnelles")

    st.subheader("Analyste financier et analyste de données — Banque Nationale Agricole")
    st.write("2018 – 2022")
    st.markdown("""
    - Analyse financière et analyse de données pour soutenir la prise de décision
    - Production de rapports de gestion et de tableaux de bord
    - Analyse des portefeuilles clients et suivi des indicateurs de performance
    - Extraction, validation et contrôle de la qualité des données
    - Participation à l’amélioration des processus et à l’optimisation des activités
    - Collaboration avec les équipes financières et opérationnelles
    """)

    st.divider()

    st.subheader("Commis de plancher — Ropack Pharma Solutions")
    st.write("2022 – 2024")
    st.markdown("""
    - Gestion des composantes, des matières premières et des fournitures des lignes de production
    - Suivi des inventaires, application du FIFO et documentation des dossiers de production
    - Respect des Bonnes Pratiques de Fabrication (BPF) et des normes de qualité
    - Participation aux projets d’amélioration continue et au maintien des standards de productivité
    - Formation et accompagnement des nouveaux employés
    """)

    st.divider()

    st.subheader("Service de livraison, travailleur autonome — Intelcom Express")
    st.write("2016 – 2018")
    st.markdown("""
    - Planification et optimisation des itinéraires
    - Gestion autonome des priorités et respect des délais
    - Excellent service à la clientèle et résolution de problèmes
    """)

    st.header("🎓 Formation")

    st.markdown("""
    **Certificat en technologie d’affaire TI** — UQAM  
    Montréal, Canada | 2024 – 2026  
    Moyenne cumulative : **4.0 / 4.3**

    **MBA Finance** — Université Laval  
    Québec, Canada | 2012 – 2014

    **Licence fondamentale en finance** — IHEC Sousse  
    Sousse, Tunisie | 2008 – 2011
    """)

    st.header("📜 Certifications")

    st.markdown("""
    - Cours sur le commerce des valeurs mobilières au Canada — CSI Canada
    - Certificat en analyse technique — CSI Canada
    """)

    st.header("🌍 Langues")

    st.write("Français")
    st.progress(95)

    st.write("Anglais")
    st.progress(75)

# =========================
# PAGE PROJETS
# =========================
def page_projets():

    st.title("📁 Mes projets")

    st.write("""
    Voici une sélection de projets que je vais présenter dans mon portfolio.

    """)

    projets = [
        {
            "titre": "Acceptation carte bancaire",
            "tech": "Python • Machine Learning • Scikit-learn",
            "desc": "Modèle de classification pour prédire si un client accepte une offre bancaire ou une carte.",
            "lien": "https://fetoui1988-supercard-streamlit-app-app-ehc5mu.streamlit.app/"
        },
        {
            "titre": "Projet SAP GBI",
            "tech": "SAP • MM • SD • FI",
            "desc": "Simulation complète des processus achat, vente, stock et finance dans SAP GBI.",
            "lien": "#"
        },
        {
            "titre": "Projet SQL Server",
            "tech": "SQL Server • Requêtes • Base de données",
            "desc": "Création d’une base relationnelle avec tables, clés, jointures et analyses SQL.",
            "lien": "#"
        },
        {
            "titre": "Dashboard financier",
            "tech": "Python • Streamlit • Pandas",
            "desc": "Application interactive pour analyser revenus, dépenses, ratios financiers et tendances.",
            "lien": "#"
        },
        {
            "titre": "Clustering clients",
            "tech": "Python • K-Means • Analyse non supervisée",
            "desc": "Segmentation des clients selon leurs comportements et caractéristiques.",
            "lien": "#"
        },
        {
            "titre": "Dashboard Power BI",
            "tech": "Power BI • KPI • Visualisation",
            "desc": "Tableau de bord pour suivre les indicateurs de performance et faciliter la décision.",
            "lien": "#"
        }
    ]

    for i in range(0, len(projets), 3):

        cols = st.columns(3)

        for j in range(3):

            if i + j < len(projets):

                p = projets[i + j]

                with cols[j]:

                    st.markdown(
                        f"""
                        <div class="project-card">
                            <div class="project-title">{p["titre"]}</div>
                            <div class="project-tech">{p["tech"]}</div>
                            <div class="project-desc">{p["desc"]}</div>
                            <a class="project-link" href="{p["lien"]}" target="_blank">
                                🚀 Voir le projet
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

# =========================
# PAGE CONTACT
# =========================
def page_contact():

    st.title("📞 Contact")

    st.write("N'hésitez pas à me contacter.")

    st.divider()

    st.subheader("👤 Informations")

    st.write("📍 Montréal, Canada")

    st.write("📧 fetoui.atef@courrier.uqam.ca")

    st.write("📱 514-222-0227")

    st.markdown(
        "[🔗 Mon LinkedIn](https://www.linkedin.com/in/atef-fetoui-0936955a/)"
    )

    st.divider()

    st.info("Le formulaire de contact sera ajouté prochainement.")

# =========================
# ROUTAGE
# =========================
if menu == "Accueil":
    page_accueil()

elif menu == "Présentation / CV":
    page_cv()

elif menu == "Projets":
    page_projets()

elif menu == "Contact":
    page_contact()

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<center>© 2026 Atef Fetoui – Portfolio professionnel</center>",
    unsafe_allow_html=True
)