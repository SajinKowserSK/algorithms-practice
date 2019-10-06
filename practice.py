'''Write a recursive function that calculates base to the power of exponent in O(log n) run time'''


def calculate (base, exponent):
    if exponent == 1:
        return base

    else:
        if exponent % 2 == 0:
            return calculate(base, (exponent/2)) * calculate(base, (exponent/2))

        else:
            return calculate(base, ((exponent-1)/2)) * calculate(base, ((exponent-1)/2)) * base


print(calculate(2,3))
