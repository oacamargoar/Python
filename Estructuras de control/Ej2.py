print("Ingrese el limite inferior")
inf = int(input())
print("Ingrese el limite superior")
sup = int(input())
while(sup < inf):
  print("El limite inferior debe ser menor, ingrese el limite superior, sabiendo que el limite inferior es ", inf)
  sup = int(input())
print("Mostrar todos los números impares desde " + str(inf) + " hasta " + str(sup))
while(inf <= sup):
  if (inf%2 != 0):
    print(inf)
  inf += 1
print("Fin...")