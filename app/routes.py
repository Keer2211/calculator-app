from fastapi import APIRouter

from app.services import add, subtract, multiply, divide

router = APIRouter()   # <-- this must exist at the top level

@router.get("/add")
def add_numbers(a: float, b: float):
    return {"result": add(a, b)}

@router.get("/subtract")
def subtract_numbers(a: float, b: float):
    return {"result": subtract(a, b)}

@router.get("/multiply")
def multiply_numbers(a: float, b: float):
    return {"result": multiply(a, b)}

@router.get("/divide")
def divide_numbers(a: float, b: float):
    return {"result": divide(a, b)}