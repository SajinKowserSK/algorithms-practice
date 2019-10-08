'''calculate given base to given power using recursion'''

def calculate (base, power):
    if power == 1:
        return base

    else:
        if power % 2 == 0: # power is even
            return calculate(base, power/2) * calculate(base, power/2)

        else: # power is odd
            return calculate(base, (power-1)/2) * calculate(base, (power-1)/2) * base


print(calculate(2,4))
print(calculate(2,3))
