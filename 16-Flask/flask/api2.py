from flask import Flask,jsonify,request

app = Flask(__name__) ## created an WSGI application(interface between web server and flask based app)


##Initial Data 
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/',methods=['GET'])
def home():
    return "Welcome to the sample TO-DO-LIST app"

## GET : Retrieve all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items) ## jsonify() converts Python data (like dictionary or list) into JSON format and sends it as an HTTP response.

## GET : retrieve specefic element by id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_elementById(item_id):
    for item in items:
        if item['id'] == item_id: 
            return jsonify(item)
    return jsonify({"error":"item not found"})

## POST : create a new task 
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    else:
        new_item={
            "id" :items[-1]['id'] + 1 if items else 1,
            "name" : request.json["name"], ## response.json() is used to convert JSON data received from an API response into a Python dictionary or list.
            "description" : request.json['description']
        }
        items.append(new_item)
        return jsonify(new_item)
    
## PUT : Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    ## response.json().get() is used when you want to safely access a value from JSON response without causing an error if the key is missing.
    ## response.json().get('name') -> .If "name" does not exist → ✅ Returns None (safe)
    ## response.json()['name'] -> If "name" does not exist → ❌ Program crashes (KeyError)
    for item in items:
        if item["id"] == item_id:
            item["name"] = request.json.get("name",item["name"])
            item["description"] = request.json.get("description", item["description"])
            return jsonify(item)
    return jsonify({"error":"item not found"})

## DELETE : Delete an exisiting item
@app.route('/items/<int:item_id>',methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)