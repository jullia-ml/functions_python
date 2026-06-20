def exibir_status(logado):
    if logado:
        print("Acesso concedido")
    else:
        print("Acesso negado")

exibir_status(True)
exibir_status(False)