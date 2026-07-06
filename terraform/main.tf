# Define as configurações necessárias para o Terraform
terraform {

  # Especifica os providers utilizados no projeto
  required_providers {

    # Provider responsável por gerenciar recursos do Docker
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

# Configura a conexão com o Docker local
provider "docker" {}

# Cria um container Docker para executar a aplicação Flask
resource "docker_container" "flask_api_container" {

  # Nome que será atribuído ao container
  name = "flask-api-container"

  # Imagem Docker que será utilizada para criar o container
  image = "flask-api:latest"

  # Mapeamento de portas entre o host e o container
  ports {

    # Porta utilizada pela aplicação dentro do container
    internal = 5000

    # Porta exposta na máquina host
   external = 5000
  }

  # Define a política de reinicialização do container
  # O container será reiniciado automaticamente,
  # exceto quando for parado manualmente.
  restart = "unless-stopped"
}