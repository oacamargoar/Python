class Alumno :
    def __init__(self, nombre, nota) :
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self) -> str:
        return "Nombre: {}, Nota: {}".format( self.nombre, self.nota )
    
    def resultado(self) :
        if(self.nota >= 3) :
            print(str(self.nota) + " Aprobado")
        else :
            print(str(self.nota) + " Reprovado")

# La calificación va hasta 5, debe como minimo tener 3 para ganar (En mi caso)
alumno = Alumno("Omar Camargo Ardila", 4.8)
print(alumno)
alumno.resultado()