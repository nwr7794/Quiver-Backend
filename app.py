import json
from flask import Flask, Markup, request, redirect, render_template, jsonify
import requests
from datetime import date
import time
import os
import json
from flask_cors import CORS
from fred import Fred
import pandas as pd


#INIT THE CLIENT
API_KEY = os.environ.get('FRED_API_KEY')
fr = Fred(api_key=API_KEY,response_type='json')

#creates instance of app
app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)

@app.route("/")
def pingroute():

    return 'OK'    

@app.route("/retrievedata")
def retrieveData():

    return(fr.category.details(97))

@app.route("/fredsearch")
def fredsearch():

    return 'Search results'    

#instantiate app
if __name__ == "__main__":
    app.run(debug=True, port=3000)