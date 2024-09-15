# Função principal do sistema bancário
def banco():
    saldo = 0.0
    extrato = []
    LIMITE_SAQUES = 3
    SAQUE_MAXIMO = 500.0
    saques_diarios = 0

    while True:
        print("\n==== Sistema Bancário ====")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Visualizar Extrato")
        print("[0] Sair")
        
        opcao = input("Escolha uma operação: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == '2':
            valor = float(input("Digite o valor do saque: R$ "))
            saldo, extrato, saques_diarios = sacar(saldo, extrato, valor, saques_diarios, LIMITE_SAQUES, SAQUE_MAXIMO)

        elif opcao == '3':
            exibir_extrato(saldo, extrato)

        elif opcao == '0':
            print("Obrigado por usar o sistema bancário!")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Função de depósito
def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

# Função de saque
def sacar(saldo, extrato, valor, saques_diarios, LIMITE_SAQUES, SAQUE_MAXIMO):
    if saques_diarios >= LIMITE_SAQUES:
        print("Limite de saques diários atingido!")
    elif valor > SAQUE_MAXIMO:
        print(f"O limite máximo por saque é de R$ {SAQUE_MAXIMO:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, saques_diarios

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n==== Extrato Bancário ====")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================")

# Inicializa o sistema
banco()