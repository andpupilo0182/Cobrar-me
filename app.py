from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'appdata'
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/appdata'
mongo = PyMongo(app)

#lista todos os usuarios do mongodb
@app.route('/api/users/lista', methods=['GET'])
def get_all_users():
  user = mongo.db.usuarios
  output = []
  for s in user.find():
    output.append({'nome' : s['nome'], 'valor' : s['valor']})
  return jsonify({'resultado' : output})

#cadastra o usuario no mongodb
@app.route('/api/users/cadastra', methods=['POST'])
def add_user():
  user = mongo.db.usuarios
  nome = request.json['nome']
  valor = request.json['valor']
  user_id = user.insert({'nome': nome, 'valor': valor})
  new_user = user.find_one({'_id': user_id })
  output = {'nome': nome, 'valor': valor}
  return jsonify({'Usuario cadastrado' : output})

if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
