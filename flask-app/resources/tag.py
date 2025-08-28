from http import HTTPStatus
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import db
from models import TagModel, StoreModel
from models.item import ItemModel
from schemas import TagAndItemSchema, TagSchema
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint("tags", __name__, description="Operations on tags")


@bp.route("/store/<string:store_id>/tag")
class TagInStore(MethodView):
    @bp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()

    @bp.arguments(TagSchema)
    @bp.response(201, TagSchema)
    def post(self, tag_data, store_id):
        if TagModel.query.filter(
            TagModel.store_id == store_id, TagModel.name == tag_data["name"]
        ).first():
            abort(400, message="A tag with that name already exists in that store.")

        tag = TagModel(**tag_data, store_id=store_id)

        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return tag


@bp.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagsToItem(MethodView):
    @bp.response(HTTPStatus.CREATED, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.append(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message="An error occurred while inserting the tag.")
        return tag

    @bp.response(HTTPStatus.OK, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the tag.")

        return {"message": "Item removed from the tag.", "item": item, "tag": tag}


@bp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @bp.response(200, TagSchema)
    def get(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        return tag

    @bp.response(
        HTTPStatus.ACCEPTED,
        description="Deletes a tag if no item is tagged with it.",
        example={"message": "Tag deleted."},
    )
    @bp.alt_response(HTTPStatus.NOT_FOUND, description="Tag not found.")
    @bp.alt_response(
        HTTPStatus.BAD_REQUEST,
        description="Returned if t he tag is assigned to one or more items. In this case, the tag is not deleted",
    )
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)

        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message": "Tag deleted."}

        abort(
            HTTPStatus.BAD_REQUEST,
            message="Could not delete tag. Make sure tag is not associated with any items, then try again.",
        )
