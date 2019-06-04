from flask import Flask
from app import configure_routes


def test_results():
    ''' Test the loading the results page on a youtube video ID works
    
    Parameters
    ----------
    None

    Return
    ------
    None
    '''

    #create instance of my app and register the routes
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    #test on specific route that the page loads with no error
    url = '/result/9_k_goMr5ZI/French/Drake'
    response = client.get(url)
    assert response.status_code == 200
