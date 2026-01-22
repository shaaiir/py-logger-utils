# Python Supply Chain Attack Simulation Lab

WARNING: STRICTLY FOR EDUCATIONAL & AUTHORIZED LAB USE ONLY

This repository demonstrates how software supply-chain attacks work using a controlled, ethical simulation.

No real secrets are stolen
No system exploitation occurs
Only lab-generated fake secrets are used

## Overview

Modern applications rely heavily on third-party libraries. Developers routinely install dependencies from GitHub or PyPI without deeply inspecting their internal behavior.

This lab demonstrates how a malicious Python library can:
- Look completely legitimate
- Be installed normally
- Execute hidden logic automatically
- Exfiltrate sensitive data silently

This is one of the most dangerous real-world attack vectors today.

## What Is a Supply Chain Attack

A software supply-chain attack occurs when an attacker compromises a trusted dependency instead of attacking the application directly.

Common targets include:
- Open-source libraries
- Build tools
- CI/CD pipelines
- Package managers

Instead of hacking you, the attacker hacks what you trust.

## Lab Objective

The objective of this lab is to help students understand:

- How malicious dependencies work
- Why executing code on import is dangerous
- How secrets stored in environment variables can leak
- Why developers often don't notice supply-chain attacks
- How defenders can detect and prevent these attacks

## How This Repository Works (High Level)

This repository contains a Python package that:

1. Executes code automatically when imported
2. Reads environment variables prefixed with LAB_
3. Sends those values to an instructor-controlled server
4. Continues program execution normally

Important
- Only variables starting with LAB_ are collected
- This prevents collecting real credentials
- This keeps the lab ethical and safe

## Attack Flow

Student installs library
↓
Student imports library in Python app
↓
Python executes init.py automatically
↓
Library reads LAB_* environment variables
↓
Data sent to instructor server
↓
Application runs normally

No pop-ups.
No warnings.
No crashes.

That is what makes supply-chain attacks dangerous.

## Repository Structure

py-logger-utils/
│
├── setup.py
├── py_logger_utils/
│ ├── __init__.py (Executes hidden logic on import)
│ └── collector.py (Collects LAB_* secrets)
└── README.md

## Instructor Setup

### Step 1: Start the Receiver Server

The instructor runs a simple HTTP server to receive lab data.

Example (Flask):

```python
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/collect", methods=["POST"])
def collect():
    data = request.json
    with open("exfiltrated_data.log", "a") as f:
        f.write(json.dumps(data) + "\n")
    return {"status": "received"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
