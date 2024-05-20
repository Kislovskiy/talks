def plus(a):
    def add(b):
        return a + b

    return add


if __name__ == "__main__":
    result = plus(2)(3)
    # Partial apply, transform binary function to unary function
    plusTwo = plus(2)
    print(plusTwo(3))
