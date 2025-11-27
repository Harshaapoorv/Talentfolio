# Talentfolio Backend

The Talentfolio Backend is built using **FastAPI**, **Python**, and **PostgreSQL**.  
It powers the core API services for the Talentfolio platform, including authentication, user profiles, portfolios, job systems, file uploads, and notifications.

This project is designed in **sprints**, following an Agile development approach with a full-stack architecture.

---

## 🚀 Tech Stack

- **FastAPI** – High-performance Python web framework
- **Uvicorn** – ASGI server for running FastAPI
- **PostgreSQL** – Primary database
- **SQLAlchemy** – ORM for database models
- **Pydantic** – Request/response validation
- **python-dotenv** – Environment variable management

Future integrations (coming in later sprints):
- JWT Authentication (access + refresh tokens)
- OAuth (Google/GitHub)
- Cloud Storage (Supabase / Cloudinary)
- WebSockets
- CI/CD with GitHub Actions

---

## 📁 Project Structure

```bash
talentfolio-backend/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── api/                 # Routers (auth, users, projects, jobs)
│   ├── core/                # Config, security utilities
│   ├── models/              # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic request/response models
│   ├── db/                  # DB session, base metadata
│   └── __init__.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠️ Local Development Setup

### **1. Clone the repository**

```bash
git clone https://github.com/Harshaapoorv/Talentfolio.git
cd talentfolio-backend
```

### **2. Create and activate a virtual environment
macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\activate
```

### **3. Install dependencies
```bash
pip install -r requirements.txt
```


If you add new packages:
```bash
pip freeze > requirements.txt
```

### **4. Setup environment variables

Copy .env.example → .env:
```bash
cp .env.example .env
```


Update values as needed (DB, secrets, etc.).

### **5. Run the development server
```bash
uvicorn app.main:app --reload
```


The backend will run at:

http://localhost:8000

### **6. API Documentation

FastAPI provides built-in docs:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

### **7. Health Check

Test the basic health endpoint:

http://localhost:8000/health


Expected:

{ "status": "ok" }






