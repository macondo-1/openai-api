from openai import OpenAI

client = OpenAI()

audio_file = open("/Users/albertoruizcajiga/Documents/SIS final/openai/openai-api/audio_file.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcription.text)