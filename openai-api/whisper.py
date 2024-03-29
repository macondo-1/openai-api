from openai import OpenAI

AUDIO_FILE_PATH = '/Users/albertoruizcajiga/Documents/SIS final/openai/openai-api/13- Beth Golay - KMUW.m4a'

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key="My API Key",
)
#from docx import Document

def transcribe_audio(AUDIO_FILE_PATH):
    with open(AUDIO_FILE_PATH, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create("whisper-1", audio_file)
    return transcription['text']

#print(transcribe_audio(AUDIO_FILE_PATH))

from openai import OpenAI
client = OpenAI()

audio_file= open("/Users/albertoruizcajiga/Documents/SIS final/openai/openai-api/audio_file.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)