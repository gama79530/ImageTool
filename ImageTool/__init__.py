from flask import Flask
import click
from flask.cli import with_appcontext
import os

def create_app(test_config=None) :
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        INSTANCE_PATH = app.instance_path,
        IMG_DATABASE_PATH = os.path.join(app.instance_path, 'database')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'
        
    app.cli.add_command(init_img_db_cmd)

    from .blueprints import uploader
    app.register_blueprint(uploader.bp)
    app.add_url_rule('/', endpoint='')

    return app

@click.command('init-img-db')
@with_appcontext
def init_img_db_cmd() :
    from .widgts.IRE_Keras import index
    index.init_img_db()
    click.echo('Initialized the img database.')
    