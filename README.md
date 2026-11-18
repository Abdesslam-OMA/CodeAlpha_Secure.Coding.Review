<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:1E293B,100:0284C7&height=220&section=header&text=Python%20Secure%20Coding%20Review&fontSize=38&fontColor=F8FAFC&fontAlignY=38&desc=Static%20Application%20Security%20Testing%20(SAST)%20%26%20Manual%20Code%20Audit&descAlignY=58&descSize=16&animation=fadeIn" width="100%" alt="Python Secure Coding Review" />

<p align="center">
  <img src="https://img.shields.io/badge/Assessment_Type-SAST_%2B_Manual_Audit-0284C7?style=for-the-badge&logo=shield&logoColor=white" alt="Assessment Type" />
  <img src="https://img.shields.io/badge/Target_Runtime-Python_3.14.8-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Analyzer-Bandit_v1.9.4-DC2626?style=for-the-badge&logo=securityscorecard&logoColor=white" alt="Bandit" />
  <img src="https://img.shields.io/badge/Environment-Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Status-Baseline_Audit_Complete-16A34A?style=for-the-badge" alt="Status" />
</p>

<p align="center">
  <a href="#-executive-summary">Executive Summary</a> •
  <a href="#%EF%B8%8F-assessment-environment--architecture">Environment</a> •
  <a href="#-security-assessment-methodology">Methodology</a> •
  <a href="#-security-assessment-metrics">Metrics</a> •
  <a href="#-vulnerability-findings">Findings</a> •
  <a href="#%EF%B8%8F-remediation-roadmap--secure-code-comparison">Remediation</a> •
  <a href="#-references--standards">References</a>
</p>

</div>

---

## 📋 Executive Summary

This repository documents a structured **Secure Coding Review** of a baseline Python/SQLite authentication service (`main.py`). The engagement combined automated **Static Application Security Testing (SAST)** with **Bandit** and a **manual line-by-line architectural inspection** to uncover implementation flaws, cryptographic weaknesses, and authorization gaps.

> **Assessment Thesis:** Automated SAST tooling rapidly detects known insecure API sinks and broken cryptographic primitives, whereas manual source review is indispensable for uncovering business-logic and access-control vulnerabilities that are syntactically valid.

### Key Audit Highlights

- **Automated SAST scan (Bandit v1.9.4):** flagged **4 security findings** across 70 lines of source code (**2 High**, **2 Medium**), mapped to **CWE-327** and **CWE-89**.
- **Manual logic audit:** identified **1 Critical architectural vulnerability** (**CWE-284, Improper Access Control**) that allows unauthenticated access to administrative database dumps, an issue completely invisible to syntax-level static analyzers.

---

## 🛠️ Assessment Environment & Architecture

### Engagement Specifications

| Parameter | Specification |
| :--- | :--- |
| **Target Application** | CLI User Authentication & Admin Management System (`main.py`) |
| **Runtime & Engine** | Python `3.14.8` • SQLite3 embedded relational database |
| **SAST Tooling** | Bandit `1.9.4` (AST-based Python security linter) |
| **Testing Host** | Kali Linux security workstation |
| **Methodology** | Hybrid white-box audit (automated SAST + manual code inspection) |
| **CWE / Standards Mapping** | MITRE CWE Top 25 • OWASP ASVS v4.0 • OWASP Cheat Sheet Series |

### Target Attack Surface (`main.py`)

| Module / Function | Responsibility | Security Relevance |
| :--- | :--- | :--- |
| `register()` | Creates new user records in `users.db` | Handles raw credentials, password hashing, and SQL `INSERT` execution |
| `login()` | Validates user credentials against stored hashes | Processes untrusted username input and performs hash verification |
| `admin_panel()` | Queries and prints all records from the `users` table | Exposes sensitive database records and password hashes without session checks |

---

## 🔍 Security Assessment Methodology

The review followed a two-phase white-box auditing workflow.

### Phase 1: Automated SAST (Bandit)

Abstract Syntax Tree (AST) scanning was run across the codebase to identify insecure standard-library calls and tainted string interpolation:

```bash
bandit -r main.py
```

**Focus:** cryptographic primitives, SQL query construction, hardcoded secrets, and unsafe execution sinks.

### Phase 2: Manual Source Inspection

Line-by-line architectural and control-flow review to evaluate trust boundaries and application logic.

**Focus:** authentication state management, role-based access control (RBAC), privilege separation, and sensitive data exposure.

---

## 📊 Security Assessment Metrics

| Audit Metric | Value | Notes |
| :--- | :---: | :--- |
| **Lines of Code Scanned** | 70 | 0 lines skipped (no `#nosec` directives) |
| **Automated SAST Findings** | 4 | Maps to 2 unique root-cause CWEs (CWE-327, CWE-89) |
| **Manual Logic Findings** | 1 | High-impact authorization bypass (CWE-284) |
| **Total Actionable Issues** | **5** | Combined SAST + manual review |

### Severity Distribution (Combined Audit)

```text
CRITICAL (Manual)  ████░░░░░░░░░░░░░░░░  1  (20%)  [CWE-284: Unauthenticated Admin Access]
HIGH     (Bandit)  ████████░░░░░░░░░░░░  2  (40%)  [CWE-327: Broken MD5 Password Hashing]
MEDIUM   (Bandit)  ████████░░░░░░░░░░░░  2  (40%)  [CWE-89:  SQL Injection via f-strings]
LOW      (Bandit)  ░░░░░░░░░░░░░░░░░░░░  0  (0%)
```

---

## 🚨 Vulnerability Findings

### Summary Matrix

| ID | Vulnerability | CWE | Detection | Severity / Confidence | Location |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VULN-01** | Weak cryptographic hash (MD5) in registration | CWE-327 | Bandit B324 | 🔴 High / High | `main.py:25` |
| **VULN-02** | SQL injection via string interpolation (`INSERT`) | CWE-89 | Bandit B608 | 🟠 Medium / Low | `main.py:28` |
| **VULN-03** | SQL injection via string interpolation (`SELECT`) | CWE-89 | Bandit B608 | 🟠 Medium / Low | `main.py:44` |
| **VULN-04** | Weak cryptographic hash (MD5) in verification | CWE-327 | Bandit B324 | 🔴 High / High | `main.py:53` |
| **VULN-05** | Missing authentication & authorization on admin panel | CWE-284 | Manual audit | 🟣 Critical / High | `main.py:63-74`, `main.py:87` |

---

### VULN-01 & VULN-04: Use of Broken Cryptographic Hash (MD5)

**Affected locations:** `main.py:25` (`register()`) and `main.py:53` (`login()`)

**Root cause:** User passwords are digested with raw, unsalted `hashlib.md5()`. MD5 is collision-vulnerable and engineered for high-throughput checksums, not credential storage. Without a unique salt or an adaptive work factor, stored digests can be cracked at billions of hashes per second on modern GPUs, or matched instantly with precomputed rainbow tables.

**Impact:** Full credential compromise across all registered accounts if `users.db` is exfiltrated through backup exposure, local file disclosure, or SQL injection.

**Remediation:** Migrate password storage to an adaptive, salted, memory-hard key derivation function such as **Argon2id** (`argon2-cffi`) or **bcrypt**.

---

### VULN-02 & VULN-03: SQL Injection via Dynamic f-String Interpolation

**Affected locations:** `main.py:28` (`register()`) and `main.py:44` (`login()`)

**Root cause:** Untrusted user input (`username`) is interpolated directly into SQL strings using Python f-strings (`WHERE username = '{username}'`). Because data and control planes are mixed, a single quote (`'`) breaks out of the string literal and injects arbitrary SQL.

**Impact:** Authentication bypass (for example `' OR '1'='1' --`), unauthorized account enumeration, and manipulation of query execution flow.

**Remediation:** Strictly separate SQL syntax from user data using parameterized queries (`?` placeholders), supported natively by `sqlite3`.

---

### VULN-05: Unauthenticated Admin Panel (Manual Review Finding)

**Affected locations:** `main.py:63-74` (`admin_panel()`) and `main.py:87` (main menu loop)

**Root cause:** Selecting option 3 in the CLI menu invokes `admin_panel()` directly, without checking whether a user session exists or whether the caller holds administrative privileges. In addition, `SELECT * FROM users` dumps raw password hashes to stdout.

**Impact:** Complete bypass of access controls. Any anonymous user can enumerate all registered usernames and extract their unsalted MD5 password hashes.

**Remediation:**

1. Introduce session state tracking (`current_user`) and an `is_admin` role attribute in the database schema.
2. Enforce an explicit authorization guard at the entry point of `admin_panel()`.
3. Apply the principle of least privilege by excluding the `password` column from administrative `SELECT` projections.

> **Key lesson:** Bandit reported 0 issues on `admin_panel()` because `SELECT * FROM users` is syntactically safe from SQL injection. Static analysis alone cannot infer intended authorization boundaries.

---

## 🛡️ Remediation Roadmap & Secure Code Comparison

### Before vs. After

<table>
<tr>
<th width="50%">❌ Vulnerable</th>
<th width="50%">✅ Hardened</th>
</tr>
<tr>
<td>

```python
# 1. Unsalted, broken MD5 hash
hashed_pw = hashlib.md5(
    password.encode()
).hexdigest()
```

</td>
<td>

```python
# 1. Salted, adaptive bcrypt hash
hashed_pw = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)
```

</td>
</tr>
<tr>
<td>

```python
# 2. SQL injection via f-string
query = f"""
SELECT * FROM users
WHERE username = '{username}'
"""
cursor.execute(query)
```

</td>
<td>

```python
# 2. Parameterized SQL query
cursor.execute(
    "SELECT id, username, password, is_admin "
    "FROM users WHERE username = ?",
    (username,)
)
```

</td>
</tr>
<tr>
<td>

```python
# 3. No auth check on admin panel
elif choice == "3":
    admin_panel()
```

</td>
<td>

```python
# 3. Session & RBAC enforcement
elif choice == "3":
    admin_panel(current_user)
```

</td>
</tr>
</table>

### Actionable Remediation Checklist

-  **Phase 1: Static & Manual Audit.** Identify cryptographic, injection, and access-control weaknesses (`main.py`).
-  **Phase 2: Cryptographic Hardening.** Replace `hashlib.md5` with bcrypt (`gensalt()` + `checkpw()`).
-  **Phase 3: Query Parameterization.** Refactor all `cursor.execute()` calls to use `?` bind parameters.
-  **Phase 4: RBAC & Data Minimization.** Gate `admin_panel()` behind authenticated `is_admin` checks and omit password hashes from output.
-  **Phase 5: Verification Re-Scan.** Re-run `bandit -r main.py` to confirm 0 High/Medium findings.

---

## 🎯 Key Security Engineering Takeaways

1. **Defense in depth in the SDLC:** integrating SAST tools like Bandit into development workflows catches low-hanging vulnerabilities before code reaches production.
2. **Tooling boundaries:** automated scanners excel at pattern and taint analysis (CWE-89, CWE-327), but human review remains essential for authorization flaws (CWE-284) and business-logic gaps.
3. **Secure defaults:** parameterized queries, modern password hashing (Argon2id / bcrypt), and default-deny access control eliminate entire vulnerability classes at design time.

---

## 📚 References & Standards

- [Bandit Documentation](https://bandit.readthedocs.io/): Python AST security linter
- [MITRE CWE-327](https://cwe.mitre.org/data/definitions/327.html): Use of a Broken or Risky Cryptographic Algorithm
- [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html): Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
- [MITRE CWE-284](https://cwe.mitre.org/data/definitions/284.html): Improper Access Control
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

---

<div align="center">

**PYTHON SECURE CODING REVIEW**

*Security is not an afterthought. It is a core architectural requirement.*

</div>
