# Hacer un ciclo que se ejecute 10 veces
# debe pedir 2 numeros por teclado
# en cada vuelta y decir cual es mayor
# de los dos

for i in range(10):
    # todo lo que pongas acá se ejecutará 10 veces
    print("Vuelta", i)
    num1 = int(input('Num1: ')) # a
    num2 = int(input('Num2: ')) # b

    if num1 > num2:
        print("Num1 es mayor")
    elif num1 < num2:
        print("Num2 es mayor")
    else:
        print("Son iguales")