from flask import Flask, render_template, request
from markupsafe import escape
import scraper

# TODO: add error handling 

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
                           listings=data['listings'],
                           numListings=len(data['listings']))

def fetchData(url):
    return scraper.scrapeUrl(url)

app.run(host="0.0.0.0", port=8080)