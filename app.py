from flask import Flask


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:example@127.0.0.1:3307/Oknoaz"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "9fbc546684f5d7800067528c0b579c06"


from core.controllers import core as core_bp
from extensions import *


if __name__ == "__main__":

    from core.models import *

    app.register_blueprint(core_bp)
    app.run(port=4000, debug=True)
    