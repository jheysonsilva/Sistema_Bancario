# Menu de opções
menu = """
[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair
=> """

# Variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do sistema
while True:
    opcao = input(menu).strip().upper()

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Operação falhou! O valor precisa ser positivo.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("❌ Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("❌ Operação falhou! O valor do saque excede o limite de R$500,00.")
        elif excedeu_saques:
            print("❌ Operação falhou! Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("✅ Saque realizado com sucesso!")
        else:
            print("❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "E":
        print("\n📄 EXTRATO")
        print("Nenhuma movimentação registrada." if not extrato else extrato)
        print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
        print("-" * 30)

    elif opcao == "Q":
        print("👋 Obrigado por usar nosso sistema. Até mais!")
        break

    else:
        print("❌ Operação inválida. Por favor, selecione uma opção válida.")
