from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return translator.englishtofrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    return translator.frenchtoenglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    return render_template('templates/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
