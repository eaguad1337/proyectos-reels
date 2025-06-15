def decorador(func):
    def funcion_decorada(a, b):
        print("Inicio decorador")
        func(a, b)
        print("Fin decorador")
    return funcion_decorada

@decorador
def hola_mundo():
    print("hola mundo")

hola_mundo()