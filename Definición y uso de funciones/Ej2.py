def numPrimo():
  num = int(input('Ingrese un número entero: '))
  t = 0
  for i in range(2, int(num)) :
    if(num%i == 0) :
      t += 1
  if(t != 0) :
    print(f"{num} No es un número primo")
  else :
    print(f"{num} Es un número primo")

numPrimo()