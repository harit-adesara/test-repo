def calculate_area(radius):
    import math
    return math.pi * radius ** 2


def print_result():
    area = calculate_area(5)
    print(f"Area: {area}")


if __name__ == "__main__":
    print_result()