from memory_profiler import profile

# Original list-based approach
@profile
def numeros_primos(cantidad):
    count = 0
    aux = 2
    primos = []
    while count < cantidad:
        for i in range(2, aux):
            if aux % i == 0:
                break
        else:
            primos.append(aux)
            count += 1
        aux += 1
    return primos

# Generator-based approach
@profile
def numeros_primos_gen(cantidad):
    count = 0
    aux = 2
    while count < cantidad:
        for i in range(2, aux):
            if aux % i == 0:
                break
        else:
            yield aux
            count += 1
        aux += 1

print("List-based:")
numeros_primos(500)

print("\nGenerator-based:")
for p in numeros_primos_gen(500):
    pass