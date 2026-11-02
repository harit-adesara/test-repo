from datetime import datetime


def logger(message):
    log(message)

def log(message):
    current = datetime.now().strftime("%H:%M:%S")
    print(f"[{current}] {message}")