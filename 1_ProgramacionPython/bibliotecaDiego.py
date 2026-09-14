def distancia(r,θ,z):
    """Calcula la distancia entre un punto en coordenadas cilíndricas P(r,θ,z) al origen."""
    return (r**2+z**2)**(1/2)

def factorialDiego(n):
    """Calcula el factorial de un número entero positivo n."""
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac

def factorial(n):
    """Permite calcular el factorial de un número entero positivo n de forma recursiva."""
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def catalan(n):
    """Calcula el n-ésimo número de Catalán"""
    if n == 0:
        return 1
    elif n > 0:
        return (4*n-2)/(n+1)*catalan(n-1)

def mcd(m,n):
    """Encuentra el Máximo Común Divisor entre dos números enteros n y m positivos."""
    if n == 0:
        return m
    elif n > 0:
        return mcd(n, m % n)

def facprimos(n):
    "Descompone un número entero positivo mayor que dos en sus factores primos dentro de una lista."
    p = []
    
    for i in range(2,n+1):
        while n % i == 0:
            p.append(i)
            n = n//i
        if n == 1:
            break
    return p