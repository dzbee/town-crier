from flask import Flask
from flask_bootstrap import Bootstrap

from services.index import register_index_endpoints
from services.encounter import register_encounter_endpoints

def initialize_app(testing=False):
    app = Flask(__name__)
    if testing:
        app.config['SECRET_KEY'] = 'testing'

    Bootstrap(app)

    register_index_endpoints(app)
    register_encounter_endpoints(app)

    return app

if __name__ == '__main__':
    initialize_app(testing=True).run()
