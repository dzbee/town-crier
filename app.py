from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from config import Config

from services.index import register_index_endpoints
from services.encounter import register_encounter_endpoints
from services.character import register_character_endpoints

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
Migrate(app, db)
Bootstrap(app)

register_index_endpoints(app)
register_encounter_endpoints(app)
register_character_endpoints(app)

if __name__ == '__main__':
    app.run()
