from flask import Flask

from resources.atis import atis_resource
from resources.auth import auth_resource
from resources.fields import fields_resource
from storage import db

app = Flask(__name__)
app.register_blueprint(atis_resource)
app.register_blueprint(auth_resource)
app.register_blueprint(fields_resource)

if __name__ == '__main__':
    db.connect()
    app.run()
