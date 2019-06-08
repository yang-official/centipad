from flask import Flask
from docusign import embedded_signing_ceremony
import webbrowser
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/docusign")
def docusign():
    webbrowser.open_new_tab(embedded_signing_ceremony())
    return 'See New Tab'

if __name__ == '__main__':
	app.run(debug=True)
