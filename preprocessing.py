import re
import os

class Preprocessing(object):
    def __init__(self):
        self.stopwords = [line.rstrip('\n\r') for line in open(os.path.join(os.getcwd(), 'stopwords.txt'))]

    def casefolding(self, sentence):
        sentence = sentence.lower()
        sentence = re.sub(r'[^a-z]', ' ', re.sub("’", '', sentence))
        return sentence

    def tokenization(self, sentence):
        return sentence.split()

    def stopword_removal(self, token):
        temp = []
        for i in range(len(token)):
            if token[i] not in self.stopwords:
                temp.append(token[i])
        return temp