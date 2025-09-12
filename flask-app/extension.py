from flask import jsonify
from flask_jwt_extended import JWTManager
from flask import current_app as app

from blocklist import BLOCKLIST

jwt = JWTManager()


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):  # type: ignore
    return jwt_payload["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token has been revoked.", "error": "token_revoked"}
        ),
        401,
    )


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify(
        {"description": "The token is not fresh.", "error": "fresh_token_required"},
        401,
    )


@jwt.additional_claims_loader
def add_claims_to_jwt(identity: str):
    app.logger.info("identity: ", identity)
    if identity == "1":
        return {"is_admin": True}
    return {"is_admin": False}


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):  # noqa: F811
    return jsonify({"message": "The token has expired.", "error": "token_expired"}), 401


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
