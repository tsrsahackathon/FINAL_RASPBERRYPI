##summarization part starts


import nltk
import numpy
import requests
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

fb = open('PUNC_transcript.txt','r')
texts = fb.read()
fb.close()


arr = texts.split(".")

sentences = len(arr)/2.5



def summarize(text, language="english", sentences_count=sentences):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

if __name__ == "__main__":
    summary = summarize(texts)
    print(summary)

file = open("summary.txt","w")
file.write(summary)
file.close()
## summarization part ends
###############



###############
## keywords part start
api_key = "5457D9C0W8HO2JDZW2QCRVMNBBWYTMKAR00IGWYB88VQ74SWG0TYQHJQRJZLO7FT"
endpoint = "https://jamsapi.hackclub.dev/openai/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

fb = open('summary.txt', 'r')
textx = fb.read()
fb.close()


messages = []

user_question = "can you write the keywords from the given text" + textx

messages.append({"role": "user", "content": user_question})
data = {
    "model": "gpt-3.5-turbo",
    "messages": messages
}
response = requests.post(endpoint, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    assistant_answer = result["choices"][0]["message"]["content"]
    print(assistant_answer)
    messages.append({"role": "assistant", "content": assistant_answer})
else:
    print(f"Request failed: {response.reason}")

hold = open("keywords.txt","w")
hold.write(assistant_answer)
hold.close()


##keywords part end
###################