import requests
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
nasa_api_key = "YsD8TsWqhkTlB5hzRkuOa6fl173kYpKHTgmbHpBL"

@app.route('/')
def index():
    daterequested = request.args["date"]
    response = requests.get("https://api.nasa.gov/planetary/apod?date=" + daterequested + "&api_key=" + nasa_api_key)
    url = response.json()["url"]

    return render_template('index.html', landing_image=url, explanation=response.json()["explanation"],media_type=response.json()["media_type"])

@app.route('/mars')
def mars():
    response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=10&api_key=" + nasa_api_key)
    photoArray = response.json()["photos"]
    print(photoArray)
    return render_template('mars.html', photo_array=photoArray)