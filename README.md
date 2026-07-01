🚀 Flask DevOps Project

📖 Sobre o projeto

Este projeto foi desenvolvido para praticar e demonstrar conceitos de DevOps utilizando uma aplicação Flask simples.

O objetivo é construir um fluxo moderno de desenvolvimento, passando pela criação da aplicação, containerização, infraestrutura como código, orquestração e automação de deploy.

🛠️ Tecnologias
Python
Flask
Docker
Kubernetes
Terraform
GitHub Actions
Git
Render

📂 Estrutura do projeto
api-flask/
│
├── .github/
│   └── workflows/
│       └── pipeline.yaml
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   └── main.tf
│
├── Dockerfile
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

🏗️ Arquitetura
                GitHub
                   │
                   ▼
         GitHub Actions (CI/CD)
                   │
          Build + Validation
                   │
                   ▼
             Docker Image
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
   Kubernetes            Render
      Cluster             Deploy

🚀 Como executar
1. Clonar o projeto
git clone https://github.com/joaocarvals/api-flask

cd api-flask
2. Criar ambiente virtual
Windows
python -m venv venv

venv\Scripts\activate
Linux/macOS
python3 -m venv venv

source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
4. Executar a aplicação
python main.py

A aplicação ficará disponível em:

http://localhost:5000
🐳 Docker
Build
docker build -t flask-api .
Executar
docker run -p 5000:5000 flask-api
☸️ Kubernetes

Aplicar Deployment

kubectl apply -f k8s/deployment.yaml

Aplicar Service

kubectl apply -f k8s/service.yaml

Verificar pods

kubectl get pods

Verificar serviços

kubectl get svc
🌍 Terraform

A infraestrutura está sendo criada utilizando o provider Docker do Terraform.

Atualmente o projeto possui:

Estrutura inicial criada
Provisionamento de imagem Docker
Ajustes finais em andamento

Após finalizado será possível executar:

terraform init

terraform plan

terraform apply
🔄 Pipeline CI/CD

O projeto utiliza GitHub Actions para automatizar o fluxo de integração contínua.

Fluxo atual:

Checkout do código
Instalação das dependências
Build da aplicação
Build da imagem Docker
Deploy automatizado
🎯 Objetivos de aprendizado
✅ Desenvolvimento de APIs REST
✅ Dockerização de aplicações
✅ Kubernetes
✅ GitHub Actions
🔄 Terraform
🔄 Deploy automatizado
🔄 Cloud Computing
🚧 Roadmap

Criar API Flask

Criar Dockerfile

Configurar GitHub Actions

Criar Deployment Kubernetes

Criar Service Kubernetes

Finalizar Terraform

Adicionar testes automatizados

Monitoramento com Prometheus

Dashboards com Grafana

Deploy na AWS (EKS/ECS)

Pipeline completo de CI/CD

👨‍💻 Autor

João Carvalho

Graduando em Ciência da Computação e entusiasta de DevOps, Cloud Computing e Automação.

LinkedIn:
https://www.linkedin.com/in/joãocarvalhoos

GitHub:
https://github.com/joaocarvals