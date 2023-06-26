from pydantic import BaseModel

class Deposit(BaseModel):
    destination: int
    amount: float

class Withdraw(BaseModel):
    origin: int
    amount: float

class Transfer(BaseModel):
    origin: int
    amount: float
    destination: int

