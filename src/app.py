from flask import Flask, render_template, request, redirect, url_for, make_response
from markupsafe import escape
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.post('/fetch')
def postFetch():
    url = request.form['url']
    response = make_response(redirect(url_for("results")))
    response.set_cookie('url', url)
    return response

@app.route('/results')
def results():
    url = request.cookies.get('url')
    return render_template("result.html", dbaurl=escape(url))

app.run(host="0.0.0.0", port=8080)