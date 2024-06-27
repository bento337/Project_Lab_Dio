menu = '''
   [d] Depositar
   [s] Sacar
   [e] Extrato
   [q] Sair

=> '''

saldo = 0
limite = 500
extrato = "============= Extrato ============="
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito: ")
        valor = int(input("Informe o valor que deseja depositar: "))
        if valor > 0:
           saldo += valor
           extrato = f"Depósito de {str(valor)} reais"
        else: 
           print("Valor inválido")

    elif opcao == "s":
        if(numero_saques<LIMITE_SAQUES):
          print("Saque: ")
          valor = int(input("Informe o valor que deseja sacar: "))
          if valor <= limite:
             saldo -= valor
             numero_saques += 1
             extrato += f"Saque de {str(valor)} reais"
        else:
           print("Operação inválida, o límite de saques diários foi excedido.")
           print(extrato)
           break

    elif opcao == "e":
        print(extrato)
        print(f"O saldo atual é de {saldo}")
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")