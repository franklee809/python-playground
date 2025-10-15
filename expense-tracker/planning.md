# 🧾 Receipt OCR to Google Sheets — Spec

## 📌 Overview
Automate receipt tracking by building an agentic workflow that:
- Accepts screenshot images of receipts
- Uses an LLM to perform OCR and extract structured data
- Validates and formats the data
- Appends it to a Google Sheet in a predefined schema

---

## 🧠 Workflow Summary

```mermaid
graph TD
A[Upload receipt screenshot] --> B[LLM OCR]
B --> C[Parse & validate fields]
C --> D[Format to schema]
D --> E[Append to Google Sheet]