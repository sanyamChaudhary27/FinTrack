from pydantic import BaseModel, EmailStr
from typing import Optional
from sqlmodel import Field, SQLModel

class ExpenseBase(SQLModel):
    item: str
    amount: float
    category: str

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str
    username: str
    password: str

class Expense(ExpenseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class ExpenseCreate(ExpenseBase):
    pass

class Analytics(BaseModel):
    total_expense: float
    max_expense: float
    categorized_spend: dict

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str