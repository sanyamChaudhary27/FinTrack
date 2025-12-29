# 💰 FinTrack - Smart Finance Tracker

A powerful, API-first finance tracking application built with **FastAPI**. FinTrack helps users manage expenses securely with modern authentication and persistent database storage.

## 🚀 Features

- **🔐 Secure Authentication:** 
  - User Registration & Login
  - Password Hashing (Bcrypt)
  - JWT (JSON Web Tokens) for secure session management
- **💾 Persistent Storage:** 
  - SQLite Database integration (SQLModel)
  - Users and transactions are saved permanently
- **⚡ High Performance:** 
  - Built on FastAPI for blazingly fast response times
  - Async ready

## ️ Tech Stack

- **Backend:** Python 3.8+, FastAPI
- **Database:** SQLite, SQLModel
- **Security:** Passlib (Bcrypt), PyJWT, OAuth2

##  Installation & Setup

1. **Clone the repo**
   ```
   git clone https://github.com/sanyamChaudhary27/FinTrack.git
   cd FinTrack/backend
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Server**
   ```
   uvicorn main:app --reload
   ```

4. **Access API Docs**
   Go to `http://localhost:8000/docs` to test the API interactively.

##  How to Test (Auth Flow)

1. **Register:** POST `/register` with a username and password.
2. **Login:** POST `/token` to receive your **Access Token**.
3. **Protected Routes:** (Coming soon) Use the token to add/view expenses.

---
*Built with Sincerity by Sanyam Chaudhary*
