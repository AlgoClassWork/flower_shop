from flask import Flask, render_template, request, redirect, url_for
from flower_db import *

app = Flask(__name__)

@app.route('/')
def index():
    flowers = get_all_flowers()
    return render_template('index.html', flowers=flowers)

@app.route('/flower/<int:flower_id>')
def flower_detail(flower_id):
    flower = get_flower_by_id(flower_id)
    if flower:
        return render_template('flower_detail.html', flower=flower)
    else:
        return "Цветок не найден", 404


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        flower_id = request.form.get('flower_id')
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        image_path = request.form.get('image_path')
        action = request.form.get('action')

        if action == 'add':
            add_flower(name, description, price, quantity, image_path)
        elif action == 'edit':
            update_flower(name, description, price, quantity, image_path, flower_id)
        elif action == 'delete':
            delete_flower(flower_id)

        return redirect(url_for('admin'))

    flowers = get_all_flowers()
    return render_template('admin.html', flowers=flowers)


app.run(debug=True)
