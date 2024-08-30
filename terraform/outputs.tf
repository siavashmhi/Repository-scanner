# Output the public IPs of the created servers
output "server_ips" {
  value = {
    master_server_1 = hcloud_server.master_server_1.ipv4_address
    master_server_2 = hcloud_server.master_server_2.ipv4_address
    worker_server_1 = hcloud_server.worker_server_1.ipv4_address
    worker_server_2 = hcloud_server.worker_server_2.ipv4_address
  }
}
