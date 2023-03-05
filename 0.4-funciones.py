def informacion ():
    print('Fernando Morales')

informacion()
informacion()
informacion()

#________________________________________________________________________________________

def informacion2 (nombre, puesto = 'desconocido'):
    print(f'soy {nombre} y soy {puesto}')

informacion2('Pedro','Programador')
informacion2('Itzel','Diseñadora')
informacion2('Juan','Programador')

#________________________________________________________________________________________
def informacion3(nombre):
    return nombre

empleado = informacion3('Fernando')
print(empleado)