from flask import Flask

def create_app(env):
    app = Flask(__name__)

    from src.config import app_config
    app.config.from_object(app_config[env])

    from src import api_bp
    app.register_blueprint(api_bp)

    from src.models import db
    db.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app("production")
    app.run()