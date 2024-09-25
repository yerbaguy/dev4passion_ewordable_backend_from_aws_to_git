from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)


@app.route("/")
def Home():
    return "Home"

if __name__ == "__main__":
   # app.run(debug=True)
   app.run(host='0.0.0.0', port=5000)
