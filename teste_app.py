from app import app

def test_obter_livros():
    response = app.test_client().get('/livros')
    assert response.status_code == 200
    assert len(response.get_json()) == 3

def test_obter_livro_por_id():
    response = app.test_client().get('/livros/1')
    assert response.status_code == 200
    assert response.get_json()['titulo'] == 'O Senhor dos Anéis'

def test_criar_livro():
    cliente = app.test_client()
    novo_livro = {
        'id': 4,
        'titulo': 'Novo Livro',
        'autor': 'Autor',
    }
    response = cliente.post('/livros', json=novo_livro)
    assert response.status_code == 201
    assert response.get_json() == novo_livro

def test_editar_livro():
    client = app.test_client()

    dados = {
        'titulo': 'Livro Editado',
        'autor': 'Autor Editado'
    }
    response = client.put('/livros/1', json=dados)
    assert response.status_code == 200
    livro = response.get_json()
    assert livro['titulo'] == 'Livro Editado'

