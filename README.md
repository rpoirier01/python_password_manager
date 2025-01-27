# Password Manager

A simple command-line password manager built using Python and SQLite to store website credentials securely.

## Features

- Store and manage website credentials (username, password, website), check password strength and generate strong passwords
- Credentials are stored in a SQLiteDB using hashing to protect the master password and encryption to protect website passwords
- Ability to add, view, delete and check how strong credentials are
- Automatically generates an encryption key: ensure it is securely stored with file-level encryption on your hard disk (responsibility for securing it lies with you).

### Prerequisites

- Python 3.x
- SQLite (comes built-in with Python)
- Dependencies listed in `requirements.txt`

### Steps to Install

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd password-manager

2. Setup a virtual environment with:
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies with:
    pip install -r requirements.txt
