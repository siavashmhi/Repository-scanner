terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }

    grafana = {
      source  = "grafana/grafana"
      version = "1.30.0" # Use the latest stable version
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

provider "grafana" {
  url  = "http://localhost:${docker_container.grafana.ports[0].external}/"
  auth = "admin:admin"
}

# Create a Docker network
resource "docker_network" "grafana_network" {
  name = "grafana_network"
}

# Pull Grafana Docker image
resource "docker_image" "grafana" {
  name         = "grafana/grafana:latest"
  keep_locally = false
}

# Create Grafana container
resource "docker_container" "grafana" {
  image = docker_image.grafana.name
  name  = "grafana"

  # Attach the container to the Docker network
  networks_advanced {
    name = docker_network.grafana_network.name
  }

  ports {
    internal = 3000
    external = 3000
  }

  env = [
    "GF_SECURITY_ADMIN_PASSWORD=admin",
    "GF_SECURITY_ADMIN_USER=admin",
  ]

  restart = "always"
  depends_on = [
    docker_network.grafana_network,
    docker_image.grafana,
  ]
}

# create sleep for grafana container
resource "time_sleep" "wait_grafana_ready" {
  create_duration = "10s"
  depends_on = [
    docker_container.grafana,
  ]
}

# create grafana user 
resource "grafana_user" "admin" {
  login    = "lzadmin"
  name     = "lzadmin"
  email    = "lzadmin@localhost"
  password = "lzadmin"
  is_admin = true
  depends_on = [
    docker_container.grafana,
    time_sleep.wait_grafana_ready,
  ]
  lifecycle {
    ignore_changes = [
      email,
      password
    ]
    prevent_destroy = false
  }
}
