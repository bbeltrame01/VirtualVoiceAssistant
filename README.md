# Assistente Virtual com Voz 🚀🎙️

Este repositório contém o código de um **assistente virtual com voz** desenvolvido em Python. Ele grava a sua voz, transcreve o áudio para texto, utiliza uma inteligência artificial para gerar respostas e reproduz a resposta em áudio.

## 🛠️ Funcionalidades

- **Gravação de Áudio:** Captura áudio do usuário em tempo real.
- **Transcrição:** Converte o áudio gravado em texto usando o modelo Whisper.
- **Assistente Inteligente:** Consulta um modelo de IA para gerar respostas.
- **Texto para Fala:** Converte as respostas da IA em áudio com Google Text-to-Speech (gTTS).
- **Interatividade por Teclado:**
  - Pressione `R` para iniciar uma nova interação.
  - Pressione `Esc` para encerrar o programa.

---

## 📂 Estrutura do Projeto

```plaintext
├── .env                       # Configurações de ambiente (API Key do OpenAI).
├── main.py                    # Código principal do assistente virtual.
└── requirements.txt           # Lista de dependências do projeto.
```

---

## 🚀 Como Usar

### 1️⃣ Pré-requisitos
- Python 3.8 ou superior.
- Configurar sua API Key do OpenAI em um arquivo `.env`:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```
- Dependências do Python:
  ```bash
  pip install -r requirements.txt
  ```

### 2️⃣ Execução do Projeto
1. Execute o programa com:
   ```bash
   python main.py
   ```
2. Pressione `R` para começar a gravar. 
3. Interaja com o assistente e ouça as respostas!
4. Pressione `Esc` para sair.

---

## 🔧 Dependências

Este projeto utiliza as seguintes bibliotecas:

- [Pygame](https://www.pygame.org/) - Reproduzir áudio.
- [Sounddevice](https://python-sounddevice.readthedocs.io/) - Captura de áudio.
- [Scipy](https://scipy.org/) - Manipulação de arquivos de áudio.
- [Whisper](https://github.com/openai/whisper) - Transcrição de áudio.
- [Langchain](https://www.langchain.com/) - Integração com modelos de IA.
- [Google Text-to-Speech (gTTS)](https://gtts.readthedocs.io/) - Conversão de texto em áudio.
- [Pynput](https://pynput.readthedocs.io/) - Captura de eventos de teclado.

Para instalar todas as dependências, basta rodar:
```bash
pip install -r requirements.txt
```

---

## 📋 Observações

- **Compatibilidade:** O código foi testado no Windows/Linux, mas pode exigir adaptações no macOS.
- **Configuração do Whisper:** O modelo `tiny` é usado por padrão. Para maior precisão, considere utilizar modelos maiores, mas tenha em mente o impacto no desempenho.
- **Licença:** O código está disponível para uso pessoal. Verifique as licenças das bibliotecas utilizadas.

---

## 🖥️ Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.
