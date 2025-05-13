# 🧠 Job Application Bot

An automated job/internship application tool built with Python + Selenium.

## 🔍 What It Does

- Searches job listings based on:
  - Keywords (e.g. Software Engineer Intern, Data Analyst Intern)
  - Location (Singapore / Remote)
  - Salary threshold (if provided)

- Automatically applies to jobs that:
  - Only require resume uploads (i.e. "Easy Apply")

- Saves more complex listings (e.g., application forms) to a CSV for manual follow-up.

## 📂 Structure

- `fetcher/` — Scrapes listings from job boards (e.g. Indeed, LinkedIn)
- `filter_queue/` — Filters listings by salary, keywords, recency
- `applier/` — Uses Selenium to auto-apply to jobs
- `scheduler/` — Setup for cron jobs or GitHub Actions
- `resumes/` — Contains your tailored resumes
- `templates/` — Cover letter and other templates
- `data/` — Auto and manual queues (`to_apply.json`, `skipped.csv`)

## ⚙️ Technologies

- Python
- Selenium (for web automation)
- YAML config
- GitHub Actions (optional)
- CSV / JSON logging

## 📌 Why I Built This

As a student in Singapore looking for Software, Data, and ML internships, I wanted a smarter way to automate the application process — especially for roles with fast-moving deadlines.

## 📅 How to Run

1. Edit `config.yaml` to match your keywords, location, salary, and resume paths  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```  
3. Run:
   ```bash
   python main.py
   ```  
4. Optionally schedule it daily via cron or GitHub Actions.

---

This project is 100% customizable and intended for educational + personal productivity purposes.
