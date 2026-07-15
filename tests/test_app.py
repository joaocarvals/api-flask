from main import app

client = app.test_client()

# Teste para consultar todos os livros

def test_obter_livros():
    response = client.get('/livros')

    assert response.status_code == 200
    assert len(response.get_json()) == 3


# Teste para consultar um livro pelo ID

def test_obter_livro_por_id():
    response = client.get('/livros/1')

    assert response.status_code == 200
    assert response.get_json()['titulo'] == 'O Senhor dos Anéis'


# Teste para criar um livro

def test_criar_livro():
    novo_livro = {
        'id': 4,
        'titulo': 'Novo Livro',
        'autor': 'Autor',
    }

    response = client.post('/livros', json=novo_livro)

    assert response.status_code == 201

    data = response.get_json()

    assert data['titulo'] == 'Novo Livro'
    assert data['autor'] == 'Autor'


# Teste para editar um livro pelo ID

def test_editar_livro():
    dados = {
        'titulo': 'Livro Editado',
        'autor': 'Autor Editado'
    }

    response = client.put('/livros/1', json=dados)

    assert response.status_code == 200

    livro = response.get_json()

    assert livro['titulo'] == 'Livro Editado'