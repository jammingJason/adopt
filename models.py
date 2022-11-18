from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""
    __tablename__ = "pets"

    def __repr__(self):
        p = self
        return f"< Pet id = {p.id}, name = {p.name}, species = {p.species},image_url = {p.image_url}, age={p.age}, notes={p.notes}, available={p.available} >"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    species = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String(),
                      nullable=True)
    available = db.Column(db.Boolean(), nullable=False)
