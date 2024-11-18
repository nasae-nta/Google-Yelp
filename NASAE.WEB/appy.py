import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="PROJECT 001",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Estilos personalizados
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap');

    body {
        background: url('imagenes_web/logo.png') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Roboto', sans-serif;
        color: white;
        margin: 0;
    }

    h1 {
        font-family: 'Tahoma', sans-serif;
        color: white;
        font-size: 60px;  /* Tamaño del título principal */
        text-align: center; /* Centrar el título */
        margin-top: 20px;  /* Espaciado superior */
    }
    h3 {
        font-family: 'Tahoma', sans-serif;
        color: white;
        font-size: 40px;  /* Tamaño del título principal */
        text-align: center; /* Centrar el título */
        margin: 70px 0 50px 0;  /* Espaciado superior */

    }

    h2, h3 {
        font-family: 'Tahoma', sans-serif;
        color: white;
        
        
    }

    .title-box {
        margin-top: 40px;  /* Separación entre el título principal y el recuadro */
    }

    .box {
        border: 2px solid #FFD700;  /* amarillo neón */
        border-radius: 15px;
        padding: 20px;
        width: 60%;  /* Hacemos el recuadro más estrecho */
        margin-top: 20px;
        font-size:24px;
    }

    .about-title {
        font-size: 40px;
        font-weight: bold;
        text-align: left;
        color: #ffffff;  
        margin-top: 50px;
        margin-bottom: 20px;
    }

    iframe {
        width: 100%;  /* El iframe ocupa todo el ancho disponible */
        height: 800px;  /* Ajusta la altura a 800px */
        border: none;  /* Sin bordes extra en el iframe */
    }

    .logo-image {
        display: block;
        margin: 0 auto;
        width: 100%;  /* Aumentamos el tamaño del logo */
    }
    </style>
""", unsafe_allow_html=True)

# Título principal de la página
st.title("ANONIMOS NASAE 🚀")

# Espacio para "About Us"
st.markdown("<div class='about-title'>About Us😎</div>", unsafe_allow_html=True)

# Recuadro de "Sobre nosotros" en un recuadro amarillo
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("<div class='box'>Somos una consultora de datos formada por cinco miembros, provenientes de áreas variadas, pero con un mismo objetivo y pasión: la mejora de procesos de negocio. Estamos especializados en proporcionar soluciones estratégicas basadas en análisis de datos. Nuestro objetivo es apoyar a nuestros clientes en la toma de decisiones clave que impulsen su crecimiento y los posicionen como líderes en sus respectivas industrias. Trabajamos con negocios de diversos sectores, incluyendo restaurantes y comercios afines, ayudándolos a optimizar sus operaciones, identificar oportunidades de mercado y mejorar la experiencia de sus clientes mediante el uso inteligente de los datos.</div>", unsafe_allow_html=True)

with col2:
    st.image("imagenes_web/logo.png",caption= "Anonimos NASAE", use_column_width=True, width=300)  # Tamaño ajustado del logo

# Espacio para el dashboard
st.subheader("Dashboard Interactivo")

# Inserción del dashboard de Power BI mediante iframe
st.components.v1.html("""
    <iframe title="GOOGLE MAPS & YELP PORJECT 001 (2)" 
        width="100%" 
        height="800" 
        src="https://app.powerbi.com/view?r=eyJrIjoiMDdhMzdkMGItZDE3Ny00MWRiLTg2NjgtYTI3N2MwMWJkZGQ0IiwidCI6ImZjMDA1NDdhLTI0YmItNGU0Zi05ZDYxLTczZmNhNWViOWRmMyIsImMiOjR9&pageName=73ec77b604824e04f8eb" 
        frameborder="0" 
        allowfullscreen="true">
    </iframe>
""", height=800)



