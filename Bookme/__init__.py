#! ../env/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Yasoob Khalid'
__email__ = 'yasoob.khld@gmail.com'
__version__ = '0.1'

from flask import Flask
from webassets.loaders import PythonLoader as PythonAssetsLoader

from Bookme import assets
from Bookme.models import db

from Bookme.extensions import (
    cache,
    assets_env,
    debug_toolbar,
    login_manager
)


def create_app(object_name, env="prod"):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. Bookme.settings.ProdConfig

        env: The name of the current environment, e.g. prod or dev
    """

    app = Flask(__name__)

    app.config.from_object(object_name)
    app.config['ENV'] = env

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().iteritems():
        assets_env.register(name, bundle)

    # register our blueprints
    from controllers.main import main
    from controllers.api import api

    app.register_blueprint(main)
    app.register_blueprint(api)

    return app
