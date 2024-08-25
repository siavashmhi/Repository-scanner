terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.33.0"  # You c an specify the latest version or the version you prefer
    }
  }
}

provider "hcloud" {
  token = "HHCM3vaB4drbPhyfJgwFgxEZl4RUbCnBq1vGc2fIKDWBjDEkgF1Nx3oCHf4MMsxU"
}

# Create a private network with a 192.168 IP range
resource "hcloud_network" "cluster_network" {
  name     = "cluster-network"
  ip_range = "192.168.0.0/16"
}

# Create a subnet for the network
resource "hcloud_network_subnet" "subnet" {
  network_id   = hcloud_network.cluster_network.id
  type         = "cloud"
  network_zone = "eu-central"
  ip_range     = "192.168.0.0/24"
}

# Read Siavash-MacOs ssh key 
data "hcloud_ssh_key" "siavash_macos_key" {
  name       = "Siavash-MacOs"
}

# Create 4 Ubuntu servers with the specified SSH key, server type, and location
resource "hcloud_server" "master_server_1" {
  name        = "master-server-1"
  image       = "ubuntu-22.04"
  server_type = "cx21"
  location    = "nbg1"
  ssh_keys    = ["Siavash-MacOs"]

  network {
    network_id = hcloud_network.cluster_network.id
  }
}

resource "hcloud_server" "master_server_2" {
  name        = "master-server-2"
  image       = "ubuntu-22.04"
  server_type = "cx21"
  location    = "nbg1"
  ssh_keys    = ["Siavash-MacOs"]

  network {
    network_id = hcloud_network.cluster_network.id
  }
}

resource "hcloud_server" "worker_server_1" {
  name        = "worker-server-1"
  image       = "ubuntu-22.04"
  server_type = "cx21"
  location    = "nbg1"
  ssh_keys    = ["Siavash-MacOs"]

  network {
    network_id = hcloud_network.cluster_network.id
  }
}

resource "hcloud_server" "worker_server_2" {
  name        = "worker-server-2"
  image       = "ubuntu-22.04"
  server_type = "cx21"
  location    = "nbg1"
  ssh_keys    = ["Siavash-MacOs"]

  network {
    network_id = hcloud_network.cluster_network.id
  }
}

# Output the public IPs of the created servers
output "server_ips" {
  value = {
    master_server_1 = hcloud_server.master_server_1.ipv4_address
    master_server_2 = hcloud_server.master_server_2.ipv4_address
    worker_server_1 = hcloud_server.worker_server_1.ipv4_address
    worker_server_2 = hcloud_server.worker_server_2.ipv4_address
  }
}
