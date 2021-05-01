base_de_datos = {
    'NIF-A':{
        'Nombre':'Juan Garza',
        'Direccion':'Toluca',
        'Telefono':437498249,
        'Correo':'@gmail',
        'Preferente': False
        },
    'NIF-B':{
        'Nombre':'Daniel Campos',
        'Direccion':'Metepec',
        'Telefono':9989747243,
        'Correo':'@hotmail',
        'Preferente': False
        },
    'NIF-C':{
        'Nombre':'Maria Orquesta',
        'Direccion':'San Mateo',
        'Telefono':6522985489,
        'Correo':'@Platzi',
        'Preferente': False
        },
    'NIF-D':{
        'Nombre':'Pedro Infente',
        'Direccion':'San Gaspar',
        'Telefono':376944452,
        'Correo':'@indeed',
        'Preferente': True
        },
    'NIF-E':{
        'Nombre':'Sarah Rosa',
        'Direccion':'Jalisco',
        'Telefono':387498752,
        'Correo':'@toluca',
        'Preferente': True
        },
    'NIF-C':{
        'Nombre':'Jesus Salvador',
        'Direccion':'Michoacan',
        'Telefono':309598375982,
        'Correo':'@jovenes',
        'Preferente': True
        },
    'NIF-A':{
        'Nombre':'Judas Bueno',
        'Direccion':'Veracruz',
        'Telefono':35892759823,
        'Correo':'@youth',
        'Preferente': False
        },
    'NIF-D':{
        'Nombre':'Malcom Serie',
        'Direccion':'Sonora',
        'Telefono':398752892,
        'Correo':'@malcom',
        'Preferente': False
        },
    'NIF-B':{
        'Nombre':'Reesse Orden',
        'Direccion':'Yucatan',
        'Telefono':375298752,
        'Correo':'@dell',
        'Preferente': True
        },
    'NIF-E':{
        'Nombre':'Odin del Mes',
        'Direccion':'Campeche',
        'Telefono':3860980252,
        'Correo':'@logitech',
        'Preferente': True
        },
}

while True:
    opc = input("""Ingrese una opcion: 
    [1] Agregar usuario
    [2] Eliminar usuario
    [3] Mostrar usuario
    [4] Mostrar todos los usuarios
    [5] Mostrar usuarios preferentes
    [6] Salir del programa 
    >> """)
    if opc == '1':
        # Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
        datos_cliente = dict()
        datos_cliente['Nombre'] = input('Ingrese el nombre del cliente: ')
        datos_cliente['Direccion'] = input('Ingrese la direccion del cliente: ')
        datos_cliente['Telefono'] = input('Ingrese el telefono del cliente: ')
        datos_cliente['Correo'] = input('Ingrese el correo del cliente: ')
        preferencia = input('El cliente es preferente? [y/n]: ')
        if preferencia == 'y': 
            datos_cliente['Preferente'] = True  
        else:
            datos_cliente['Preferente'] = False
        nif_cliente = input('Ingrese la NIF del cliente [NIF-Letra]: ')
        base_de_datos[nif_cliente] = datos_cliente
        break
    elif opc == '2':
        # Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
        pass
    elif opc == '3':
        # Preguntar por el NIF del cliente y mostrar sus datos.
        pass
    elif opc == '4':
        # Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
        pass
    elif opc == '5':
        # Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
        pass
    elif opc == '6':
        # Terminar el programa.
        break
exit()