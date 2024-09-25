from flask import Flask,request,jsonify
#from youtube_transcript_api import YouTubeTranscriptApi as yta
from youtube_transcript_api import YouTubeTranscriptApi
from textblob import TextBlob
import numpy as np
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
import nltk
import pandas as pd
import io
import os
import unicodedata
import string
import glob
import random
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate('ewords-4e4f8-firebase-adminsdk-u8kct-3bc2f120d8.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

random_word = []

app_id = "c6e4e155"
app_key = "8e66c4be8437dbbd71d0c69465e22e9d"


ALL_LETTERS = string.ascii_letters + ".,;'"

app = Flask(__name__)


@app.route('/youtube-api-check', methods = ['GET'])
def get_articles():
    vid_id = "6ViGc5NgdSw"

    outls = []

    tx = YouTubeTranscriptApi.get_transcript('Z6nkEZyS9nA', languages=['en'])

    for i in tx:
        outtext = (i['text'])
        outls.append(outtext+"\n")



    ##data = yta.get_transcript(vid_id)

    ##return data
 #return jsonify({"Hello":"World"})


if __name__ == "__main__":



    app.run(host='0.0.0.0', port=5000)
