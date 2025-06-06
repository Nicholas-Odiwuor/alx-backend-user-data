# 0x03. User Authentication Service

## Description
This project walks through the fundamental mechanisms of building an authentication system using **Flask**, focusing on learning by doing. While production systems should use established libraries (e.g., `Flask-User`), this exercise helps understand how authentication works under the hood.

## Learning Objectives
You should be able to explain:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements
- OS: Ubuntu 18.04 LTS
- Python: 3.7
- Code Style: `pycodestyle` 2.5
- All files must:
  - Start with `#!/usr/bin/env python3`
  - Be executable and end with a new line
  - Be well-documented (modules, classes, methods)
  - Be type annotated
  - Pass `wc` length checks

## Technical Constraints
- Use **SQLAlchemy 1.3.x**
- Use **bcrypt** (`pip3 install bcrypt`)
- Flask app must only use `Auth` class (not interact directly with DB)
- Use only public methods of `Auth` and `DB`

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Requests Module](https://requests.readthedocs.io/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Setup
Install `bcrypt` dependency:
```bash
pip3 install bcrypt

