from flask import render_template

def register_index_endpoints(app):

    @app.route('/')
    def index():
        return render_template('index.html')
