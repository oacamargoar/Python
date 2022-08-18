def bisiesto():
  a = int(input("Ingresar un año: "))

  if(a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)):
      print(f"El año {a} es bisiesto!")
  else:
      print(f"El año {a} NO es bisiesto!")

bisiesto()