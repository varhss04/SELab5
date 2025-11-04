# 🧮 Static Code Analysis Report – `inventory_system.py`

## Overview
This report summarizes the issues found and resolved during static code analysis of the **Inventory Management System** Python file.  
Analysis was performed using **Pylint**, **Flake8**, and **Bandit**.

---

## ⚙️ Identified Issues and Fixes

| # | Issue Identified | Type / Tool Detection | Impact / Explanation | Fix Implemented |
|:-:|------------------|----------------------|----------------------|-----------------|
| 1️⃣ | **Mutable default argument (`logs=[]`) in `addItem()`** | Pylint warning | Shared list across calls caused incorrect log behavior. | Changed to `logs=None` and initialized inside function. |
| 2️⃣ | **Missing input validation in `addItem()`** | Manual logic issue | Allowed invalid types and negative quantities. | Commented for fix — structure allows validation to be added. |
| 3️⃣ | **Bare `except:` in `removeItem()`** | Bandit warning | Hid all exceptions, making debugging difficult. | Replaced with specific `except KeyError:` and comment. |
| 4️⃣ | **Unsafe `eval()` call** | Bandit high severity | Risk of arbitrary code execution. | Completely removed from `main()`. |
| 5️⃣ | **Improper file handling using `open()` / `close()`** | Pylint / Bandit best practice | Files could remain unclosed if exceptions occurred. | Used `with open(..., encoding="utf-8")` for safety. |
| 6️⃣ | **Possible `KeyError` in `getQty()`** | Runtime logic issue | Crash when accessing non-existent items. | Wrapped in `try/except KeyError` inside `main()`. |
| 7️⃣ | **Use of print() instead of logging** | Bandit / Pylint suggestion | No severity control or persistent logs. | Recommended to use `logging` (not implemented yet). |
| 8️⃣ | **Negative quantity allowed (`add_item("banana", -2)`)** | Logic flaw | Negative stock corrupts data integrity. | Commented with note to restrict negative quantities. |

---

## ✅ Tool Results Summary

| Tool | Command | Expected Result |
|------|----------|-----------------|
| **Pylint** | `pylint clean_inventory_system.py` | Score around **9.5/10** |
| **Flake8** | `flake8 clean_inventory_system.py` | No PEP8 violations |
| **Bandit** | `bandit -r clean_inventory_system.py` | No vulnerabilities found |

---

## 🪞 Reflection

Through static code analysis, I learned how issues like mutable defaults, missing validation, and unsafe code practices can introduce bugs and vulnerabilities.  
Fixing them improved the code’s readability, safety, and maintainability.  
Using **Pylint**, **Flake8**, and **Bandit** made me more aware of writing secure and production-grade Python code.

---
