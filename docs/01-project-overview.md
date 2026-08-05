# Secure Cloud Web Platform

## Objective

Build a secure cloud platform to host a web application.

The platform must be:
- **Automated**
- **Secure**
- **Monitored**
- **Documented**
- **Scalable**

---

## Architecture & Technology Stack

### Cloud & Infrastructure
* **Cloud Provider:** Azure
* **Infrastructure as Code (IaC):** Terraform
* **CI/CD:** GitHub Actions

### Application & Database
* **Framework:** FastAPI
  * *Why FastAPI?* Simple, widely adopted, easy to secure, features automatic API documentation, and ideal for REST APIs.
* **Database:** Azure SQL

### Authentication
* **Current:** JWT
* **Future Roadmap:** Microsoft Entra ID Integration

---

## Security & Compliance

* **Key Management:** Azure Key Vault
* **Access Control:** Managed Identity & RBAC (Role-Based Access Control)
* **Network Security:** NSGs (Network Security Groups)
* **Governance & Threat Protection:** Azure Policy & Defender for Cloud

---

## Monitoring & Observability

* Log Analytics
* Azure Monitor

---

## Security Testing Tools

* OWASP ZAP
* Burp Suite
* Nmap
* Nikto
