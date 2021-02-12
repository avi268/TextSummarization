from flask import Flask, request, render_template
import gensim
from gensim.summarization import summarize

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    original_text = request.form['text']
    summary=summarize(original_text, ratio=0.1, word_count=100)
    summary = summary.replace('\n','')
    return render_template('my-form.html',original_text = original_text,summary_text = summary)

if __name__=='__main__':
    app.run(debug=True,port=5000)