class Personaje:
    def __init__(self,habilidades, nombre,sexo,lugar_de_origen):
        self.habilidades = habilidades
        self.nombre = nombre
        self.sexo = sexo
        self.origen = lugar_de_origen
        self.vida = 100
    
    def moverse(self):
        print(f'{self.nombre} se esta moviendo')
    
    def interactuar(self, habilidad):
        if habilidad in self.habilidades:
            print(f'{self.nombre} utiliza {habilidad}')
        else:
            print(f'Aun no adquieres {habilidad}')


class Soporte(Personaje):
    def __init__(self, vida, rasgo, arma, nombre, sexo, origen, habilidades):
        super().__init__(habilidades, nombre, sexo, origen)
        self.vida = vida
        self.rasgo = rasgo
        self.arma = arma
    
if __name__ == '__main__':
    ugarus = Soporte(90,'alienigena','arco','ugarus','indefinido',{'altura':1234,'longitud':567,'profundidad':85798},['atacar','defenderse', 'curar'])

    print(ugarus.habilidades)
    ugarus.moverse()
    ugarus.interactuar('atacar')
        