# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    determinante = b**2 - 4 * a * c
    bhaskara_mas = (-b + (determinante)**(1/2)) / (2 * a)
    bhaskara_menos = (-b - (determinante)**(1/2)) / (2 * a)

    if determinante > 0:
        return f"({bhaskara_mas}, {bhaskara_menos})"
    if determinante < 0:
        return f"( )"
    if determinante == 0:
        return f"({bhaskara_mas})"


def value_y(a, b, c, x):
    Y = a*x**2 + b*x + c
    return Y


def to_string(a, b, c):
    if a == 0:
        if b == 0:
            hola = f"f(x) = {c}"
            return hola
        elif c == 0:
            hola = f"f(x) = {b} * X"
            return hola
        else:
            hola = f"f(x) = {b} * X + {c}"
            return hola
    elif b == 0:
        if c == 0:
            hola = f"f(x) = {a} * X^2"
            return hola
        else:
            hola = f"f(x) = {a} * X^2 + {c}"
            return hola
    elif c == 0:
        hola = f"f(x) = {a} * X^2 + {b} * X"
        return hola
    else:
        hola = f"f(x) = {a} * X^2 + {b} * X + {c}"
        return hola



def derivation(a, b, c):
    if a == 0:
        derivadarda = f"f'(x) = {b}"
        return derivadarda
    elif b == 0:
        derivadarda = f"f'(x) = {2 * a} * X"
        return derivadarda
    else:
        derivadarda = f"f'(x) = {2 * a} * X + {b}"
        return derivadarda

