import nltk


from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import json
import requests
import speech_recognition as sr
from os import path
from pydub import AudioSegment
print('transcribing')
# convert mp3 file to wav
sound = AudioSegment.from_mp3("/home/aryan-khandelwal/Documents/hack/FINAL_RASPBERRYPI-master/test1.wav")
sound.export("transcript.wav", format="wav")


# transcribe audio file
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file



filez = r.recognize_google(audio)




## punctuation GPT starts
import requests

api_key = "5457D9C0W8HO2JDZW2QCRVMNBBWYTMKAR00IGWYB88VQ74SWG0TYQHJQRJZLO7FT"
endpoint = "https://jamsapi.hackclub.dev/openai/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

messages = []

user_question = "To this text, add punctuation and grammar such as commas and fullstops" + filez

messages.append({"role": "user", "content": user_question})
data = {
    "model": "gpt-3.5-turbo",
    "messages": messages
}
response = requests.post(endpoint, headers=headers, json=data)
temp=''
if response.status_code == 200:
    result = response.json()
    assistant_answer = result["choices"][0]["message"]["content"]
    print(assistant_answer)
    temp=assistant_answer
    messages.append({"role": "assistant", "content": assistant_answer})
else:
    print(f"Request failed: {response.reason}")


fp = open('PUNC_transcript.txt', 'w')
fp.write(temp)
fp.close()

