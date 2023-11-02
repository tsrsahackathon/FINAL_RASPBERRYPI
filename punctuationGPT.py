
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

with open('PUNC_transcript.txt','w') as fb:
    texts = fb.read()

text = texts
arr = text.split(".")

sentences = len(arr)/2.5

print(sentences)

def summarize(text, language="english", sentences_count=sentences):
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join([str(sentence) for sentence in summary])

if __name__ == "__main__":
    summary = summarize(text)
    print(summary)

file = open("<FILE PATH>","w")
file.write(summary)


