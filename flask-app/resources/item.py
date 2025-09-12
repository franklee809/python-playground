from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from schemas import ItemSchema, ItemUpdateSchema
from models import ItemModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

bp = Blueprint("items", __name__, description="Operations on items")


@bp.route("/item/<int:item_id>")
class Item(MethodView):
    @jwt_required()
    @bp.response(200, ItemSchema)
    def get(self, item_id):
        return ItemModel.query.get_or_404(item_id)

    @jwt_required()
    def delete(self, item_id):
        jwt = get_jwt()
        print(jwt)
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()

        return {"message": "Item deleted."}

    @jwt_required()
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
    @jwt_required()
    @bp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @jwt_required(fresh=True)
    @bp.arguments(
        ItemSchema,
    )
    @bp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            abort(500, description="An error occurred while inserting the item.")
        except IntegrityError as e:
            print(e)
            abort(400, description="An item with that name already exists.")

        return item


# @app.errorhandler(400)
# def custom400(error):
#     response = jsonify({"message": error.description})
#     response.status_code = 400
#     return response


# @app.errorhandler(500)
# def custom400(error):
#     response = jsonify({"message": error.description})
#     response.status_code = 500
#     return response
