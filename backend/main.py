from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from models import Expense, ExpenseCreate, Analytics, User, UserCreate, Token, UserRead
from typing import List
from sqlmodel import Session, select, func
from database import create_db_and_tables, get_session
from auth import get_password_hash, verify_password, create_access_token

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return {"message": "FinTrack System Active"}

@app.post("/add-expense", response_model=Expense)
def add_expense(expense_data: ExpenseCreate, session: Session = Depends(get_session)):
    expense = Expense.from_orm(expense_data)
    session.add(expense)
    session.commit()
    session.refresh(expense)
    return expense


@app.get("/expenses")
def get_expenses(session: Session = Depends(get_session)):
    statement = select(Expense)
    result = session.exec(statement).all()
    return result

@app.get("/analytics", response_model=Analytics)
def get_analytics(session: Session = Depends(get_session)):
    total_expense_query = select(func.sum(Expense.amount))
    total_amount = session.exec(total_expense_query).first() or 0.0
    
    max_expense_query = select(func.max(Expense.amount))
    max_amount = session.exec(max_expense_query).first() or 0.0

    category_query = select(
        Expense.category,
        func.sum(Expense.amount)
    ).group_by(Expense.category)
    
    category_results = session.exec(category_query).all()

    breakdown = {}
    for category, amount in category_results:
        breakdown[category] = amount
        
    return Analytics(
        total_expense = total_amount,
        max_expense = max_amount,
        categorized_spend = breakdown
    )

@app.post("/register", response_model=UserRead)
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    if session.exec(select(User).where(User.username == user.username)).first():
        raise HTTPException(status_code = 404, detail = "Username Taken")
    hashed_pass = get_password_hash(user.password)
    new_user = User(email = user.email, username = user.username, password=hashed_pass)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@app.post("/token", response_model=Token)
def login_from_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
    ):
    querry = select(User).where(User.username==form_data.username)
    user = session.exec(querry).first()
    valid_pass = verify_password(form_data.password, user.password)
    if not user or not valid_pass:
        raise HTTPException(status_code = 404, detail = "Usernameor Password is incorrect")
    access_token = create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }