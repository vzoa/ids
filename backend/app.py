from flask import Flask

from ids.resources.fields import fields_resource
from ids.storage import db

app = Flask(__name__)
app.register_blueprint(fields_resource)

if __name__ == '__main__':
    db.connect()
    app.run()
