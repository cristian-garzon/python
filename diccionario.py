empleados={}
op=""
while op!='6':
    op=input('MENU \n1.añadir cliente\n2.eliminar cliente\n3.mostrar cliente\n4.listar usuarios\n5.clientes preferentes\n6.terminar programa\nelija una opcion: ')
    if op=='1':
        identificador=input("id: ")
        nombre=input("nombre: ")
        direccion=input("direccion: ")
        tel=input("telefono: ")
        correo=input("correo: ")
        preferente=input("es preferente? s/n: ")
        empleado={'nombre':nombre,'direccion':direccion,'telefono':tel,'correo':correo,'preferente':preferente=='s'}
        empleados[identificador]=empleado
    if op=='2':
        identificador=input("que id eliminamos: ")
        if identificador in empleados:
            del empleados[identificador]
        else:
            print("no se encontro el empleado")
    if op=='3':
        identificador=input("id del empleado a mostrar: ")
        if identificador in empleados:
            for key,valor in empleados[identificador].items():
                print(key,valor)
        else:
            print("no se encontro el empleado")
    if op=='4':
        for i, j in empleados.items():
            print(i,j['nombre'])
    if op=='5':
        for i, j in empleados.items():
            if j['preferente']:
                print(i,j['nombre'])