#Los decoradores son funciones que extienden la funcionalidad de otras funciones
#Un decorador en una funcion que recibe otra funcion como parametro y retorna otra funcion

def saludar(nombre):
    print(f'Hola {nombre}')


def prsentarse(nombre):
    print(f'Mi nombre {nombre} y estudio data science')


def consume_funciones(llamada_a_funcion):
    return llamada_a_funcion('Aby')

#Se hace el llamado de la funcion 
consume_funciones(saludar)


def funcion_decoradora(funcion):
    def wrapper():
        print('Mensaje uno')
        funcion()
        print('Mensaje dos')
    return wrapper()

#Utilizamos en @ con el nombre de nuestra funcion decoradora. Haciendo esto evitamos esto:
#zumbido = funcion_decoradora(zumbido)
@funcion_decoradora
def zumbido():
    print('bzzzzz!')
