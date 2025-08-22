import uuid
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models.store import StoreModel
from schemas import StoreSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

bp = Blueprint("stores", __name__, description="Operations on stores")


@bp.route("/store/<string:store_id>")
class Store(MethodView):
    @bp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Store deleted."}


@bp.route("/store")
class StoreList(MethodView):
    @bp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @bp.arguments(StoreSchema)
    @bp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A store with that name already exists.")
        except SQLAlchemyError:
            abort(500, "An error occurred while creating the store.")
        return store
