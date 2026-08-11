def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))

print(f"resultado da soma: {(somar(a, b))}")
print(f"resultado da subtração: {(subtrair(a, b))}")
print(f"resultado da multiplicação: {(multiplicar(a, b))}")
print(f"resultado da divisão: {(dividir(a, b))}")