video_url = "https://www.youtube.com/watch?v=RMFOXVh9uqg"
#from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress

from youtube_transcript_api import YouTubeTranscriptApi

try:
    #yt = YouTube(video_url)
    yt = YouTube(video_url, on_progress_callback = on_progress, use_po_token = True )
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download()
    video_id = video_url.split("v=")[1]
    tanscripts = YouTubeTranscriptApi.get_transcript(video_id)

    if transcripts:
        subtitle_text = "".join([entry["text"] for entry in transcripts ])

        print("transcripts")
        print(subtitle_text)

    else:
        print("transcripts not available")


except Exception as e:
    print(f"error occured: {str(e)}")
