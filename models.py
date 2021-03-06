from preprocessing import Preprocessing
import nltk
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer


def sentence_split(paragraph):
    data = nltk.sent_tokenize(paragraph)
    return data


def word_freq(data):
    w = []
    for sentence in data:
        for words in sentence:
            w.append(words)
    bag = list(set(w))
    res = {}
    for word in bag:
        res[word] = w.count(word)
    return res


def fit(paragraph):
    pre = Preprocessing()

    sentence_list = sentence_split(paragraph)
    data = []
    for i in range(len(sentence_list)):
        data.append(pre.stopword_removal(
            pre.tokenization(
                pre.casefolding(sentence_list[i]))))
    data = (list(filter(None, data)))

    wordfreq = word_freq(data)

    ranking = []
    for words in data:
        temp = 0
        for word in words:
            temp += wordfreq[word]
        ranking.append(temp)

    sort_list = sorted(range(len(ranking)),
                       key=ranking.__getitem__, reverse=True)
    n = 1
    sentence = ''
    for i in range(n):
        sentence += '{}. '.format(sentence_list[sort_list[i]])
    return sentence


def lex_rank(parser):
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, 2)
    result = ''
    for sentence in summary:
        result = result + str(sentence) + '. '
    return result


def luhn(parser):
    summarizer = LuhnSummarizer()
    summary = summarizer(parser.document, 2)
    result = ''
    for sentence in summary:
        result = result + str(sentence) + '. '
    return result


def lsa(parser):
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)
    result = ''
    for sentence in summary:
        result = result + str(sentence) + '. '
    return result
