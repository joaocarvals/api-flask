from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien',
    },
    {
        'id': 2,
        'titulo': 'Homens de Preto',
        'autor': 'Jorge Abreu',
    },
    {
        'id': 3,
        'titulo': 'Big Mike',
        'autor': 'Joao Jones',
    }
]

#Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar um livro pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#Editar um livro pelo ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Cria um novo livro
@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

#Excluir um livro pelo ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros)

if __name__ == "__main__":
    app.run(port=5000, host="localhost", debug=True)

