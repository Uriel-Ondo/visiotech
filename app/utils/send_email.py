import smtplib
import os
import logging
from email.message import EmailMessage
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration du logger
LOG_FILE = "logs/email_errors.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Définition des serveurs SMTP
SMTP_SERVERS = {
    "amen": {
        "server": os.getenv("SMTP_SERVER_AMEN"),
        "port": int(os.getenv("SMTP_PORT_AMEN")),
        "user": os.getenv("SMTP_USER_AMEN"),
        "password": os.getenv("SMTP_PASS_AMEN"),
        "use_ssl": True
    },
    "gmail": {
        "server": os.getenv("SMTP_SERVER_GMAIL"),
        "port": int(os.getenv("SMTP_PORT_GMAIL")),
        "user": os.getenv("SMTP_USER_GMAIL"),
        "password": os.getenv("SMTP_PASS_GMAIL"),
        "use_ssl": False
    }
}

# Liste des destinataires
RECIPIENTS = [
    "contact@visiotech.me",
    "nick@visiotech.me",
    "uriel@visiotech.me",
    "nickalix2@gmail.com",
    "ondondoutoumouuriel@gmail.com"
]

def send_email(subject, text_body, html_body, sender="contact@visiotech.me", primary_provider="amen"):
    """Envoie un email en format HTML et texte brut, avec fallback SMTP"""
    providers = ["amen", "gmail"]
    providers.remove(primary_provider)
    providers.insert(0, primary_provider)

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = ", ".join(RECIPIENTS)
    msg["Subject"] = subject
    msg.set_content(text_body)  # Version texte brut
    msg.add_alternative(html_body, subtype="html")  # Version HTML

    for provider in providers:
        smtp_config = SMTP_SERVERS[provider]
        try:
            if smtp_config["use_ssl"]:
                server = smtplib.SMTP_SSL(smtp_config["server"], smtp_config["port"])
            else:
                server = smtplib.SMTP(smtp_config["server"], smtp_config["port"])
                server.starttls()

            server.login(smtp_config["user"], smtp_config["password"])
            server.send_message(msg)
            server.quit()
            print(f"✅ Email envoyé avec succès via {provider.upper()} !")
            return True

        except Exception as e:
            error_message = f"❌ Erreur avec {provider.upper()} : {e}"
            logging.error(error_message)
            print(error_message)

    print("🚨 Échec total : Aucun fournisseur SMTP n'a réussi à envoyer l'email.")
    return False
