from flask import Flask, render_template, request
from gtts import gTTS
import os
import time  # NEW: To generate a unique file name

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/pronounce', methods=['POST'])
def pronounce():
    word = request.form.get('word')
    language = request.form.get('language', 'en')  # Default to English

    if not word:
        return "No word provided", 400

    try:
        # Generate a unique filename using timestamp
        timestamp = int(time.time())
        audio_file = f"static/pronunciation_{timestamp}.mp3"

        # Convert text to speech
        tts = gTTS(text=word, lang=language)
        tts.save(audio_file)

        return render_template('index.html', audio_file=audio_file)
    except ValueError:
        return "Error: Language not supported", 400


if __name__ == '__main__':
    app.run(debug=True)
