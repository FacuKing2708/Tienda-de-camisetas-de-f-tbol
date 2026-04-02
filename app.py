import streamlit as st

st.set_page_config(page_title="Tienda de Camisetas", layout="wide")

# 🔹 MENÚ LATERAL
st.sidebar.title("⚽ Menú")
pagina = st.sidebar.radio("Navegación", [
    "Inicio",
    "Tienda",
    "Nosotros",
    "Blog",
    "Contacto",
    "Mi cuenta"
])

# 🔹 INICIO
if pagina == "Inicio":
    st.title("⚽ Tienda de Camisetas de Fútbol")
    st.subheader("Bienvenido a la mejor tienda deportiva")

    st.image("https://images.unsplash.com/photo-1518091043644-c1d4457512c6")

    st.markdown("""
    ### 🔥 ¿Qué ofrecemos?
    - Camisetas de clubes
    - Selecciones nacionales
    - Personalización de camisetas
    
    👉 Usa el menú de la izquierda para navegar
    """)

# 🔹 TIENDA
elif pagina == "Tienda":
    st.title("🛒 Tienda")

    categoria = st.selectbox("Selecciona categoría", ["Ligas", "Selecciones"])

    # 🔸 LIGAS
    if categoria == "Ligas":
        st.subheader("⚽ Ligas")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg", width=150)
            st.write("**FC Barcelona**")
            st.write("💰 $70")
            st.button("Comprar Barcelona")

        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg", width=150)
            st.write("**Real Madrid**")
            st.write("💰 $75")
            st.button("Comprar Madrid")

        with col3:
            st.image("https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg", width=150)
            st.write("**Manchester United**")
            st.write("💰 $65")
            st.button("Comprar United")

    # 🔸 SELECCIONES
    elif categoria == "Selecciones":
        st.subheader("🌎 Selecciones")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Peru.svg", width=150)
            st.write("**Perú**")
            st.write("💰 $60")
            st.button("Comprar Perú")

        with col2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Argentina.svg", width=150)
            st.write("**Argentina**")
            st.write("💰 $70")
            st.button("Comprar Argentina")

        with col3:
            st.image("https://upload.wikimedia.org/wikipedia/en/0/05/Brazil_national_football_team_logo.svg", width=150)
            st.write("**Brasil**")
            st.write("💰 $68")
            st.button("Comprar Brasil")

# 🔹 NOSOTROS
elif pagina == "Nosotros":
    st.title("👥 Nosotros")

    st.subheader("¿Quiénes somos?")
    st.write("Somos una tienda especializada en camisetas de fútbol.")

    st.subheader("Misión y Visión")
    st.write("Ofrecer productos de calidad a todos los fanáticos del fútbol.")

# 🔹 BLOG
elif pagina == "Blog":
    st.title("📰 Blog")

    st.subheader("🔥 Última noticia")

    st.image("https://images.unsplash.com/photo-1508098682722-e99c643e7f7b")

    st.markdown("""
    **El fútbol mundial se prepara para una nueva temporada llena de emoción ⚽**

    Los grandes clubes de Europa como el Real Madrid, Barcelona y Manchester United
    ya presentaron sus nuevas camisetas para la temporada, generando gran expectativa
    entre los fanáticos.

    Las selecciones también se preparan para próximas competiciones internacionales,
    mostrando nuevos diseños innovadores.
    """)

# 🔹 CONTACTO
elif pagina == "Contacto":
    st.title("📞 Contacto")

    st.write("📱 WhatsApp: +51 999 999 999")
    st.write("📍 Ubicación: Lima, Perú")

    st.text_input("Nombre")
    st.text_area("Mensaje")
    st.button("Enviar")

# 🔹 MI CUENTA
elif pagina == "Mi cuenta":
    st.title("👤 Mi cuenta")

    st.text_input("Correo electrónico")
    st.text_input("Contraseña", type="password")

    st.button("Iniciar sesión")
