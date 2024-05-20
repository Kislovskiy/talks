def compose(*functions):
    """
    Compose multiple functions: f(g(...(h(x))))
    """

    def composed_function(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result

    return composed_function


# Example functions
def square(x):
    return x**2


def add_one(x):
    return x + 1


def double(x):
    return x * 2


def to_s(s):
    return f"final result {str(s)}"


if __name__ == "__main__":
    pipeline = compose(to_s, square, add_one, double)
    print(f"Result: {pipeline(3)}")
