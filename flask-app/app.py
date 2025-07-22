from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{"name": "My store", "items": [{"name": "chair", "price": 15.99}]}]


@app.get("/stores")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store), 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    print(f"Creating item in store: {name} with data: {request_data}")
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return {"message": "store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_score(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"], "message": "items found"}, 200
    return {"message": "store not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)
