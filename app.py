from flask import Flask, request, send_file,jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://sathesiddhesh16:WhN3pbVrUq3NxTog@cluster0.ujgemdl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['portfolio_db']
collection = db['contacts']

@app.route('/')
def index():
    return render_template('index.html')   
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    print(data)
    collection.insert_one({
        'name': data['name'],
        'phone': data['number'],
        'address': data['address'],
        'email':data['email'],
        'message': data['message']
    })

    return send_file('./assets/img.png')
@app.route('/get')
def get():
    contacts = list(collection.find({}, {'_id': 0}))
    return jsonify(contacts)
if __name__ == '__main__':
    app.run(debug=True)