# 💰 FinTrack - Smart Finance Tracker

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/SQLModel-008080?style=for-the-badge&logo=python)](https://sqlmodel.tiangolo.com/)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)](https://jwt.io/)

FinTrack is an API-first, high-performance finance tracking application designed for modern expense management. Built with **FastAPI** and **SQLModel**, it offers a secure, scalable, and intuitive way to manage transactions with built-in analytics.

---

## 🛠️ Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) - Chosen for its high performance, automatic documentation (Swagger), and asynchronous capabilities.
- **ORM & Validation:** [SQLModel](https://sqlmodel.tiangolo.com/) - Unifies SQLAlchemy and Pydantic, providing a single source of truth for database models and API schemas.
- **Database:** SQLite - A lightweight, file-based database ideal for rapid development and portability.
- **Authentication:** OAuth2 with Password Hashing ([Bcrypt](https://pypi.org/project/passlib/)) and JSON Web Tokens ([JWT](https://github.com/mpdavis/python-jose)) for stateless, secure session management.

---

## 🏗️ Architecture & Features

### 🔐 Security First
- **Password Hashing:** Uses `passlib` with the `bcrypt` algorithm to ensure user passwords are never stored in plain text.
- **JWT Authentication:** Implements stateless authentication using Bearer tokens, allowing for secure and scalable client-server communication.

### 📊 Powerful Analytics
- Real-time spend tracking and categorization.
- Aggregated insights (Total Spend, Max Expense, Category Breakdown) powered by efficient SQL queries through SQLModel.

### 🚀 Developer Experience
- **Auto-generated Docs:** Interactive API documentation via Swagger UI.
- **Type Safety:** Full support for Python type hints, ensuring robust and maintainable code.

---

## 📡 API Reference

### Authentication
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/register` | `POST` | Create a new user account. |
| `/token` | `POST` | Authenticate and receive a JWT access token. |

### Expenses
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/add-expense` | `POST` | Record a new expense with item, amount, and category. |
| `/expenses` | `GET` | Retrieve all recorded transactions. |
| `/analytics` | `GET` | Get a detailed breakdown of financial activity. |

### Example: Adding an Expense
```bash
curl -X 'POST' \
  'http://localhost:8000/add-expense' \
  -H 'Content-Type: application/json' \
  -d '{
  "item": "Coffee",
  "amount": 4.50,
  "category": "Food"
}'
```

---

## 🚦 Getting Started

### Prerequisites
- Python 3.8+
- Virtual Environment (recommended)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanyamChaudhary27/FinTrack.git
   cd FinTrack/backend
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Explore the API:**
   Visit `http://localhost:8000/docs` to access the interactive Swagger documentation.

---

## 🔮 Future Roadmap
- [ ] **Frontend Integration:** Build a React or Next.js dashboard for visual analytics.
- [ ] **Advanced Filters:** Filter expenses by date range and category tags.
- [ ] **Multi-currency Support:** Automatic currency conversion using external APIs.
- [ ] **Cloud Deployment:** Containerization with Docker and deployment to AWS/Heroku.

---
*Developed with focus on performance and security by **Sanyam Chaudhary***
