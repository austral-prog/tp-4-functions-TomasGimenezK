# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""

    if x>y:
        return x
    elif y>x:
        return y
    else:
        return x

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x >= y and x >= z:
        return x
    elif y >= z and y > x:
        return y
    elif z > x and z > y:
        return z




print(max_of_three(0,0,0))
print(max_of_two(0,0))
