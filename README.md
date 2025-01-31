# Password Manager

A simple command-line password manager built using Python and SQLite to store website credentials securely. It stores passwords locally and securely and logs security related events to a Splunk server (located on the same network).

## Features

- Store and manage website credentials (username, password, website), check password strength and generate strong passwords
- Credentials are stored in a SQLiteDB using hashing to protect the master password and encryption to protect website passwords
- Ability to add, view, delete and check how strong credentials are
- Automatically generates an encryption key: ensure it is securely stored with file-level encryption on your hard disk (responsibility for securing it lies with you).
- Sends security-related event logs to a Splunk server for monitoring, including:
  - **Failed master password login attempts** (Warning)
  - **Adding a new password** (Info/Warning based on strength)
  - **Updating an existing password** (Info/Warning based on strength)

## Why This Project?

- This project demonstrates secure credential storage, password encryption and hashing and implements event logging to a centralized server. These are key concepts in cybersecurity and system monitoring that this project provided hands-on experience with


## Viewing Results in Splunk
- To see security related events in Splunk from this application, search with: source="udp:514" index="main"

### Prerequisites

- Python 3.x
- SQLite (comes built-in with Python)
- A Splunk server must be running (IP address specified in config.json, e.g., { "ip": "192.168.1.100" })
- Dependencies listed in `requirements.txt`

### Steps to Install

1. Clone this repository:
   git clone <repository_url>
   cd password-manager

2. Setup a virtual environment with:
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies with:
    pip install -r requirements.txt
