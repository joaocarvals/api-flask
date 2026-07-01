terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_container" "flask_api_container" {
  name  = "flask-api-container"
  image = "flask-api:latest"

  ports {
    internal = 5000
    external = 5000
  }

  restart = "unless-stopped"
}