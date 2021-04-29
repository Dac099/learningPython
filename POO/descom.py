class Car:
    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(5)

        self._estado = 'en movimiento'

    def aparcar(self):
        self._estado = 'apagado'
        


class Motor:
    def __init__(self, cilindros, tipo='gasolina'):        
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura

    def inyecta_gasolina(self, cantidad):
        self.cantidad = cantidad

