import json
import random
import string


def generate_user_id():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


def validate_name(name):
    return len(name) >= 3


def calculate_bonus(salary):
    return salary * 0.10


def read_config():
    config = '{"company":"OpenAI","version":"1.0"}'
    return json.loads(config)


def create_employee(name, salary):
    if not validate_name(name):
        raise ValueError("Invalid name")

    return {
        "id": generate_user_id(),
        "name": name,
        "salary": salary,
        "bonus": calculate_bonus(salary),
    }


def print_employee(emp):
    print("-" * 40)
    print(f"ID      : {emp['id']}")
    print(f"Name    : {emp['name']}")
    print(f"Salary  : {emp['salary']}")
    print(f"Bonus   : {emp['bonus']}")
    print("-" * 40)


def dummy_function_1():
    return sum(range(10))


def dummy_function_2():
    return sum(range(20))


def dummy_function_3():
    return sum(range(30))


def dummy_function_4():
    return sum(range(40))


def dummy_function_5():
    return sum(range(50))


def dummy_function_6():
    return sum(range(60))


def dummy_function_7():
    return sum(range(70))


def dummy_function_8():
    return sum(range(80))


def dummy_function_9():
    return sum(range(90))


def dummy_function_10():
    return sum(range(100))


def report():
    emp = create_employee("Harit", 50000)
    print_employee(emp)

    cfg = read_config()
    print(cfg)


if __name__ == "__main__":
    report()