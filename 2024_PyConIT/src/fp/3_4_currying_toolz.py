from toolz import curry


def add_three_numbers(x, y, z):
    return x + y + z


curried_add = curry(add_three_numbers)

if __name__ == "__main__":
    # Partial application
    add_five = curried_add(2)(3)

    # Full application
    result = add_five(5)

    print(result)  # Output: 10
