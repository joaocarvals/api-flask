terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "flask_api" {
  name = "flask-api:latest"

  build {
    context = ".."
    dockerfile = "./Dockerfile"
  }
}

resource "docker_container" "flask_api_container" {
  name  = "flask-api-container"

  image = docker_image.flask_api.image_id

  ports {
    internal = 5000
    external = 5000
  }
}