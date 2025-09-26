import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração da página
st.set_page_config(page_title="🤖 ChatBot com Groq", page_icon="⚡")

# Título
st.title("⚡ ChatBot com Groq")

# Verificar se a API key está configurada
api_key = os.getenv("GROQ_API_KEY")

if api_key:
    st.success("✅ API Groq configurada!")
    
    # Configurar cliente Groq
    client = Groq(api_key=api_key)
    
    # Histórico de conversa
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Mostrar histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Input do usuário
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Adicionar mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Gerar resposta
        with st.chat_message("assistant"):
            with st.spinner("⚡ Processando..."):
                try:
                    # Usar o modelo Llama3 do Groq
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {"role": "user", "content": prompt}
                        ],
                        model="llama-3.1-8b-instant",  # Modelo rápido e gratuito
                        temperature=0.7,
                        max_tokens=1024
                    )
                    
                    answer = chat_completion.choices[0].message.content
                    st.write(answer)
                    
                    # Adicionar resposta ao histórico
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    
                except Exception as e:
                    st.error(f"Erro: {e}")

else:
    st.error("❌ Chave da API Groq não encontrada!")
    st.info("🔧 Configure no arquivo .env: GROQ_API_KEY=sua-chave-aqui")
    st.info("🔗 Obtenha sua chave em: https://console.groq.com/keys")