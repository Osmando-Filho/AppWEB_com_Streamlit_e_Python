# Este aplicativo é um exemplo de como usar o Streamlit para tirar fotos

import streamlit as st

st.title("Aplicação de Fotos 📸")

foto = st.camera_input("Tirar uma foto")

if foto:
    st.image(foto)
    st.download_button(
        label="📥 Baixar foto",
        data=foto.getvalue(),
        file_name="minha_foto.png",
        mime="image/png"
    )

# Para executar o aplicativo, usar o comando no terminal: python -m streamlit run foto.py
