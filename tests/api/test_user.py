import pytest
from django.contrib import auth
from django.contrib.auth import user_logged_in, user_logged_out
from django.template.context_processors import request
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import Product

client = APIClient()


'''
Integration testing 
'''


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        name="Tamer",
        email="tamer@gmail.com",
        password="t12345678"
    )

    response = client.post("/api/users/register/", payload)
    data = response.data
    assert payload["name"] == data["name"]
    assert payload["email"] == data["username"]  # if we put email instead of username , the test is failed ,why?
    assert payload["password"] not in data  # because of hashing?


@pytest.mark.django_db
def test_login_user():
    payload = dict(
        name="Tamer",
        email="tamer@gmail.com",
        password="t12345678"
    )

    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", dict(username="tamer@gmail.com", password="t12345678"))
    assert response.data['name'] == payload['name']
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_user_fail():  # user not exist
    response = client.post("/api/users/login/", dict(username="assi@gmail.com", password="t12345678"))
    assert response.status_code == 401

@pytest.mark.django_db
def test_if_profile_exist_after_login():
    payload = dict(
        name="testing123",
        email="test11@test.com",
        username="test11",
        password="t1234567"
    )
    client.post("/api/users/register/", payload)
    response = client.post("/api/users/login/", {"username": "test11@test.com", "password": "t1234567"})
    # response = client.get('http://127.0.0.1/#/profile')
    assert response.status_code == 200

# @pytest.mark.django_db
# def test_logout():
#     payload = dict(
#         name="Tamer",
#         email="tamer@gmail.com",
#         password="t12345678"
#     )
#
#     client.post("/api/users/register/", payload)
#     client.post("/api/users/login/", dict(username="tamer@gmail.com", password="t12345678"))
#
#     response = client.get("/api/users/profile/")
#     client.logout()
#     response = client.get("/api/users/profile/")
#
#     assert response.status_code == 405  # invalid user

# 1
