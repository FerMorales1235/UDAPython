Adeudo = input ("El Alumno presenta adeudo de: ")
Adeudo = float (Adeudo)
if Adeudo >= 1 :
    print(f'El alumno tiene un adeudo de {Adeudo} y por lo tanto tiene falta')
else: 
    print("El alumno no presenta adeudo por lo tanto no tiene falta")


Faltas = input ("Numero de faltas del alumno: ")
Faltas = int (Faltas)
if Faltas >= 3 :
    print(f"El alumno tiene {Faltas} faltas por lo que esta Reprobado")
else: 
    print("El alumno esta Aprobado")
    

