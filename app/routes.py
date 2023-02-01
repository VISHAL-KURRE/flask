from app import app
from flask import Flask, render_template

from . import templates




@app.route('/')
def index():
    return render_template('templates/index.html')
