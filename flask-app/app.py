import os
from flask import Flask, json, jsonify
from flask_smorest import Api
from resources.item import bp as ItemBlueprint
from resources.store import bp as StoreBlueprint
from resources.tag import bp as TagBlueprint
from resources.user import bp as UserBlueprint
from flask_jwt_extended import JWTManager
import models
import secrets
from db import db


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)
    jwt = JWTManager(app)

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity: str):
        app.logger.info("identity: ", identity)
        if identity == "1":
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify(
            {"message": "The token has expired.", "error": "token_expired"}
        ), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify(
            {
                "message": "Request does not contain an access token.",
                "error": "authorization_required",
            }
        ), 401

    app.config["JWT_SECRET_KEY"] = "7#\xce\x17i1\xa0\xde\xba\x854,\xe1\x10$\xba"
    # app.config["JWT_SECRET_KEY"] = (
    #     secrets.SystemRandom().getrandbits(128).to_bytes(16, "big")
    # )
    print(app.config["JWT_SECRET_KEY"])

    with app.app_context():

        def create_tables():
            db.create_all()

        create_tables()
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    return app
