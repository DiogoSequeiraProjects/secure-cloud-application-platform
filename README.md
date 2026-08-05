# 🛡️ Enterprise Cloud Platform & DevSecOps Architecture

An end-to-end, production-grade cloud platform hosted on **Microsoft Azure**, provisioned via **Terraform (IaC)**, secured with **Zero Trust principles**, and fully automated using **GitHub Actions (DevSecOps)**.

---

## 🎯 Architecture Overview & Key Objectives

This project demonstrates a **Secure-by-Design** methodology to host modern enterprise web applications. Rather than deploying resources manually, every component was architected, provisioned, and governed using Infrastructure as Code (IaC) and DevSecOps best practices.

### 🌟 Key Objectives
* **Infrastructure as Code (IaC):** 100% automated provisioning via Terraform modules.
* **Zero Trust & Defense-in-Depth:** Micro-segmented networks, strict RBAC, and explicit identity boundaries.
* **Automated DevSecOps Pipeline:** Continuous security scans and automated deployment workflows.
* **Centralized Governance & Observability:** Real-time threat detection, compliance rules, and audit logging.

---

## 🏗️ High-Level Architecture & Tech Stack

┌─────────────────────────────────────────────────────────┐
│                     Developer Workflow                  │
└────────────────────────────┬────────────────────────────┘
│ Push / PR
▼
┌─────────────────────────────────────────────────────────┐
│                     GitHub Actions                      │
│  (Fmt ➔ Validate ➔ Security Scan ➔ Plan ➔ Apply)        │
└────────────────────────────┬────────────────────────────┘
│ Provision / Update
▼
┌─────────────────────────────────────────────────────────┐
│                    Microsoft Azure                      │
│ ┌───────────────────┐ ┌───────────────────────────────┐ │
│ │  Network Isolation│ │      Security & Governance    │ │
│ │  - Virtual Network│ │  - Azure Key Vault            │ │
│ │  - NSG Rules      │ │  - Azure Policy / Defender    │ │
│ └───────────────────┘ └───────────────────────────────┘ │
│ ┌───────────────────┐ ┌───────────────────────────────┐ │
│ │  Identity & Access│ │ Monitoring & Observability    │ │
│ │  - Azure RBAC     │ │  - Log Analytics              │ │
│ │  - Managed Identities│- Azure Monitor               │ │
│ └───────────────────┘ └───────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘


| Domain | Technology / Service |
| :--- | :--- |
| **Cloud Provider** | Microsoft Azure |
| **IaC & Automation** | Terraform, GitHub Actions |
| **Security & Identity** | Azure Key Vault, Azure RBAC, Managed Identities, Azure Policy |
| **Networking** | Virtual Networks (VNet), Subnets, Network Security Groups (NSGs) |
| **Monitoring & Security Ops** | Azure Monitor, Log Analytics Workspace, Defender for Cloud |

---

## 🚀 Implementation Phases

### Phase 1: Architecture Design & Project Planning
Focused on designing a production-inspired architecture following the **Zero Trust Security Model** and Azure Best Practices prior to resource deployment.
* **Focus:** Network segmentation, identity architecture, governance planning, and threat surface reduction.
* **Deliverables:** High-Level Architecture Diagrams, Network Topology, Terraform Modular Layout.

### Phase 2: Infrastructure as Code (Terraform)
Modularized Infrastructure as Code configuration to prevent configuration drift and guarantee idempotent deployments.
* **Module Structure:**
```text
terraform/
├── modules/
│   ├── networking/
│   ├── security/
│   ├── monitoring/
│   ├── identity/
│   └── governance/
├── main.tf
├── variables.tf
└── outputs.tf
