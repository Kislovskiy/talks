from toolz import curry


@curry
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        raise ValueError(f"Error: {e}")


if __name__ == "__main__":
    try:
        result = divide(10)(0)
    except ValueError as e:
        print(f"Error handling: {e}")
