from flask import Flask

app = Flask(__name__)

from app.models import Sender
sender = Sender()

from app import views