import os
from flask import Flask, abort, redirect, render_template, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)
#can also use: bcrypt.init_app(app)

db = SQLAlchemy(app)
#can also use: db.init_app(app)

#connecting to MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.get('/')
def index():
    return render_template('index.html')
