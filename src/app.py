from flask import Flask, render_template, request, make_response
from markupsafe import escape
import scraper

# TODO: add error handling 

app = Flask(__name__, static_url_path="/static")

@app.route('/', methods=["GET","POST"])
def index():
    # if request.method == "POST":
    #     keywords.append(request.form['keyword'])
    keywords = []
    if request.cookies.get("keywords"):
        keywords = request.cookies.get("keywords").split(",")
    resp = make_response(render_template("index.html", keywords=keywords))
    return resp

"""
Server will collect all data from url and send all to client.
Client will then do sorting and filtering on that data 
"""
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