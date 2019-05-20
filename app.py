from googleapiclient.discovery import build
from flask import Flask, render_template, url_for

app = Flask(__name__)

api_key = 'AIzaSyD2tUZp7juaZ_8z1yo6p7BxftxEAdO4z_Y'
youtube = build('youtube', 'v3', developerKey=api_key)
req = youtube.search().list(q="Drake" , part="snippet", type="video", maxResults=1).execute()

video_id = req['items'][0]['id']['videoId']

videoData = {
   # 'artist' : self.request.get('artist'),
    #'country' : self.request.get('country'),
    'search_response' : req,
    'vidId': video_id
  #  'title':title
}
@app.route("/")
def hello():
    return render_template('home.html', videoData=videoData)

