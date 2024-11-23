import os
import pygame
import logging
import sounddevice as sd
import scipy.io.wavfile as wavfile
from playsound import playsound
from pynput import keyboard
from langchain_groq import ChatGroq
from faster_whisper import WhisperModel
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from gtts import gTTS

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

# Configurações principais
DURATION = 5  # Tempo de gravação em segundos
SAMPLE_RATE = 16000  # Taxa de amostragem do áudio
OUTPUT_AUDIO_FILE = "input_audio.wav"
RESPONSE_AUDIO_FILE = "response_audio.mp3"

# Carrega variáveis de ambiente do .env
_ = load_dotenv(find_dotenv())

# Obtém a API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
  raise ValueError("A API Key não foi encontrada. Verifique o .env ou as variáveis de ambiente.")

# Configuração do Whisper
whisper_model = WhisperModel(
  "tiny", 
  device="cpu", # Use 'cuda' para GPU, se disponível
  compute_type="float32", 
  cpu_threads=os.cpu_count(), 
  num_workers=os.cpu_count()
)

# Inicializa client OpenAI
client = OpenAI()

# Grava o áudio
def record_audio(filename):
  try:
    logging.info("Gravando áudio... Fale agora.")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="int16")
    sd.wait()  # Aguarda o término da gravação
    wavfile.write(filename, SAMPLE_RATE, audio)
    # logging.info("Áudio gravado com sucesso!")
  except Exception as e:
    logging.error(f"Erro ao gravar áudio: {e}")

# Transcreve o áudio
def transcribe_audio(filename):
  try:
    # logging.info("Transcrevendo áudio...")
    segments, _ = whisper_model.transcribe(
      filename,    
      temperature=0.0,     
      task="transcribe",
      language="pt"
    )
    transcription = " ".join([segment.text for segment in segments])
    logging.info(f" - Você: {transcription}")
    return transcription
  except Exception as e:
    logging.error(f"Erro ao transcrever áudio: {e}")
    return None

# Consulta resposta da IA
def get_response_from_ai(prompt):
  try:
    # logging.info("Consultando o modelo de IA...")
    response = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=[{"role": "user", "content": f"Responda em português: {prompt}"}]
    )
    ai_response = response.choices[0].message.content
    logging.info(f" - Assistente: {ai_response}")
    return ai_response
  except Exception as e:
    logging.error(f"Erro ao consultar IA: {e}")
    return None

# Usa o TTS para converter texto em áudio
def text_to_speech(text, output_file):
  try:
    # logging.info("Convertendo resposta em áudio...")
    # gTTS (Google Text-to-Speech)
    tts = gTTS(text, lang="pt")
    tts.save(output_file)
    # logging.info(f"Áudio gerado: {output_file}")
  except Exception as e:
    logging.error(f"Erro ao converter texto em áudio: {e}")

def play_audio(filename):
  try:
    logging.info("Reproduzindo áudio...")
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Aguarda o término da reprodução
    while pygame.mixer.music.get_busy():
      continue
    logging.info("Pressione 'r' para gravar novamente ou 'esc' para sair.")
  except Exception as e:
    logging.error(f"Erro ao reproduzir áudio: {e}")
  finally:
    pygame.mixer.quit()

def on_key_press(key):
  try:
    if hasattr(key, 'char') and key.char == "r":  # Pressione 'r' para gravar
      record_audio(OUTPUT_AUDIO_FILE)
      transcription = transcribe_audio(OUTPUT_AUDIO_FILE)
      if transcription:
        response = get_response_from_ai(transcription)
        if response:
          text_to_speech(response, RESPONSE_AUDIO_FILE)
          play_audio(RESPONSE_AUDIO_FILE)
    elif key == key.esc: # Pressione 'esc' para sair
      logging.info("Tecla 'esc' pressionada. Encerrando o programa.")
      return False
  except AttributeError:
    pass # Ignorar teclas especiais
  except Exception as e:
    logging.error(f"Erro no evento de tecla: {e}")

def main():
  logging.info("Pressione 'r' para iniciar a gravação ou 'esc' para sair.")
  with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()

if __name__ == "__main__":
  main()