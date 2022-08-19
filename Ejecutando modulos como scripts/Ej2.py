import time as t

hora = t.strftime("%H")
min = t.strftime("%M")


if(int(hora) >= 19) :
    print(f"Ya son más de las 19:00 ¿Que esperas?, exactamente las {hora}:{min}")
else : 
    print(f"Faltan {19 - int(hora)} horas y {60 - int(min)} minutos para la salida")