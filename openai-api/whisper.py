from openai import OpenAI
from pydub import AudioSegment

client = OpenAI()

def transcribe_english_to_english():
    audio_file = open("good_morning_10.mp3", "rb")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file
    )
    transcription = transcription.text

    transcription_file = open('transcription.txt', 'w')
    transcription_file.write(transcription)
    transcription_file.close()

    return transcription

def abstract_summary_extraction(transcription):
    completion = client.chat.completions.create(
        #model="gpt-4-0613",
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


"""
song = AudioSegment.from_mp3("ukranian_audio.mp3")

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000

first_10_minutes = song[:ten_minutes]

first_10_minutes.export("good_morning_10.mp3", format="mp3")
"""


"""
transcription_file = open('transcription.txt', 'r')
transcription = transcription_file.read()
transcription_file.close()
abstract = abstract_summary_extraction(transcription)


abstract_file = open('abstract.txt', 'w')
abstract_file.write(abstract)
abstract_file.close()
"""

def translate_to_english(file_name):

    audio_file= open(file_name, "rb")
    translation = client.audio.translations.create(
      model="whisper-1", 
      file=audio_file
    )
    trans_text = translation.text

    translation_file = open('ukranian_translation.txt', 'w')
    translation_file.write(trans_text)
    translation_file.close()


file_name = 'ukranian_audio_short.mp3'
translate_to_english(file_name)