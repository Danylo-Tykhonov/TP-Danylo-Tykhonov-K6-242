import math

def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c

def korni(a: float, b: float, c: float):
    D = discriminant(a, b, c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

a, b, c = 1, -3, 2
roots = korni(a, b, c)
print("Корні рівняння:", roots)
