divisa = {
    'euro':'€',
    'dollar':'$',
    'yen':'¥'
}

divisa_usuario = input('Dame la divisa de tu pais: ')
if divisa_usuario in divisa:
    print(divisa[divisa_usuario])
else:
    print('Divisa no encontrada')