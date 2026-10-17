resource "azurerm_virtual_network" "main" {
  name                = "${local.name_prefix}-vnet"
  location            = var.location
  resource_group_name = azurerm_resource_group.main.name
  address_space       = var.address_space

  tags = local.common_tags
}

resource "azurerm_subnet" "application" {
  name                 = "${local.name_prefix}-app-subnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.20.1.0/24"]
}

resource "azurerm_subnet" "management" {
  name                 = "${local.name_prefix}-management-subnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.20.2.0/24"]
}
