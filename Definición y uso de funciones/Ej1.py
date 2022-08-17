import math

def areaTriangulo(b: float, h: float):
    return ( b * h / 2 )

def areaCirculo(r: float):
    return  (math.pi * r**2 )

print(f"El area del triangulo es: {areaTriangulo(5, 8)}")
print(f"El area del circulo es: {round(areaCirculo(8), 3)}")