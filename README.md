# Customer Management System – Flask REST API

## 📌 Overview
A simple backend REST API built using Flask that performs CRUD operations on customer data.
This project demonstrates clean architecture, object-oriented programming, and RESTful design
principles suitable for entry-level software engineering roles.

---

## 🛠️ Tech Stack
- Python
- Flask
- REST API
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure
- `routes/` – API endpoints
- `services/` – Business logic
- `models/` – Data models
- `database/` – Database connection placeholders

---

## 🚀 Features
- Create Customer
- Retrieve Customer by ID
- Retrieve All Customers
- Update Customer
- Delete Customer
- Basic input validation
- Error handling
- MySQL & MongoDB placeholders

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/api/customers/` | Create customer |
| GET | `/api/customers/{id}` | Get customer |
| GET | `/api/customers/` | Get all customers |
| PUT | `/api/customers/{id}` | Update customer |
| DELETE | `/api/customers/{id}` | Delete customer |

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
python app.py
