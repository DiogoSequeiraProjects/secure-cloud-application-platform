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
```
### Phase 3: Network Security & Segmentation
Isolated workloads using network segmentation to prevent lateral movement.

Configured isolated Virtual Networks (VNets) and micro-segmented Subnets.

Enforced strict ingress/egress rules using Network Security Groups (NSGs).

### Phase 4: Identity & Access Management (IAM)
Implemented granular access controls aligned with the Principle of Least Privilege.

Customized Azure RBAC assignments for human and machine identities.

Elimination of overly permissive default roles across management groups.

### Phase 5: Secrets & Credentials Management
Zero-hardcoded secrets policy implemented across application and infrastructure layers.

Centralized storage for API keys, storage account tokens, and database credentials inside Azure Key Vault.

Automated access via Managed Identities to eliminate static secrets.

### Phase 6: Cloud Governance & Compliance
Maintained resource compliance and prevented accidental configuration alterations.

Implemented Azure Policies to enforce resource compliance and tagging strategies.

Applied Resource Locks to prevent critical resource destruction.

### Phase 7: Continuous Monitoring & Security Operations
End-to-end visibility and real-time threat detection across the infrastructure.

Integrated Log Analytics Workspace for centralized diagnostic log collection.

Enabled Microsoft Defender for Cloud and Azure Monitor for security alerting and compliance monitoring.

### Phase 8: DevSecOps CI/CD Pipeline
Automated pipeline integrating security checks into every stage of the software delivery lifecycle.

[ Developer ] ──> [ Pull Request ] ──> [ GitHub Actions Pipeline ]
                                                 │
            ┌────────────────────────────────────┴────────────────────────────────────┐
            ▼                                    ▼                                    ▼
   [ Terraform Fmt/Validate ]           [ Security Scanning ]                [ Terraform Plan/Apply ]

   
### 🛠️ Demonstrated Core Competencies
Cloud Architecture & Engineering: Azure Networking, IaC Architecture, Modular Design.

DevSecOps & Automation: GitHub Actions CI/CD, Automated Security Checks, Terraform.

Cybersecurity & Governance: Zero Trust Architecture, RBAC, Secrets Management, Azure Policy, Defender for Cloud.

Observability & Ops: Diagnostic Logging, Threat Detection, SIEM/Telemetry Integration.
