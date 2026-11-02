from datetime import datetime


from datetime import datetime


def logger(message):
    current = datetime.now().strftime("%H:%M:%S")
    print(f"[{current}] {message}")