from datetime import datetime
import logging

def log(message):
    current = datetime.now().strftime("%H:%M:%S")
    print(f"[{current}] {message}")

logger = log