#Función para crear archivo
def setLista(file, datos) :
    f = open(file, 'w')
    
    for h in datos :
        if not h.endswith('\n') == True:
            h += '\n'
        
        f.write(h)

    f.close()
#Lista que contiene los datos
hobbies = [
    '* Aprende Py',
    '* Aprender Java',
    '* Aprender para ser FullStack'
]
#Llamamos a la función y pasamos por parametro
setLista('hobbies.txt', hobbies)
#Abriremos el archivo
file = open('hobbies.txt', 'r')
lineas = file.read()
file.close()
#Imprime las lineal del archivo
print(lineas)