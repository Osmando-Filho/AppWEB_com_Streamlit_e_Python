# 🎙️ Conversor de Textos em Áudio com Streamlit

Este projeto é um aplicativo web simples desenvolvido em **Python** usando o **Streamlit**, que permite converter textos digitados em áudio (voz sintetizada) utilizando a biblioteca **gTTS (Google Text-to-Speech)**.

---

## 🚀 Funcionalidades

- Interface web simples e interativa feita com Streamlit.  
- Converte texto digitado em áudio automaticamente.  
- Reproduz o áudio diretamente no navegador.  
- Permite baixar o arquivo de áudio gerado em formato `.mp3`.  
- Suporte para idioma **português (pt-BR)** por padrão.

---

## 🧩 Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)  
- [io (módulo padrão do Python)](https://docs.python.org/3/library/io.html)

---

## 📦 Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/conversor-texto-audio.git
cd conversor-texto-audio


2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)
   python -m venv venv
   venv\Scripts\activate    # No Windows
   # ou
   source venv/bin/activate # No Linux/Mac

3️⃣ Instalar as dependências
   pip install streamlit gtts
   
4️⃣ Executar o aplicativo
   streamlit run app.py

🗣️ Exemplo de uso

Execute o app.

Digite um texto como:

"A tecnologia está transformando o mundo."

Clique em “🔊 Converter em Áudio”.

O áudio será gerado e reproduzido.

Clique em “📥 Baixar áudio” para salvar o arquivo .mp3.

📜 Licença

Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais e pessoais.

✨ Autor

Osmando Filho
💻 Estudante de Análise e Desenvolvimento de Sistemas
📧 Contato: oporfilho@gmail.com

🔗 GitHub: https://github.com/Osmando-Filho