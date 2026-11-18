# 🔐 Python Secure Coding Review

### Identifying • Analyzing • Understanding • Remediating Security Vulnerabilities

\<p align="center">



\


\</p>

---

## `01` — Project Overview

This project demonstrates a practical **Secure Coding Review** of a deliberately vulnerable Python login application.

The objective was to investigate common application security weaknesses through manual source code inspection and automated static analysis using **Bandit**.

The assessment focused on identifying insecure password hashing, potentially vulnerable SQL query construction, and weaknesses in authentication and access control.

Rather than simply writing functional code, this project explores the importance of developing applications with security as a fundamental requirement.

> **Core Objective:** Identify security vulnerabilities, understand their potential impact, and recommend appropriate remediation techniques.

---

## `02` — Assessment Environment

| Component            | Description               |
| :------------------- | :------------------------ |
| Programming Language | Python 3.14.8             |
| Database             | SQLite3                   |
| Security Analyzer    | Bandit 1.9.4              |
| Operating System     | Kali Linux                |
| Assessment Method    | Manual Code Review + SAST |
| Application Type     | Python Login System       |

### Tools & Technologies

- **Python:** Application development and source code analysis.
- **SQLite3:** Database operations and user management.
- **Bandit:** Automated Python security vulnerability detection.
- **Kali Linux:** Security testing environment.

---

## `03` — Application Architecture

The application was developed as a basic user authentication system containing the following functionalities:

| Function            | Description                                |
| :------------------ | :----------------------------------------- |
| User Registration   | Creates new user accounts.                 |
| Password Hashing    | Hashes passwords before database storage.  |
| User Authentication | Checks submitted credentials.              |
| SQLite Integration  | Stores and retrieves user information.     |
| Admin Panel         | Provides access to database functionality. |

### Project Structure

```text
secure-coding-review/
│
├── main.py
│
├── README.md
│
└── requirements.txt
```

The application was intentionally developed with insecure coding practices to provide a practical environment for security assessment.

---

## `04` — Security Assessment Methodology

The assessment was conducted using two complementary approaches.

### A. Manual Source Code Inspection

The application source code was inspected to identify potentially insecure implementations.

Areas examined:

- Password hashing mechanisms.
- SQL query construction.
- Authentication mechanisms.
- Authorization controls.
- Sensitive information exposure.
- User input handling.

### B. Static Application Security Testing (SAST)

Bandit was used to automatically inspect the Python source code for common security weaknesses.

**Command executed:**

```bash
bandit -r main.py
```

Bandit analyzed the application and generated a report containing vulnerability identifiers, severity ratings, confidence levels, affected code locations, and CWE references.

---

## `05` — Security Assessment Results

\<details>
\<summary>\<strong>▼ View Security Assessment Summary\</strong>\</summary>

| Metric          | Result |
| :-------------- | -----: |
| Lines of Code   |     70 |
| Total Findings  |      4 |
| High Severity   |      2 |
| Medium Severity |      2 |
| Low Severity    |      0 |
| Files Skipped   |      0 |

\</details>

### Vulnerability Distribution

| Severity  | Findings | Distribution |
| :-------- | -------: | :----------- |
| 🔴 High   |        2 | 50%          |
| 🟠 Medium |        2 | 50%          |
| 🟢 Low    |        0 | 0%           |

### Overall Findings

\<pre> HIGH      ██████████  2 MEDIUM    ██████████  2 LOW                   0  TOTAL FINDINGS: 4 \</pre>

*Note: The distribution represents Bandit's four reported findings, not four unique root causes.*

---

## `06` — Detailed Vulnerability Analysis

### Finding 01 — Weak Cryptographic Hashing

\<p> \<img src="[https://img.shields.io/badge/SEVERITY-HIGH-red?style=flat-square](https://img.shields.io/badge/SEVERITY-HIGH-red?style=flat-square)" /> \<img src="[https://img.shields.io/badge/CONFIDENCE-HIGH-red?style=flat-square](https://img.shields.io/badge/CONFIDENCE-HIGH-red?style=flat-square)" /> \<img src="[https://img.shields.io/badge/BANDIT-B324-blue?style=flat-square](https://img.shields.io/badge/BANDIT-B324-blue?style=flat-square)" /> \</p>

**CWE-327 — Use of a Broken or Risky Cryptographic Algorithm**

**Affected locations:** `main.py:25` and `main.py:53`

**Description**

The application uses the MD5 hashing algorithm to process user passwords during registration and authentication.

MD5 is considered cryptographically broken and is unsuitable for password storage because it is extremely fast to calculate and does not provide the computational resistance required against modern password-cracking attacks.

**Potential Impact**

- Increased risk of password recovery if database hashes are exposed.
- Greater susceptibility to dictionary and brute-force attacks.
- Compromised user accounts.

**Recommended Remediation**

Replace MD5 with a dedicated password-hashing algorithm such as Argon2id or bcrypt.

---

### Finding 02 — Potential SQL Injection in Registration

\<p>
\<img src="[https://img.shields.io/badge/SEVERITY-MEDIUM-orange?style=flat-square](https://img.shields.io/badge/SEVERITY-MEDIUM-orange?style=flat-square)" />
\<img src="[https://img.shields.io/badge/CONFIDENCE-LOW-yellow?style=flat-square](https://img.shields.io/badge/CONFIDENCE-LOW-yellow?style=flat-square)" />
\<img src="[https://img.shields.io/badge/BANDIT-B608-blue?style=flat-square](https://img.shields.io/badge/BANDIT-B608-blue?style=flat-square)" />
\</p>

**CWE-89 — SQL Injection**

**Affected location:** `main.py:28`

**Description**

The registration function constructs SQL statements using Python f-strings.

User-controlled input is directly inserted into the SQL query.

This creates a potential SQL Injection vulnerability because specially crafted input may alter the intended SQL statement.

**Potential Impact**

- Unauthorized database operations.
- Manipulation of database records.
- Potential exposure of sensitive information.

**Recommended Remediation**

Use parameterized SQL statements to separate user input from executable SQL commands.

---

### Finding 03 — Potential SQL Injection in Authentication

\<p>
\<img src="[https://img.shields.io/badge/SEVERITY-MEDIUM-orange?style=flat-square](https://img.shields.io/badge/SEVERITY-MEDIUM-orange?style=flat-square)" />
\<img src="[https://img.shields.io/badge/CONFIDENCE-LOW-yellow?style=flat-square](https://img.shields.io/badge/CONFIDENCE-LOW-yellow?style=flat-square)" />
\<img src="[https://img.shields.io/badge/BANDIT-B608-blue?style=flat-square](https://img.shields.io/badge/BANDIT-B608-blue?style=flat-square)" />
\</p>

**CWE-89 — SQL Injection**

**Affected location:** `main.py:44`

**Description**

The login function uses string-based SQL query construction to retrieve user information.

The username is inserted directly into the SQL statement instead of being passed as a parameter.

**Potential Impact**

An attacker may manipulate the database query and potentially bypass intended username filtering or access unauthorized records.

**Recommended Remediation**

Replace string interpolation with parameterized SQL queries.

---

### Finding 04 — Weak Hashing During Password Verification

\<p> \<img src="[https://img.shields.io/badge/SEVERITY-HIGH-red?style=flat-square](https://img.shields.io/badge/SEVERITY-HIGH-red?style=flat-square)" /> \<img src="[https://img.shields.io/badge/CONFIDENCE-HIGH-red?style=flat-square](https://img.shields.io/badge/CONFIDENCE-HIGH-red?style=flat-square)" /> \<img src="[https://img.shields.io/badge/BANDIT-B324-blue?style=flat-square](https://img.shields.io/badge/BANDIT-B324-blue?style=flat-square)" /> \</p>

**CWE-327 — Use of a Broken or Risky Cryptographic Algorithm**

**Affected location:** `main.py:53`

**Description**

The login functionality uses MD5 to calculate the hash of the submitted password before comparing it with the stored password hash.

This continues the use of an insecure cryptographic algorithm throughout the authentication process.

**Potential Impact**

The application remains dependent on weak password hashing, making stored credentials more vulnerable if database information is compromised.

**Recommended Remediation**

Implement a secure password verification mechanism using Argon2id or bcrypt.

---

## `07` — Additional Manual Review Finding

### Missing Authentication and Authorization Controls

**Detection Method:** Manual Code Inspection

During the manual assessment, an additional security weakness was identified in the admin panel.

The admin functionality can be accessed directly without checking whether the user is authenticated or has administrative privileges.

**Potential Impact**

- Unauthorized access to administrative functionality.
- Exposure of database records.
- Disclosure of stored password hashes.

**Recommended Remediation**

- Implement authentication before granting access to administrative functionality.
- Introduce role-based access control (RBAC).
- Restrict administrative actions to authorized users.
- Never expose stored password hashes through application interfaces.

**Important:** This finding was identified manually and was not included in Bandit's four reported findings.

---

## `08` — Remediation Strategy

The following security improvements are recommended:

| Security Issue                | Recommended Solution                       |
| :---------------------------- | :----------------------------------------- |
| Weak MD5 hashing              | Implement Argon2id or bcrypt               |
| SQL Injection in registration | Use parameterized queries                  |
| SQL Injection in login        | Use parameterized queries                  |
| Missing admin authentication  | Implement authentication and authorization |
| Sensitive data exposure       | Restrict database information access       |

### Example: Secure SQL Query

**Vulnerable implementation:**

```python
query = f"""
SELECT * FROM users
WHERE username = '{username}'
"""

cursor.execute(query)
```

**Improved implementation:**

```python
query = """
SELECT * FROM users
WHERE username = ?
"""

cursor.execute(query, (username,))
```

Parameterized queries ensure that user input is treated as data rather than executable SQL syntax.

---

## `09` — Key Learning Outcomes

This assessment provided practical experience in:

- Understanding common Python application vulnerabilities.
- Identifying weak cryptographic implementations.
- Recognizing potential SQL Injection vulnerabilities.
- Using Bandit for static application security testing.
- Interpreting vulnerability severity and confidence ratings.
- Understanding CWE classifications.
- Performing manual source code security reviews.
- Applying secure coding principles.
- Recommending appropriate remediation techniques.

**Key Takeaway:**

> Security is not an additional feature. It is a fundamental part of software development.

---

## `10` — Conclusion

The security assessment successfully identified four findings through automated static analysis and one additional security weakness through manual code inspection.

The results demonstrated how seemingly simple implementation choices, such as password hashing and SQL query construction, can introduce significant security risks.

The exercise also highlighted the importance of combining automated security tools with manual code review.

Although Bandit provides valuable insights into potentially insecure coding patterns, it cannot independently identify every application-level security weakness.

The next stage of this project is to implement the recommended security improvements, perform another assessment, and compare the results.

**Assessment Status:** Initial security review completed. Remediation and retesting pending.

---

## `11` — References & Resources

- [Bandit Documentation](https://bandit.readthedocs.io/)
- [CWE-327 — Risky Cryptographic Algorithm](https://cwe.mitre.org/data/definitions/327.html)
- [CWE-89 — SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

---

\<p align="center">

**PYTHON SECURE CODING REVIEW**

*Learning to identify vulnerabilities. Understanding their impact. Building more secure applications.*

\</p>
