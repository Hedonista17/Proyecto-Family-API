"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure  # De esta forma importamos las funcionalidades para generar una id random o el apellido que siempre es el mismo 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")   # Añadimos esta var como dato-estructura fija del apellido 

member1 = {
    "id": jackson_family._generateId(),
    "first_name":"Jhon",
    "last_name":jackson_family.last_name,
    "age":33,
    "lucky_numbers":[7,13,22]
}

member2 = {
    "id": jackson_family._generateId(),
    "first_name":"Jane",
    "last_name":jackson_family.last_name,
    "age":35,
    "lucky_numbers":[10,14,3]
}

member3 = {
    "id": jackson_family._generateId(),
    "first_name":"Jimmy",
    "last_name":jackson_family.last_name,
    "age":5,
    "lucky_numbers":[1]
}
jackson_family.add_member(member1)  
jackson_family.add_member(member2)
jackson_family.add_member(member3)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()  # del archivo de datastructures - funcion 
    response_body = members
    if members == None:
        return jsonify({"msg": "Error al cargar la informacion","error":True}), 400

    return jsonify(response_body), 200


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member_by_id(member_id):
    response_body = jackson_family.get_member(member_id) # del archivo de datastructures - funcion 
    if response_body == None:
        return jsonify({"msg":"Error al cargar la informacion","error":True}), 400

    return jsonify(response_body), 200


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    response_body = {"delete_member":jackson_family.delete_member(member_id)} # del archivo de datastructures - funcion 
    if response_body == None:
        return jsonify({"msg":"Error al borrar miembro de la familia Jackson!","error":True}), 400

    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def add_member():
    request_body = request.json()
    if request_body == None:
        return jsonify({"msg":"Error al añadir miembro a la familia Jackson!","error":True}), 400
    jackson_family.add_member(request_body)  # del archivo de datastructures - funcion 
    response_body = ""
    return jsonify(response_body), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
