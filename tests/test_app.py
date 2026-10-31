
import pytest
import tempfile
import os

from app import app, init_db


@pytest.fixture
def client():

    db_fd, db_path = tempfile.mkstemp()

    app.config["DATABASE"] = db_path
    app.config["TESTING"] = True

    with app.app_context():
        init_db()

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)


def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200


def test_add_student(client):

    response = client.post("/add", data={
        "name": "Rahul",
        "roll_number": "101",
        "course": "BCA"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Rahul" in response.data


def test_search_student(client):

    client.post("/add", data={
        "name": "Rahul",
        "roll_number": "101",
        "course": "BCA"
    })

    response = client.get("/?search=Rahul")

    assert b"Rahul" in response.data


def test_delete_student(client):

    client.post("/add", data={
        "name": "Rahul",
        "roll_number": "101",
        "course": "BCA"
    })

    response = client.post(
        "/delete/1",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Rahul" not in response.data
