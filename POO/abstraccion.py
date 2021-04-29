class Lavadora:
    def __init__(self):
        pass

    def iniciar_ciclo(self, temperatura='caliente'):
        self._llenar_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_de_agua(self, temperatura):
        print(f'Llenando de agua a temperatura: {temperatura}')
    def niveles(self):
        print
    def _anadir_jabon(self):
        print(f'Mezaclando el jabon')

    def _lavar(self):
        print(f'Remojando ropa')

    def _centrifugar(self):
        print('Motor girando tacatacatacatacataca')


if __name__ == '__main__':
    lavadora_lg = Lavadora()
    lavadora_lg.iniciar_ciclo()
