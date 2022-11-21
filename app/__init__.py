from flask import Flask

from .config.environment import ProductionEnvironment
from .routes.index import blueprint as index

# FLASK RUN PATTERN
def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionEnvironment())
    app.register_blueprint(index)

    return app