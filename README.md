# ⚡ BotGroqAI

Um chatbot simples e super rápido usando Groq AI, Streamlit e o modelo Llama 3.1. Interface web moderna com histórico de conversas.

## 🚀 Funcionalidades

- **⚡ Super rápido** com Groq AI (muito mais rápido que OpenAI)
- **🆓 Totalmente gratuito** - API Groq com limite generoso
- **🦙 Llama 3.1** - Modelo de linguagem avançado
- **💬 Interface web** moderna e responsiva
- **📝 Histórico** de conversas na sessão
- **🔄 Streaming** de respostas em tempo real
- **🔒 Configuração segura** com arquivo .env

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Uma conta gratuita na Groq (https://console.groq.com)
- pip (gerenciador de pacotes do Python)

## 🛠️ Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/KarolNutty/BotGroqAI.git
cd BotGroqAI
```

### 2. Instale as dependências
```bash
pip install groq streamlit python-dotenv
```

### 3. Configure a API Key
1. Acesse: https://console.groq.com/keys
2. Faça login ou crie uma conta gratuita
3. Gere uma nova API Key
4. Crie um arquivo `.env` na pasta do projeto:

```bash
# Arquivo .env
GROQ_API_KEY=gsk_sua-chave-groq-aqui
```

### 4. Execute o chatbot
```bash
streamlit run chatbot.py
```

O navegador abrirá automaticamente em `http://localhost:8501`

## 🎯 Como usar

1. **Abra o chatbot** no navegador
2. **Digite sua mensagem** na caixa de texto inferior
3. **Pressione Enter** ou clique no botão enviar
4. **Veja a resposta** aparecer em tempo real
5. **Continue a conversa** - o histórico é mantido durante a sessão

## 📁 Estrutura do projeto

```
BotGroqAI/
├── 📄 chatbot.py           # Código principal
├── 📄 .env                 # Chaves da API (não commitado)
├── 📄 requirements.txt     # Dependências
├── 📄 README.md           # Este arquivo
└── 📄 .gitignore          # Arquivos ignorados pelo Git
```

## 🔧 Tecnologias utilizadas

- **[Groq](https://groq.com/)** - API de IA super rápida
- **[Streamlit](https://streamlit.io/)** - Framework para apps web em Python
- **[Llama 3.1](https://llama.meta.com/)** - Modelo de linguagem da Meta
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** - Gerenciamento de variáveis de ambiente

## ⚙️ Configurações avançadas

### Modelos disponíveis na Groq:
- `llama-3.1-8b-instant` - Rápido e eficiente (padrão)
- `llama-3.1-70b-versatile` - Mais inteligente, um pouco mais lento
- `mixtral-8x7b-32768` - Alternativa da Mistral
- `gemma2-9b-it` - Modelo do Google

### Para trocar de modelo:
Edite a linha no `chatbot.py`:
```python
model="llama-3.1-8b-instant"  # Altere aqui
```

## 🚨 Solução de problemas

### Erro de API Key
```
❌ Chave da API Groq não encontrada!
```
**Solução**: Verifique se o arquivo `.env` existe e contém `GROQ_API_KEY=sua-chave`

### Erro de modelo descontinuado
```
Código de erro: 400 - model_decommissioned
```
**Solução**: Modelo foi desativado. Troque para `llama-3.1-8b-instant`

### Erro de dependências
```
ModuleNotFoundError: No module named 'groq'
```
**Solução**: Execute `pip install groq streamlit python-dotenv`

## 🔮 Próximas funcionalidades

- [ ] Salvamento de conversas em arquivo
- [ ] Diferentes personas/estilos de resposta
- [ ] Upload de documentos para análise
- [ ] Geração de imagens (quando disponível na Groq)
- [ ] Modo escuro/claro
- [ ] Exportação de conversas (PDF, TXT)

## 📊 Comparação Groq vs OpenAI

| Aspecto | Groq | OpenAI |
|---------|------|--------|
| **Velocidade** | ⚡ Muito rápido | 🐌 Mais lento |
| **Preço** | 🆓 Gratuito | 💰 Pago |
| **Modelos** | Llama, Mixtral, Gemma | GPT-3.5, GPT-4 |
| **Limite** | Generoso | Limitado |

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m '✨ Adiciona nova funcionalidade'
   ```
4. Push para a branch:
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um Pull Request

## 📝 Changelog

### v1.0.0 (2025-01-XX)
- ✅ Chatbot básico funcional
- ✅ Interface Streamlit
- ✅ Integração com Groq API
- ✅ Histórico de conversas
- ✅ Configuração via .env

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**KarolNutty** 
- GitHub: [@KarolNutty](https://github.com/KarolNutty)

## 🙏 Agradecimentos

- [Groq](https://groq.com/) pela API incrível e gratuita
- [Streamlit](https://streamlit.io/) pela facilidade de criar interfaces
- [Meta](https://meta.com/) pelo modelo Llama

---

⭐ **Se este projeto te ajudou, deixe uma estrela no repositório!**

🐛 **Encontrou um bug?** Abra uma [issue](https://github.com/KarolNutty/BotGroqAI/issues)

💡 **Tem uma ideia?** Contribua com o projeto!