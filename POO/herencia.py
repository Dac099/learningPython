class Rectangulo:
    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo): #De esta forma se aplica herencia
    def __init__(self, lado):
        #Con super llamamos el constructor de la superclase y como parametros le pasamos el valor de la clase hila
        super().__init__(lado, lado)

if __name__ == '__main__':
    rectangulo = Rectangulo(3,4)
    print(rectangulo.area())

    cuadrado = Cuadrado(5)
    print(cuadrado.area())