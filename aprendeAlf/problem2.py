verduleria = {
    'Platano': 1.35,
    'Naranja': 1.00,
    'Jitomate': 2.00,
    'Zarzamora': 4.00
}

pedido = input('Verdura a comprar: ')

if pedido in verduleria:
    cantidad = float(input('Kilos a comprar: '))
    print(cantidad*verduleria[pedido])
else:
    print('No contamos con ese producto')