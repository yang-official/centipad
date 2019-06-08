from flask import Flask, render_template, url_for, request, session
from docusign import embedded_signing_ceremony
import webbrowser
import time
import spacy
from spacy_summarization import text_summarizer, text_modeler, flagger
from google_ml import classify_text
import config

nlp = spacy.load('en_core_web_sm')
app = Flask(__name__)

def readingTime(mytext):
	total_words = len([ token.text for token in nlp(mytext)])
	estimatedTime = total_words/200.0
	return estimatedTime

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
	start = time.time()
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		final_reading_time = readingTime(rawtext)
		final_summary = text_summarizer(rawtext)
		summary_reading_time = readingTime(final_summary)
		end = time.time()
		final_time = end-start
		flagged = flagger(rawtext)
		topic = text_modeler(rawtext)
	session['topic'] = topic
	session['flagged'] = flagged
	return render_template('index.html',ctext=rawtext,topic=topic,flagged=flagged,final_summary=final_summary,final_time=final_time,final_reading_time=final_reading_time,summary_reading_time=summary_reading_time)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/legal')
def legal():
	if 'topic' in session and 'flagged' in session:
		topic = session['topic']
		flagged = session['flagged']
	else:
		topic = 'error'
		flagged = 'error'
	return render_template('legal.html', topic=topic, flagged=flagged)

@app.route("/docusign")
def docusign():
    webbrowser.open_new_tab(embedded_signing_ceremony())
    return 'See New Tab'

if __name__ == '__main__':
    app.secret_key = config.secret
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
