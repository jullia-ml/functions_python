contador = 0

def incrementar_contador():
    global contador
    contador = contador + 1

incrementar_contador()
print("valor do contador global:", contador)