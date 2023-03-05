#Funcion sin parametro
def nombreFuncion():
    print("Mensaje")
nombreFuncion()

#Funcion con parametro
def nombreFuncionConParametro(Parametro):
    print("Este es el parametro: " + Parametro)
nombreFuncionConParametro("Este es el Argumento del parametro")

#Funcion con multiples parametros
def nombreFuncionConMultiplesParametros(parametro1, parametro2):
    print("Estos son los valores de los multiples parametros: " + parametro1, parametro2)
nombreFuncionConMultiplesParametros("Este es el Argumento 1", "Este es el Argumento 2")