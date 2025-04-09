from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__,
                template_folder='../temmplates',
                static_folder='../static')
    app.config.from_object(config_class)

    # Resgistrar rutas
    from app.routers import bp as routers_bp
    app.register_blueprint(routers_bp)

    # Crear directorios si no existen
    import os
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    if not os.path.exists(app.config['DOWNLOAD_FOLDER']):
        os.makedirs(app.config['DOWNLOAD_FOLDER'])

    return app
