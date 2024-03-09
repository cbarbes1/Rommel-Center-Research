from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase?serverSelectionTimeoutMS=5000"
mongo = PyMongo(app)

@app.route('/')
def index():
    user_collection = mongo.db.users
    user_collection.insert_one({'name':'John Doe', 'age':30})
    users = list(user_collection.find({}, {'id': 0}))
    return render_template('templates/users.html')

if __name__ == '__main__':
    app.run(debug=True)
