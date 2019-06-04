from googleapiclient.discovery import build
from flask import Flask, render_template, url_for, flash, redirect
import os
import requests
import random
from forms import SearchForm, RegistrationForm, LoginForm


app = Flask(__name__)
SECRET_KEY = os.urandom(32)

#Personal YouTube developer API key to use their API
app.config['SECRET_KEY'] = SECRET_KEY
api_key = 'AIzaSyD2tUZp7juaZ_8z1yo6p7BxftxEAdO4z_Y'

#list of youtube search queries and easter eggs
countries = ["Chinese", "Japanese", "turn_up","Mexican", "French", "Russian", "Korean", "yikes" , "Indian", "Spanish", "African", "Veggie Tales"]


def configure_routes(app):
    '''Registers the routes of my application
    
    Parameters
    ----------
    app: Flask app
        instance of my app
    
    Return
    ------
    None
    '''
    
    #displays the home page
    @app.route("/", methods=['GET', 'POST'])
    @app.route("/home", methods=['GET', 'POST'])
    def home():
        '''Renders the home page and generates the search query based on user input

        Paramters
        ---------
        None

        Returns
        -------
        redirect: function call
            redirects/renders the 'results' template page based on user input
        
        '''
        #create user input form
        form = SearchForm()

        #handle user interaction with application
        if form.validate_on_submit():

            youtube = build('youtube', 'v3', developerKey=api_key)
            
            #pick a random country and store user input
            song_genre = f'{form.genre.data}'
            secure_random = random.SystemRandom()
            country = secure_random.choice(countries)

            #call the YouTube API with given input
            search_response = youtube.search().list(
                    q = song_genre + " in " + country,
                    part = "snippet",
                    type = "video",
                    order = "viewCount",
                    maxResults=1,
                    ).execute()
            
            #go through API result and parse essential video data
            vid_id = search_response['items'][0]['id']['videoId']
            title = search_response['items'][0]['snippet']['title']
            results = {
                'search_response' : search_response,
                'vidId':vid_id,
                'title':title,
                'genre':song_genre,
                'country':country,
            }
            
            #handle easter eggs in and redirect to results page passing in the video data based on user input 
            if country == "Veggie Tales":
                return redirect(url_for('result', song_genre="qbw4nsNpqzA", country="farmville", name="EASTER EGG"))
            elif country == "yikes":
                return redirect(url_for('result', song_genre="I1ZEf032A1w", country="just enjoy", name="EASTER EGG"))
            elif country == "turn_up":
                return redirect(url_for('result', song_genre="VWoIpDVkOH0", country="GET LOW", name="BUST IT DOWN"))
            elif country in countries:
                return redirect(url_for('result', song_genre=results["vidId"], country=country, name=f'{form.genre.data}'))
        
        return render_template('home.html', title='Home', form=form)


    @app.route("/register", methods=['GET', 'POST'])
    def register():
        '''Renders the user registration page and notifies user if they successfully registered

        Paramters
        ---------
        None

        Returns
        -------
        redirect: function call
            redirects/renders the 'register' template page
        
        External Code: External Code used from CoreyMSchafer 'Python Flask Tutorial'
        '''
        #create user input form
        form = RegistrationForm()

        #check if user successfully registered and redirect to home page
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form)


    @app.route("/login", methods=['GET', 'POST'])
    def login():
        '''Renders the user login page and notifies user if they successfully logged in

        Paramters
        ---------
        None

        Returns
        -------
        redirect: function call
            redirects/renders the 'login' template page 

        External Code: External Code used from CoreyMSchafer 'Python Flask Tutorial'
        '''
        #create user input form
        form = LoginForm()

        #check if user succesfully logged in and redirect to home page
        if form.validate_on_submit():
            flash('You have been logged in! :)', 'success')
            return redirect(url_for('home'))
        return render_template('login.html', title='Login', form=form)


    @app.route("/result/<string:song_genre>/<string:country>/<string:name>")
    def result(song_genre, country, name):
        '''Renders the results page for the user to play music

        Paramters
        ---------
        song_genre: string
            song's music genre
        country: string
            randomly chosen country name or easter egg 
        name: string
            name of the song returned by YouTube API

        Returns
        -------
        redirect: function call
            redirects/renders the 'result' template page 
        
        '''
        return render_template('result.html', title='Result', song_genre=song_genre, country=country, name=name)

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
