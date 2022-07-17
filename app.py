import os 
from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Log

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.get('/')
def index():
    logs = Log.query.all()
    return render_template('index.html', logs=logs)
