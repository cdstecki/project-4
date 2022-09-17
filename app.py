from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/salary_db")
db = mongodb_client.db



@app.route("/get_object", methods=['POST', 'GET'])
def get_object():
    rows = []                               # define an empty list
    cursor = object_collection.find({},{ "_id": 1 })
    for document in cursor:
        rows.append(document['Location'])        # <- append to the list

    return render_template("get_object.html", rows=rows)  # Use the whole list in output


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")