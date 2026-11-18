<div align="center">

<!-- Header Banner / Title -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:1E293B,100:0284C7&height=220&section=header&text=Python%20Secure%20Coding%20Review&fontSize=38&fontColor=F8FAFC&fontAlignY=38&desc=Static%20Application%20Security%20Testing%20(SAST)%20%26%20Manual%20Code%20Audit&descAlignY=58&descSize=16&animation=fadeIn" width="100%" />

<p align="center">
  <img src="https://img.shields.io/badge/Assessment_Type-SAST_%2B_Manual_Audit-0284C7?style=for-the-badge&logo=shield&logoColor=white" alt="Assessment Type" />
  <img src="https://img.shields.io/badge/Target_Runtime-Python_3.14.8-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Analyzer-Bandit_v1.9.4-DC2626?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="Bandit" />
  <img src="https://img.shields.io/badge/Environment-Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Status-Baseline_Audit_Complete-16A34A?style=for-the-badge" alt="Status" />
</p>

<p align="center">
  <a href="#-executive-summary">Executive Summary</a> •
  <a href="#-assessment-environment--architecture">Environment</a> •
  <a href="#-security-assessment-metrics">Metrics</a> •
  <a href="#-vulnerability-findings">Findings</a> •
  <a href="#-remediation-roadmap">Remediation</a> •
  <a href="#-references--standards">References</a>
</p>

</div>

---

## 📋 Executive Summary

This repository documents a structured **Secure Coding Review** conducted against a baseline Python/SQLite authentication service (`main.py`). The engagement combined automated **Static Application Security Testing (SAST)** via **Bandit** with a **manual line-by-line architectural inspection** to uncover implementation flaws, cryptographic weaknesses, and authorization gaps.

> **Assessment Thesis:** Automated SAST tooling rapidly detects known insecure API sinks and broken cryptographic primitives, whereas manual source review is indispensable for uncovering business-logic and access-control vulnerabilities that exhibit valid syntax.

### Key Audit Highlights
* **Automated SAST Scan (`Bandit v1.9.4`):** Flagged **4 security findings** across 70 lines of source code (**2 High**, **2 Medium**) mapped to **CWE-327** and **CWE-89**.
* **Manual Logic Audit:** Identified **1 Critical architectural vulnerability** (**CWE-284 — Improper Access Control**) allowing unauthenticated access to administrative database dumps—an issue completely invisible to syntax-level static analyzers.

---

## 🛠️ Assessment Environment & Architecture

### Engagement Specifications

| Parameter | Specification |
| :--- | :--- |
| **Target Application** | CLI User Authentication & Admin Management System (`main.py`) |
| **Runtime & Engine** | Python `3.14.8` • SQLite3 Embedded Relational Database |
| **SAST Tooling** | Bandit `1.9.4` (AST-based Python Security Linter) |
| **Testing Host** | Kali Linux Security Workstation |
| **Methodology** | Hybrid White-Box Audit (Automated SAST + Manual Code Inspection) |
| **CWE / Standards Mapping** | MITRE CWE Top 25 • OWASP ASVS v4.0 • OWASP Cheat Sheet Series |

### Repository Layout

```text
secure-coding-review/
├── main.py              # Target authentication & admin application (70 LOC)
├── requirements.txt     # Environment & SAST dependencies (bandit, bcrypt)
└── README.md            # Security assessment report & remediation blueprint
