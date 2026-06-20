def somar_todos_numeros(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(somar_todos_numeros(1, 2, 3))
print(somar_todos_numeros(10, 20, 30, 40))