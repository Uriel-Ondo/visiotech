from flask import Blueprint, render_template, flash, redirect, url_for
from app.routes.forms_routes import ContactForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Logique pour traiter les données du formulaire, par exemple envoyer un email
        flash('Message envoyé avec succès!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', form=form)

@main.route('/services')
def services():
    return render_template('services.html', title='Services')
