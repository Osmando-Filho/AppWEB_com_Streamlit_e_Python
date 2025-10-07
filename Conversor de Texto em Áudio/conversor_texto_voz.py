# Este aplicativo é um exemplo de como usar o Streamlit para gravar voz

import streamlit as st
from gtts import gTTS
import io

st.title("Conversor de Textos em Áudio 🎙️")

st.write("Digite o seu texto abaixo:")
texto = st.text_area("", height=200)

if st.button("🔊 Converter em Áudio"):
    if texto.strip():
        # Converte o texto em áudio (idioma português)
        tts = gTTS(text=texto, lang='pt')
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        # Exibe o áudio
        st.audio(audio_bytes, format='audio/mp3')

        # Botão para baixar o arquivo
        st.download_button(
            label="📥 Baixar áudio",
            data=audio_bytes,
            file_name="meu_audio.mp3",
            mime="audio/mp3"
        )
    else:
        st.warning("⚠️ Por favor, digite algum texto para converter.")



# Para executar o aplicativo, usar o comando no terminal: python -m streamlit run conversor_texto_voz.py