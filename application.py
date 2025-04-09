from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import os
import secrets

app = Flask(__name__)
# Set the upload folder for images
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generates a 32-character random string
app.run(host='018.228.232.157', port=5000, debug=True)


# Sample house data (you can replace with a database later)
house = {
    'title': "Sobrado em Campo Grande - MS",
    'price': "Sob consulta",
    'address': "Rua Vitorio Zeolla, 608, Carandá Bosque, Campo Grande - MS",
    'bedrooms': 4,
    'bathrooms': 5,
    'area_cons': 400,
    'area_terr': 720,
    'description': """Casa recém reformada, no Bairro arandá Bosque, localizada na rua principal, bons restuarantes e escolas ao redor.
                    A casa possui 4 quartos, sendo 3 suítes, 5 banheiros, piscina, churrasqueira e uma área de lazer incrível. Ideal para famílias que buscam conforto e segurança.""",
    'year_built': 2018,
    'features': [
        "Piscina",
        "Smart home system",
        "Área de lazer",
        "Churrasqueira",
        "Gramado extenso",
        "Academia",
        "Escritório",
        "Garagem para 4 carros",
        "Jardim"

    ],
    'images': ['house1.jpg', 'house2.jpg', 'house3.jpg', 'house4.jpg']
}

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html', house=house)

@app.route('/details')
def details():
    return render_template('details.html', house=house)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Here you would typically send an email or save to database
        # For now, we'll just print to console
        print(f"New contact from: {form.name.data} ({form.email.data})")
        print(f"Message: {form.message.data}")
        return redirect(url_for('thank_you'))
    return render_template('contact.html', form=form, house=house)

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', house=house)

@app.route('/home')
def home():
    return redirect(url_for('index'))  # Redirect to the index page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)