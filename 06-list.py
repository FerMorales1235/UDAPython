lenguajes = {'Python','Kolin','Java','JavaScript'}
print(lenguajes)


#los arrays (lists) comienzan en la posicion
print(lenguajes[0]) #python

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

#Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

#modificando valores de un arreglo
lenguajes[2] = 'PHP'
print(lenguajes)

#agregar elementos a un arreglo (list)
lenguajes.append('Ruby')
print(lenguajes)

#eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

#eliminar de un arreglo (list)
lenguajes.pop() #eliminar el ultimo elemento
print(lenguajes)

#eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)

#eliminar por nombre
lenguajes.remove('PHP')
print(lenguajes)