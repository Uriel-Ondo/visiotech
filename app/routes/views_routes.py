from flask import Blueprint, render_template, flash, redirect, url_for
from app.routes.forms_routes import ContactForm
from app.utils.send_email import send_email
import os
import requests


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        subject = f"Nouveau message de {name} ({email})"
        text_body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        # Génération du mail en HTML
        html_body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <h2 style="color: #003366;">📩 Nouveau message reçu</h2>
                <p><strong>Nom:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Message:</strong></p>
                <p style="background: #f9f9f9; padding: 10px; border-radius: 5px;">{message}</p>
                <hr>
                <p style="text-align: center;">
                    <img src="http://138.197.19.186:8001/static/images/logo.jpg" alt="Visiotech" width="150">
                </p>
                <p style="text-align: center; font-size: 14px; color: #555;">
                    <strong>📞 +221 78 129 59 00 / +221 77 543 82 65</strong><br>
                    <strong>✉️ contact@visiotech.me</strong>
                </p>
            </div>
        </body>
        </html>
        """

        send_email(subject, text_body, html_body)

        flash("Votre message a été envoyé avec succès !", "success")
        return redirect(url_for('main.contact'))

    return render_template('contact.html', form=form)

@main.route('/services')
def services():
    return render_template('services.html', title='Services')

@main.route('/realisations')
def realisations():
    return render_template('realisations.html', title='Realisation')

