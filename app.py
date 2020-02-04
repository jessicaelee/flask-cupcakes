"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template, flask_cors
from flask_cors import CORS
from models import Cupcake, db, connect_db
# from cupcake_serialized import serialize_cupcake

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "sekrit key"
app.config['CORS_HEADERS'] = 'Content-Type'

# cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})


connect_db(app)
db.create_all()

@app.route('/')
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def show_home_page():
    return render_template('home.html')

@app.route('/api/cupcakes')
def all_cupcake_data():
    """get data about all cupcakes"""
    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def cupcake_data(cupcake_id):
    """get data about a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()
    return jsonify(cupcake=serialized)

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """create a cupcake """

    flavor = request.json.get('flavor')
    size = request.json.get("size")
    rating = request.json.get("rating")
    image = request.json.get("image") or None

    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """update a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor') or cupcake.flavor
    cupcake.size = request.json.get("size") or cupcake.size
    cupcake.rating = request.json.get("rating") or cupcake.rating
    cupcake.image = request.json.get("image") or cupcake.image or None
    
    serialized = cupcake.serialize()

    db.session.commit()

    return jsonify(cupcake=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """get data about a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify({"message": "Deleted"})
