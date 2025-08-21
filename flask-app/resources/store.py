import uuid
from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

bp = Blueprint("stores", __name__, description="Operations on stores")


@bp.route("/store/<string:store_id>")
class Store(MethodView):
    @bp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(404, message="Store not found")


@bp.route("/store")
class StoreList(MethodView):
    @bp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()

    @bp.arguments(StoreSchema)
    @bp.response(200, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if (
                store_data["name"]
                == store["name" and store_data["store_id"] == store["store_id"]]
            ):
                abort(400, message="Store already exists ")

        store_id = uuid.uuid4().hex
        new_store = {**store_data, "id": store_id}
        stores[store_id] = new_store
        return new_store
