from googleapiclient.discovery import build
from flask import Flask, render_template, url_for, flash, redirect
import os
import requests
import random
from forms import SearchForm, RegistrationForm, LoginForm


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

api_key = 'AIzaSyD2tUZp7juaZ_8z1yo6p7BxftxEAdO4z_Y'
'''
req = youtube.search().list(q="Drake" , part="snippet", type="video", maxResults=1)
res = req.execute()
'''

countries = ["Chinese", "Japanese", "turn_up","Mexican", "French", "Russian", "Korean", "yikes" , "Indian", "Spanish", "African", "Veggie Tales"]

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
    #  flash(f'Genre is {form.genre.data}!', 'success')

      youtube = build('youtube', 'v3', developerKey=api_key)

      song_genre = f'{form.genre.data}'
      secure_random = random.SystemRandom()
      country = secure_random.choice(countries)

      print(country + " " + song_genre)
      search_response = youtube.search().list(
              q = song_genre + " in " + country,
              part = "snippet",
              type = "video",
              order = "viewCount",
              maxResults=1,
            ).execute()

      vid_id = search_response['items'][0]['id']['videoId']
      title = search_response['items'][0]['snippet']['title']

      results = {
        'search_response' : search_response,
        'vidId':vid_id,
        'title':title,
        'genre':song_genre,
        'country':country,
      }

      if country == "Veggie Tales":
        return redirect(url_for('result', song_genre="qbw4nsNpqzA", country="farmville", name="EASTER EGG"))
      elif country == "yikes":
          return redirect(url_for('result', song_genre="I1ZEf032A1w", country="just enjoy", name="EASTER EGG"))
      elif country == "turn_up":
          return redirect(url_for('result', song_genre="VWoIpDVkOH0", country="GET LOW", name="BUST IT DOWN"))
      elif country in countries:
        return redirect(url_for('result', song_genre=results["vidId"], country=country, name=title))
    
    return render_template('home.html', title='Home', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been logged in! :)', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


@app.route("/result/<string:song_genre>/<string:country>/<string:name>")
def result(song_genre, country, name):
    return render_template('result.html', title='Result', song_genre=song_genre, country=country, name=name)

if __name__ == '__main__':
    app.run(debug=True)
