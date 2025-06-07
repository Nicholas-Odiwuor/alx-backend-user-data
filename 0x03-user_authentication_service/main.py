#!/usr/bin/env python3
"""
End-to-End Integration Test for User Authentication Service
"""
import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Test user registration"""
    payload = {"email": email, "password": password}
    res = requests.post(f"{BASE_URL}/users", data=payload)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "user created"}

    # Registering same user again should return 400
    res = requests.post(f"{BASE_URL}/users", data=payload)
    assert res.status_code == 400
    assert res.json() == {"message": "email already registered"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login with incorrect password"""
    payload = {"email": email, "password": password}
    res = requests.post(f"{BASE_URL}/sessions", data=payload)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test login with correct credentials"""
    payload = {"email": email, "password": password}
    res = requests.post(f"{BASE_URL}/sessions", data=payload)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "logged in"}
    return res.cookies.get("session_id")


def profile_unlogged() -> None:
    """Test access to profile without login"""
    res = requests.get(f"{BASE_URL}/profile")
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test access to profile with valid session_id"""
    cookies = {"session_id": session_id}
    res = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert res.status_code == 200
    assert "email" in res.json()


def log_out(session_id: str) -> None:
    """Test logout"""
    cookies = {"session_id": session_id}
    res = requests.delete(f"{BASE_URL}/sessions", cookies=cookies)
    assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """Test requesting a password reset token"""
    res = requests.post(f"{BASE_URL}/reset_password", data={"email": email})
    assert res.status_code == 200
    data = res.json()
    assert "reset_token" in data
    return data["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test updating password with reset token"""
    payload = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    res = requests.put(f"{BASE_URL}/reset_password", data=payload)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


# Test runner
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)

