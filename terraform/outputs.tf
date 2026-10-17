output "resource_group_name" {
  description = "Name of the main Azure Resource Group."
  value       = azurerm_resource_group.main.name
}

output "virtual_network_name" {
  description = "Name of the application virtual network."
  value       = azurerm_virtual_network.main.name
}

output "application_subnet_id" {
  description = "Resource ID of the application subnet."
  value       = azurerm_subnet.application.id
}

output "management_subnet_id" {
  description = "Resource ID of the management subnet."
  value       = azurerm_subnet.management.id
}

output "application_nsg_id" {
  description = "Resource ID of the application Network Security Group."
  value       = azurerm_network_security_group.application.id
}
