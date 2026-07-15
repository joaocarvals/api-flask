# 🚀 Flask DevOps Project

## 📖 Sobre o projeto
Este projeto foi desenvolvido para praticar e demonstrar conceitos de **DevOps** utilizando uma aplicação **Flask** simples.
O objetivo é construir um fluxo moderno de desenvolvimento, passando pela criação da aplicação, containerização, infraestrutura como código, orquestração, automação de deploy e monitoramento.

---

## 🛠️ Tecnologias
- **Python**
- **Flask**
- **Docker**
- **Kubernetes**
- **Terraform**
- **GitHub Actions**
- **Prometheus**
- **Grafana**
- **Git**
- **Render**

---

## 📂 Estrutura do projeto
```
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
```

---

## 🏗️ Arquitetura
```
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
         │
         ▼
   Prometheus + Grafana
      (Monitoramento)
```

---

## 🚀 Como executar

### 1. Clonar o projeto
```bash
git clone https://github.com/joaocarvals/api-flask
cd api-flask
```

### 2. Criar ambiente virtual
**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação
```bash
python main.py
```

A aplicação ficará disponível em:
```
http://localhost:5000
```

---

## 🐳 Docker

**Build**
```bash
docker build -t flask-api .
```

**Executar**
```bash
docker run -p 5000:5000 flask-api
```

---

## ☸️ Kubernetes

**Aplicar Deployment**
```bash
kubectl apply -f k8s/deployment.yaml
```

**Aplicar Service**
```bash
kubectl apply -f k8s/service.yaml
```

**Verificar pods**
```bash
kubectl get pods
```

**Verificar serviços**
```bash
kubectl get svc
```

---

## 🌍 Terraform
A infraestrutura é provisionada utilizando o **provider Docker** do Terraform, responsável por gerenciar a imagem e o container da aplicação de forma automatizada.

Para executar:
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

Para destruir os recursos provisionados:
```bash
terraform destroy
```

---

## 🔄 Pipeline CI/CD
O projeto utiliza **GitHub Actions** para automatizar o fluxo de integração contínua.

Fluxo atual:
1. Checkout do código
2. Instalação das dependências
3. Build da aplicação
4. Build da imagem Docker
5. Deploy automatizado

---

## 📊 Monitoramento

O projeto conta com uma stack de observabilidade utilizando **Prometheus** e **Grafana**:

- **Prometheus** coleta as métricas expostas pela aplicação e pelos recursos do cluster.
- **Grafana** consome os dados do Prometheus e exibe dashboards para acompanhamento em tempo real de métricas como uso de CPU, memória e requisições da aplicação.

---

## 🎯 Objetivos de aprendizado
- ✅ Desenvolvimento de APIs REST
- ✅ Dockerização de aplicações
- ✅ Kubernetes
- ✅ GitHub Actions
- ✅ Terraform (infraestrutura como código)
- ✅ Deploy automatizado
- ✅ Monitoramento com Prometheus
- ✅ Dashboards com Grafana

---

## 🚧 Roadmap
- [x] Criar API Flask
- [x] Criar Dockerfile
- [x] Configurar GitHub Actions
- [x] Criar Deployment Kubernetes
- [x] Criar Service Kubernetes
- [x] Finalizar Terraform
- [x] Deploy automatizado (Render)
- [x] Pipeline completo de CI/CD
- [x] Adicionar testes automatizados
- [x] Monitoramento com Prometheus
- [x] Dashboards com Grafana

---

## 👨‍💻 Autor
**João Carvalho**
Graduando em Ciência da Computação e entusiasta de DevOps, Cloud Computing e Automação.

- **LinkedIn:** [linkedin.com/in/joaocarvalhoos](https://www.linkedin.com/in/joãocarvalhoos)
- **GitHub:** [github.com/joaocarvals](https://github.com/joaocarvals)
