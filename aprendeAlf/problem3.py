base_de_datos = dict()

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
        nif_cliente = input('Ingrese la NIF del cliente [NIF-Letra]: ')
        base_de_datos[nif_cliente] = dict()
        base_de_datos[nif_cliente]['Nombre'] = input('Ingrese el nombre del cliente: ')
        base_de_datos[nif_cliente]['Direccion'] = input('Ingrese la direccion del cliente: ')
        base_de_datos[nif_cliente]['Telefono'] = input('Ingrese el telefono del cliente: ')
        base_de_datos[nif_cliente]['Correo'] = input('Ingrese el correo del cliente: ')
        preferencia = input('El cliente es preferente? [y/n]: ')
        if preferencia == 'y': 
            base_de_datos[nif_cliente]['Preferente'] = True  
        else:
            base_de_datos[nif_cliente]['Preferente'] = False
        print(f'Cliente {nif_cliente} agregado')
        continue
    elif opc == '2':
        # Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
        nif_cliente = input('Ingrese la NIF del cliente [NIF-Letra]: ')
        del base_de_datos[nif_cliente]
        print(f'Cliente {nif_cliente} eliminado')
        continue
    elif opc == '3':
        # Preguntar por el NIF del cliente y mostrar sus datos.
        nif_cliente = input('Ingrese la NIF del cliente [NIF-Letra]: ')
        if nif_cliente in base_de_datos:
            for key in base_de_datos[nif_cliente]:
                print(f'{key}   {base_de_datos[nif_cliente][key]}')
        else: 
            print(f'Cliente {nif_cliente} no encontrado')
        continue
    elif opc == '4':
        # Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
        for indice in base_de_datos:
            for key in base_de_datos[indice]:
                print(f'{key}   {base_de_datos[indice][key]}')
        continue
    elif opc == '5':
        # Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
        for indice in base_de_datos:
            if base_de_datos[indice]['Preferente'] == True:
                print(base_de_datos[indice]['Nombre'],'\t', indice)
        continue
    elif opc == '6':
        # Terminar el programa.
        break
exit()