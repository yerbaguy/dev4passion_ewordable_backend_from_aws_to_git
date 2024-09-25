import  YoutubeLoader  from "@langchain/community/document_loaders/web/youtube"

#import requests
#from youtube_transcript_api import YouTubeTranscriptApi

const loader = YoutubeLoader.createFromUrl("https://youtu.be/bZQun8Y4L2A", {
  language: "en",
  addVideoInfo: true,
});

const docs = await loader.load();

console.log(docs);
