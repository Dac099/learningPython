class Millas:
    def __init__(self, distancia = 0):
        self.distancia = distancia
    
    def transformar_a_millas(self):
        return (self.distancia * 1.609)
    
    #Metodo getter
    @property
    def obtener_distancia(self):
        print('getter method')
        return self._distancia  
    
    #Metodo setter
    @obtener_distancia.setter
    def definir_distancia(self,valor):
        if valor < 0:
            raise ValueError('Does not possible convert under 0')
        else:
            print('setter method')
            self._distancia = valor

    #Eliminar un atributo
    def eliminar_distancia(self):
        del self.distancia

    #property(fget, fset, fdel, fdoc)
    # distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)


avion = Millas()
avion.distancia = 500

print(avion.distancia)