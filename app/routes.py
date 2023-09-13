from app import app, db
from flask import render_template, redirect, url_for, request, flash
from app.forms import PasswordGeneForm
from app.models import PasswordDatabase
from random import choice, shuffle
from string import ascii_lowercase
from string import ascii_uppercase

# choice lowercase depend on form
lowercases = [char for char in ascii_lowercase]
# choice uppercase depend on form
uppercases = [char for char in ascii_uppercase]
# choice symbols depend on form
syms = ['!', '#', '$', '%', '*']
# return new list 

def processed_pass(lowercase, uppercase, symbol):
    new_list = []
    for i in range(lowercase):
        new_list.append(choice(lowercases))
    for j in range(uppercase):
        new_list.append(choice(uppercases))
    for k in range(symbol):
        new_list.append(choice(syms))

    shuffle(new_list)
    return ''.join(new_list)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasswordGeneForm()
    if form.validate_on_submit():
        generate_pass = processed_pass(int(form.lowercase.data), int(form.uppercase.data), int(form.symbols.data)) 
        new_pass = PasswordDatabase(plain_password=generate_pass, save_for=form.save_for.data)
        db.session.add(new_pass)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('index.html', title="Password-Generator", form=form)