#  WebApp QA Auditor

A powerful, modular framework designed for **manual QA testers** and **cybersecurity analysts** to audit and test web applications — combining UI test automation, API validation, and basic security checks.

---

##  Project Structure

```bash
WebApp_QA_Auditor/
├── README.md
├── requirements.txt
├── .gitignore
├── config/
│   └── settings.yaml
├── logs/
│   └── .gitkeep
├── reports/
│   └── .gitkeep
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   ├── test_registration.py
│   │   └── test_checkout.py
│   ├── api/
│   │   ├── test_users_api.py
│   │   └── test_orders_api.py
│   └── security/
│       ├── test_xss.py
│       └── test_sql_injection.py
├── utils/
│   ├── logger.py
│   ├── driver_factory.py
│   └── test_data_loader.py
└── webapp/
    ├── pages/
    │   ├── login_page.py
    │   ├── registration_page.py
    │   └── checkout_page.py
    └── locators/
        ├── login_locators.py
        └── registration_locators.py
```

---

##  Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  Features

- Modular UI tests (Page Object Model)
- API endpoint tests with assertions
- Security checks for basic vulnerabilities
- Auto-generated logs and test reports
- Configurable base URL and test data

---

##  Author

Aleksei Kozhevnikov  
Senior QA Engineer | Cybersecurity Enthusiast  
📍 Austin, Texas  
🔗 GitHub: [lifemonitors](https://github.com/lifemonitors)  

---

