"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """cupcake model"""
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(25), nullable=False)
    size = db.Column(db.String(15), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    image = db.Column(db.Text(), nullable=True, default='https://tinyurl.com/demo-cupcake')
