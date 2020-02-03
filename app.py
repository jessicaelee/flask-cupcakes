"""Flask app for Cupcakes"""
from flask import Flask, request, redirect, render_template, flash, jsonify
from models import Cupcake, db, connect_db
from cupcake_serialized import serialize_cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "sekrit key"

connect_db(app)
db.create_all()

@app.route('/api/cupcakes')
def all_cupcake_data():
    """get data about all cupcakes"""
    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def cupcake_data(cupcake_id):
    """get data about a single cupcake"""

    cupcake = Cupcake.query.get(cupcake_id)
    serialized = serialize_cupcake(cupcake)
    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """create a cupcake """

    # cupcake_obj = request.json["cupcake"]
    flavor = request.json['flavor']
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = serialize_cupcake(cupcake)

    return (jsonify(cupcake=serialized), 201)

