variable "project_name" {
  description = "Name of the project used for Azure resource naming."
  type        = string
  default     = "secure-cloud-platform"
}

variable "environment" {
  description = "Deployment environment."
  type        = string
  default     = "dev"
}

variable "location" {
  description = "Azure region for the deployment."
  type        = string
  default     = "West Europe"
}

variable "address_space" {
  description = "Address space for the application virtual network."
  type        = list(string)
  default     = ["10.20.0.0/16"]
}
