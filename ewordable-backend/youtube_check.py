from collections.abc import MutableMapping
from youtube_transcript_api import YouTubeTranscriptApi

tx = YouTubeTranscriptApi.get_transcript('Z6nkEZyS9nA')

for i in tx:
   print(i['text'])
