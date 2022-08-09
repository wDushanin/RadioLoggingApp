import os 
from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Log
from webforms import SearchForm

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)

@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@app.get('/')
def index():
    #Get Logs from Database
    logs = Log.query.all()
    return render_template('index.html', logs=logs)

# Create Search Function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    logs = Log.query
    if form.validate_on_submit():
        result = form.searched.data
        #Query the Database
        logs = logs.filter(Log.source_id.like(result))
        logs = logs.order_by(Log.time).all()
        return render_template("search.html", form=form, searched=result, logs=logs)
