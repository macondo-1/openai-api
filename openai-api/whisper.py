from openai import OpenAI

client = OpenAI()

audio_file = open("/Users/albertoruizcajiga/Documents/SIS final/openai/openai-api/audio_file.m4a", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

#print(transcription.text)
transcription = transcription.text

def abstract_summary_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return completion.choices[0].message.content



def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    return {
        'abstract_summary': abstract_summary,
    }

print(meeting_minutes(transcription))