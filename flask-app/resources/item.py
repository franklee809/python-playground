import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models.item import ItemModel
from schemas import ItemSchema, ItemUpdateSchema
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint("items", __name__, description="Operations on items")


@bp.route("/item/<string:item_id>")
class Item(MethodView):
    @bp.response(200, ItemSchema)
    def get(self, item_id):
        return ItemModel.query.get_or_404(item_id)

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}

    @bp.arguments(ItemUpdateSchema)
    @bp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)

        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item


@bp.route("/item")
class ItemList(MethodView):
    @bp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @bp.arguments(
        ItemSchema,
    )
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, "An error occurred while inserting the item.")

        return item, 201
