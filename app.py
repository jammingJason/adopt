
from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet
from forms import AddNewPet


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


@app.route('/')
def go_home():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/pets/new', methods=['GET', 'POST'])
def add_new_pet():
    """Add a new Pet"""
    form = AddNewPet()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        species = form.species.data
        image_url = form.image_url.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name, age=age, species=species,
                  image_url=image_url, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)


@app.route('/pets/<id>/edit', methods=['GET', 'POST'])
def edit_pet(id):
    """Edit a Pet"""
    pet = Pet.query.get(id)
    form = AddNewPet(obj=pet)
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        image_url = form.image_url.data
        notes = form.notes.data
        available = form.available.data
        edit_pet = Pet(id=id, name=name, species=species,
                       age=age, image_url=image_url, notes=notes, available=available)
        db.session.merge(edit_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit-pet.html', form=form, pet=pet)
