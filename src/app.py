from flask import Flask, render_template, request, redirect, url_for, make_response
from markupsafe import escape
import scraper
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.post('/results')
def results():
    url = request.form['url']
    data = fetchData(url)
    return render_template("result.html", 
                           dbaurl=escape(url),
                           numPages=data['numberOfPages'], 
                           listings=data['listings'])

def fetchData(url):
    return scraper.scrapeUrl(url)

app.run(host="0.0.0.0", port=8080)