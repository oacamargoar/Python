class Calculadora :

    def __init__(self, n1, n2) :
        self.n1 = n1
        self.n2 = n2

    def sum(self) :
        return ( self.n1 + self.n2)
    
    def res(self) :
        return ( self.n1 - self.n2)
    
    def mul(self) :
        return ( self.n1 * self.n2)
    
    def div(self) :
        if( self.n2 == 0 ) :
            return "No se puede dividir entre cero"
        else :
            return ( self.n1 / self.n2)
