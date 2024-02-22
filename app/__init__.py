from flask import Flask
# Additional Imports
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Flask-Mail configurations
app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'ca1c6502925d3d'
app.config['MAIL_PASSWORD'] = 'd2f1e6ea7b58e2'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Debug mode for Flask-Mail
app.config['MAIL_DEBUG'] = True

mail = Mail(app)
from app import views