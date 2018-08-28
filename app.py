#from config import *
from flask import Flask, render_template,flash, redirect, request, url_for,jsonify
from models import *
import json, csv

from playhouse.dataset import DataSet

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    
    # data = new_table
    data = db['data']

    map_center = [37.770715, -122.433421]
    return render_template('index.html',geodata=data,centerLatlon=map_center)

if __name__ == '__main__':
    app.run(debug=True)