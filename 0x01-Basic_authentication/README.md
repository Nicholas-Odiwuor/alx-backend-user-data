# 0x01. Basic Authentication

## 📚 Background Context

Authentication is a key step in securing APIs and applications. In this project, we build a custom **Basic Authentication** system in Python to understand how authentication works under the hood.

> ⚠️ Note: In production systems, always use established libraries or frameworks like `Flask-HTTPAuth` for security and reliability. This project is intended for educational purposes only.

---

## 🧠 Learning Objectives

- Understand the concept of user authentication
- Learn how HTTP Basic Authentication works (Base64 encoding, HTTP headers, credentials)
- Create a simple user model with hashed passwords
- Implement and apply authentication in a Flask API
- Secure API endpoints using your custom authentication class

---

## 🛠️ Requirements

### General

- All files will be interpreted/compiled on **Ubuntu 18.04 LTS** using `python3` (version 3.7)
- All files must end with a new line
- The first line of all scripts should be:
  ```bash
  #!/usr/bin/env python3

