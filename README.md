
# Student Information Management System

## 1. Project Overview

The Student Information Management System is a
web-based application developed using Python Flask
and SQLite.

It allows users to manage student information
through a simple and user-friendly interface.

## 2. Features

- Add new student records.
- View all registered students.
- Search students by name or roll number.
- Delete student records.
- Prevent duplicate roll numbers.

## 3. Technologies Used

- Python 3
- Flask
- SQLite
- HTML
- CSS
- Pytest
- Git and GitHub

## 4. Project Structure

student-information-system/

- app.py
- requirements.txt
- README.md
- .gitignore
- static/style.css
- templates/index.html
- tests/test_app.py

## 5. Installation Instructions

Clone the repository:

    git clone YOUR_REPOSITORY_URL

Navigate to the project directory:

    cd student-information-system

Create a virtual environment:

    python -m venv venv

Activate on Windows:

    venv\Scripts\activate

Install dependencies:

    python -m pip install -r requirements.txt

Run the application:

    python app.py

Open your browser:

    http://127.0.0.1:5000

## 6. Running Tests

Execute:

    python -m pytest -v

## 7. Future Enhancements

- Docker containerization.
- Amazon ECR image storage.
- Amazon EKS deployment.
- GitHub Actions CI/CD automation.
- Argo CD GitOps deployment.
