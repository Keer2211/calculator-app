# 🧮 FastAPI Calculator App

A simple yet professional **Calculator API + UI** built with [FastAPI](https://fastapi.tiangolo.com/).  
This project demonstrates clean architecture, modular code, and a minimal frontend using Jinja2 templates.

---

## 🚀 Features
- **Basic operations**: Addition, subtraction, multiplication, division
- **REST API** endpoints (`/api/add`, `/api/subtract`, `/api/multiply`, `/api/divide`)
- **Web UI** with input fields and buttons
- **Error handling** (e.g., division by zero)
- **Static files** for styling
- **Ready for deployment** on GitHub and cloud platforms

---

## 📂 Project Structure
calculator-app/
├── app/
│   ├── init.py
│   ├── main.py           # FastAPI app entrypoint
│   ├── routes.py         # API routes
│   ├── services.py       # Business logic
│   └── templates/
│       └── index.html    # Calculator UI
├── static/
│   └── style.css         # Frontend styling
├── requirements.txt      # Dependencies
└── README.md             # Project documentation


---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/keertika/calculator-app.git
cd calculator-app

**Create and activate a virtual environment
**
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux

**Install dependencies
**
pip install -r requirements.txt

**Run the server
**
python -m uvicorn app.main:app --reload

Access the app
Calculator UI → http://127.0.0.1:8000/
Swagger Docs → http://127.0.0.1:8000/docs (127.0.0.1 in Bing)

**clone and run it with
**
git clone https://github.com/keertika/calculator-app.git
cd calculator-app
python -m venv venv
venv\Scripts\activate   # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
