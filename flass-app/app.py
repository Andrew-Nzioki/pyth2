from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

stores = [
    {'id': 1,
     'name': "store1",
     'items': [
             {'name': "Item1",
              'price': 15.99},
         {'name': "Item3",
                 'price': 15.30},
         {'name': "Item4",
                 'price': 15.00}
     ]
     },
    {'id': 2,
        'name': "store2",
        'items': [
            {'name': "Item2",
             'price': 15.00},
            {'name': "Item3",
                'price': 15.00},
            {'name': "Item4",
                'price': 15.00}
        ]
     }
]

@app.route('/')
def home():
    render_template('index.html')
# POST /store/<string :name


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>


@app.route("/store/<string:name>")
def get_store(name):
    # iterate over store
    for store in stores:
        # if the store name matches ,return it
        if store['name'] == name:
            return jsonify(store)
    # if none match, return error message
    return jsonify({'message': 'store not found'})

# Get /store


@app.route("/store")
def get_stores():
    return jsonify({"stores": stores})

# POST /store/<string:name>/item{name:,price:}


@app.route(f"/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data['name'],
                "price": request_data['price']}
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({"message": "store not found"})


# GET /store/<string:name>/item


@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store["items"])
    return jsonify({"message": "items not found"})


app.run(port=5000)
