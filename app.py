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

    if categoria == "Ligas":
        st.subheader("⚽ Ligas")
        st.write("Equipos disponibles:")
        st.write("- FC Barcelona")
        st.write("- Real Madrid")
        st.write("- Manchester United")

    elif categoria == "Selecciones":
        st.subheader("🌎 Selecciones")
        st.write("Equipos disponibles:")
        st.write("- Perú")
        st.write("- Argentina")
        st.write("- Brasil")

    st.button("Agregar al carrito 🛍️")

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

    st.subheader("Noticias")
    st.write("Últimas novedades del fútbol mundial ⚽")

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
