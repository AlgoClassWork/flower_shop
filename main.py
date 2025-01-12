from flask import Flask, render_template, request
from flower_db import *

app = Flask(__name__)

@app.route('/')
def index():
    flowers = get_all_flowers()
    return render_template('index.html', flowers=flowers)


@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        image_path = request.form.get('image_path')
        action = request.form.get('action')

        if action == 'add':
            add_flower(name, description, price, quantity, image_path)
        
    flowers = get_all_flowers()
    return render_template('admin.html', flowers=flowers)

app.run()
