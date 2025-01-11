from flask import Flask, render_template
from flower_db import *

app = Flask(__name__)

@app.route('/')
def index():
    flowers = get_all_flowers()
    return render_template('index.html', flowers=flowers)

app.run()
