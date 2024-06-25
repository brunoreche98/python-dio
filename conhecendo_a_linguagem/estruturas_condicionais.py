opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato \n[3] Outros"))
extrato = 1000

if opcao == 1:
    sacar = input("Quanto você gostaria de sacar?")
    print(sacar)
elif opcao == 2:
    print(f"Sua conta tem saldo de: {extrato}")
elif opcao == 3:
    input("O que você deseja?")
else: 
    input("Encerrando aplicação")