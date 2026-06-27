🚀 API Flask com CI/CD Completo (GitHub Actions + Pytest + Render)

Este projeto é uma API desenvolvida em Flask (Python) com pipeline completo de CI/CD, incluindo:

Integração contínua com GitHub Actions
Testes automatizados com pytest
Deploy contínuo na Render
🧠 Objetivo do projeto

Demonstrar um fluxo real de DevOps moderno, onde cada alteração no código passa por validação automática antes de ir para produção.

⚙️ Arquitetura do CI/CD
Developer
   ↓ (git push)
GitHub Repository
   ↓
GitHub Actions (CI)
   ├── instala dependências
   ├── executa pytest
   ├── valida código
   ↓ (se aprovado)
Render (CD - deploy automático)
   ↓
API atualizada em produção 🚀
🧪 Pipeline de CI (GitHub Actions)

O pipeline executa automaticamente:

Instalação de dependências
Execução dos testes com pytest
Validação do código antes do deploy
Exemplo:
- name: Install dependencies
  run: pip install -r requirements.txt

- name: Run tests
  run: pytest
🧪 Testes (pytest)

Os testes garantem que a API está funcionando corretamente antes do deploy.

Exemplo de teste:
from main import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "API ok"
🔁 Fluxo completo
git push
   ↓
GitHub Actions (pytest roda automaticamente)
   ↓
Se testes PASSAREM ✅
   ↓
Render faz deploy automático
   ↓
API atualizada em produção 🚀
📁 Estrutura do projeto
api-flask/
│
├── main.py
├── test_main.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── README.md
└── .gitignore
🚀 Tecnologias utilizadas
Python 3
Flask
Pytest
Git & GitHub
GitHub Actions (CI)
Render (CD)
Gunicorn
🌐 Deploy

A API está hospedada na Render:

👉 https://sua-api.onrender.com

📌 Exemplo de endpoint
GET /
{
  "status": "success",
  "message": "API rodando com CI/CD completo e testes automatizados"
}
📈 O que este projeto demonstra

✔ CI/CD real funcionando ponta a ponta
✔ Testes automatizados com pytest
✔ Integração GitHub Actions
✔ Deploy contínuo na Render
✔ Boas práticas de DevOps
✔ Projeto pronto para portfólio profissional

🔮 Próximos passos (nível avançado)
Adicionar coverage (pytest-cov)
Adicionar lint (flake8 / ruff)
Criar Dockerfile
Migrar deploy para AWS
Adicionar monitoramento e logs
👨‍💻 Autor

João Carvalho
Foco em DevOps, automação, CI/CD e backend com Python
