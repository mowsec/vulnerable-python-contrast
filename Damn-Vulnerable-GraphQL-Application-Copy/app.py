import config
import sys

from os import urandom
from core.helpers import initialize
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import contrast
from contrast.flask import ContrastMiddleware

app = Flask(__name__, static_folder="static/")
app.wsgi_app = ContrastMiddleware(app)
app.secret_key = urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["UPLOAD_FOLDER"] = config.WEB_UPLOADDIR

db = SQLAlchemy(app)

if __name__ == '__main__':
  sys.setrecursionlimit(100000)
  initialize()
  from core.views import *
  app.run(debug = config.WEB_DEBUG,
          host  = config.WEB_HOST,
          port  = config.WEB_PORT,
          threaded=True,
          use_evalex=False)
