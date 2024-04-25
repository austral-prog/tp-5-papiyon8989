def roots(a, b, c):

    dis = (b**2)-4*a*c
    r1 = (-b + dis**0.5) / (2*a)
    r2 = (-b - dis**0.5) / (2*a)

    if  dis > 0:
        return f"({r1}, {r2})"

    if dis == 0:
        r1 = -b / (2 * a)
        return f"({r1})"

    if dis < 0:
        return "( )"

def value_y(a, b, c, x):

    return (a*(x**2))+(b*x)+(c)

def to_string(a, b, c):

    if a != 0 and b != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a != 0 and c != 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif b != 0 and c != 0:
        return f"f(x) = {b} * X + {c}"
    elif a != 0:
        return f"f(x) = {a} * X^2"
    elif b != 0:
        return f"f(x) = {b} * X"
    elif c != 0:
        return f"f(x) = {c}"
    else:
        return "f(x) = 0"


def derivation(a, b, c):

    if a != 0 and b != 0:
        return f"f'(x) = {2 * a} * X + {b}"

    elif a == 0 and b != 0:
        return f"f'(x) = {b}"

    elif a != 0 and b == 0:
        return f"f'(x) = {2 * a} * X"
        
    else:
        return "f'(x) = 0"
