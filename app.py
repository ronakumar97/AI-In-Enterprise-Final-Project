import algorithms
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from flask import Flask, request, render_template
import re

app = Flask(__name__)


def summarize_url(algorithm, text_input):
    text_input = Article(text_input)
    text_input.download()
    text_input.parse()

    parser = PlaintextParser.from_string(text_input.text, Tokenizer("english"))

    if(algorithm == 'stopwords'):
        return algorithms.fit(text_input.text)
    elif(algorithm == 'lexrank'):
        return algorithms.lex_rank(parser)
    elif (algorithm == 'luhn'):
        return algorithms.luhn(parser)
    elif (algorithm == 'lsa'):
        return algorithms.lsa(parser)


def summarize_text(algorithm, text_input):
    parser = PlaintextParser.from_string(text_input, Tokenizer("english"))

    if (algorithm == 'stopwords'):
        return algorithms.fit(text_input)
    elif (algorithm == 'lexrank'):
        return algorithms.lex_rank(parser)
    elif (algorithm == 'luhn'):
        return algorithms.luhn(parser)
    elif (algorithm == 'lsa'):
        return algorithms.lsa(parser)


@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == "POST"):
        input = request.form.getlist('inputs')
        algorithm = request.form.getlist('algorithms')
        text_input = request.form.get('text_input')

        if(input[0] == 'url'):
            result = summarize_url(algorithm[0], text_input)
        else:
            result = summarize_text(algorithm[0], text_input)

        result = re.sub('\W+', ' ', result)
        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
