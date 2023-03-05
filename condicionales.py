# Revisar si una condicion es mayot a
balance = 500
if balance > 0:
    print('Puede pagar')
else:
    print('No tiene saldo')

#Likes
    Likes = 200
    if Likes == 200:
        print('Excelente, 200 likes')
    else: 
        print('Casi llegas a los 200')


#If con texto
lenguaje = 'PHP'
if not lenguaje == 'Pythun':
    print('Excelent Desicion')

#Evaluar un Booleano
usuario_autentificado = True

usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin: 
        print('ACCESO TOTAL')
    else:
        print('Acceso al sistema')
else:
    print('Debes iniciar sesion')