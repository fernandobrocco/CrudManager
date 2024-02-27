#Create, Read, Update, Delete
from flask import Flask, request,jsonify

app = Flask(__name__)

database=[]

# create the new school subject
@app.route("/subject",methods=["POST"])
def create_subject():
    data = request.get_json()
    subject = {
        'name': data['name'],
        'professor': data['professor'],
        'number': data['number']
    }
    database.append(subject)
    return jsonify({"message":"This subject was included successfully!"}),201

# read all the subjects
@app.route("/subject",methods=["GET"])
def read_subjects():
    return jsonify(database)

# update a subject
@app.route("/subject/<string:name>",methods=["PUT"])
def update_subject(name):
    data = request.get_json()
    for subject in database:
        if subject['name'] == name:
            subject['professor'] = data['professor']
            subject['number'] = data['number']
            return jsonify({'message':'Subject actualized successfully!'}),201
    return jsonify ({'message':'Subject not found'}),404

# delete a subject
@app.route('/subject/<string:name>',methods=["DELETE"])
def delete_subject(name):
    for index,subject in enumerate(database):
        if subject['name'] == name:
            database.pop(index)
            return jsonify({'message':'Subject deleted successfully!'}),200
    return jsonify({'message':'Subject not founded'}),404

# run the utfpr manager
if __name__ == "__main__":
    app.run(debug=True)
