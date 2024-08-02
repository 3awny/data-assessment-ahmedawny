import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from httpx import ASGITransport
from app.main import app

# Test endpoint that gets the top N highest paid employees
@pytest.mark.asyncio
async def test_get_top_n_highest_paid_employees():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/top-n-highest-paid-employees?n=3")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["Name"] == "Lily Evans"  # Checking the first highest paid employee
    assert data[1]["Name"] == "Oliver Queen" # Checking the second highest paid employee
    assert data[2]["Name"] == "Barry Allen"  # Checking the third highest paid employee

# Test endpoint that gets the number of employees in a specific department
@pytest.mark.asyncio
async def test_get_number_of_employees_in_department():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/number-of-employees-in-department?department=hr")
    assert response.status_code == 200
    data = response.json()
    assert data == {"department": "hr", "number_of_employees": 4}
