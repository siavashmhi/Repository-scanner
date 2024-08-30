terraform {
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.33.0" # You c an specify the latest version or the version you prefer
    }
  }
}
