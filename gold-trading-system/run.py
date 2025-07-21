from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from config.settings import Config

db = SQLAlchemy()
redis = Redis.from_url(Config.REDIS_URL)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.trading import trading_bp
    from app.routes.price import price_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(trading_bp, url_prefix='/api/trading')
    app.register_blueprint(price_bp, url_prefix='/api/price')

    return app

if __name__ == '__main__':
    app = create_app()
    import logging
    logging.basicConfig(filename='app.log', level=logging.INFO)
    app.run(debug=True)
