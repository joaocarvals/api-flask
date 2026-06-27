🚀 API Flask com CI/CD Completo (GitHub Actions + Pytest + Render)

Este projeto é uma API desenvolvida em Flask (Python) com pipeline completo de CI/CD, incluindo integração contínua, testes automatizados e deploy contínuo.

🧠 Objetivo do projeto

Demonstrar um fluxo real de DevOps moderno, onde cada alteração no código passa por validação automática antes de ser enviada para produção.

⚙️ Arquitetura do CI/CD
Developer
   ↓ git push
GitHub Repository
   ↓
GitHub Actions (CI)
   ├── instala dependências
   ├── executa pytest
   ├── valida código
   ↓ (se aprovado)
Render (CD - deploy automático)
   ↓
API em produção 🚀
🧪 CI - GitHub Actions

O pipeline de integração contínua executa automaticamente:

Instala dependências
Roda testes com pytest
Valida o código
Exemplo do workflow:
- name: Install dependencies
  run: pip install -r requirements.txt

- name: Run tests
  run: pytest
🧪 Testes (pytest)

Os testes garantem que a API funciona antes do deploy.

Exemplo:
from main import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "API ok"
🔁 Fluxo completo
git push
   ↓
GitHub Actions executa pytest
   ↓
Se PASSAR ✅
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
└── README.md
🚀 Tecnologias utilizadas
Python 3
Flask
Pytest
Git & GitHub
GitHub Actions (CI)
Render (CD)
Gunicorn
🌐 Deploy

API em produção:

👉 https://sua-api.onrender.com

📌 Exemplo de endpoint
GET /
{
  "status": "success",
  "message": "API rodando com CI/CD completo e testes automatizados"
}
📈 O que este projeto demonstra

✔ CI/CD funcionando de ponta a ponta
✔ Testes automatizados com pytest
✔ Integração GitHub Actions
✔ Deploy contínuo na Render
✔ Projeto pronto para portfólio DevOps

🔮 Próximos passos
Coverage com pytest-cov
Lint com ruff ou flake8
Dockerização da API
Deploy em AWS
Monitoramento e logs
👨‍💻 Autor

João Carvalho
Foco em DevOps, automação, CI/CD e backend com Python
