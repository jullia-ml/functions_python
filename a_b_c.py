def somar(a, b, c):
    return a + b + c

def media(a, b, c):
    return (a + b + c) / 3

def maior(a, b, c):
    return (a, b, c)

def menor(a, b, c):
    return (a, b, c)

a = int(input("insira um numero A: "))
b = int(input("insira um numero B: "))
c = int(input("insira um numero C: "))

print(somar(a, b, c))
print(media(a, b, c))
print(f"o maior valor é: {max(maior(a, b, c))}")
print(f"o menor valor é: {min(menor(a, b, c))}")
