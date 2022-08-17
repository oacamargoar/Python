print("Ingrese la edad")
edad = int(input())
while edad < 0:
    print("La edad no puede ser negativa")
    edad = int(input())
    continue
if(edad < 18):
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")