from flask import Flask, abort, redirect, render_template, request

@app.get('/')
def index():
    return render_template('index.html')
