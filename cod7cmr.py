#lista para tipos selecionar tipos de apartamentos, informando o valor total a pagar
#como havia pedido o professor oscar na aula de terça feira
#pip install colorama
import os
while True:
    from colorama import Fore, Style, init

    init()
    
    os.system("cls")
    print(f'''{Fore.BLUE}
     _   _  ____  ________ _______ ___          ___      ________ ________
    | | | |/ __ \\|___  ___|  ______|  |         |  |    |  ______|   _____|
    | |_| | |  | |  |  |  |  |_____|  |         |  |    |  |_____|  |____
    |  _  | |  | |  |  |  |  ______|  |         |  |    |   _____|  _____|
    | | | | |__| |  |  |  |  |_____|  |____     |  |____|  |_____|  |
    |_| |_|\\____/   |__|  |________|_______|    |_______|________|__|
    {Style.RESET_ALL}''')

    tipos_lista1 = [20.00, 28.00, 35.00, 42.00, 48.00, 53.00]  # Tipos 1 ao 6
    tipos_lista2 = [28.00, 35.00, 42.00, 50.00, 57.00, 63.00]  # Tipos 7 ao 12

    # Função para exibir os valores de uma lista
    def exibir_lista(lista):
        for i, valor in enumerate(lista, start=1):
            print(f"{Fore.GREEN}{i} - R${valor:.2f}{Style.RESET_ALL}")

    # A lista
    nome=input("Digite seu nome: ")
    print("Selecione qual tipo de apartamento deseja: ")
    print("1 - Apartamento 1 ao 6")
    print("2 - Apartamento 1 ao 6")
    escolha_lista = input("Digite o número da lista que deseja visualizar (1 ou 2): ")

    if escolha_lista == "1":
        print("\nVocê selecionou a Lista 1 (Escolha um dos apartamentos 1 a 6): ")
        exibir_lista(tipos_lista1)
        escolha = int(input("\nEscolha um apartamento do tipo 1 a 6: ")) - 1
        if 0 <= escolha < len(tipos_lista1):
            valor_selecionado = tipos_lista1[escolha]

    elif escolha_lista == "2":
        print("\nVocê selecionou a Lista 2 (Escolha um dos apartamentos 1 a 6): ")
        exibir_lista(tipos_lista2)
        escolha = int(input("\nEscolha um apartamento do tipo 1 a 6: ")) - 1
        if 0 <= escolha < len(tipos_lista2):
            valor_selecionado = tipos_lista2[escolha]
    else:
        print("Opção inválida! Por favor, escolha entre as listas 1 e 2.")
        exit()

    # Solicitar quantidade de pessoas e dias
    try:
        qtd_pessoas = int(input("\nInforme a quantidade de pessoas: "))
        qtd_dias = int(input("Informe a quantidade de dias que ficará hospedado: "))
        if qtd_pessoas > 0 and qtd_dias > 0:
            total = valor_selecionado * qtd_pessoas * qtd_dias
            
            print("A reserva está no nome de: ", nome)
            print("Quantidade de dias: ", qtd_dias)
            print("Quantidade de Pessoas: ",qtd_pessoas)
        else:
            print("Por favor, insira valores positivos para pessoas e dias.")
        novo_cadastro = input("deseja continuar ou fazer uma nova reserva (Digite sim ou não): ").strip().lower()

        if novo_cadastro == 'não':
            os.system("cls")
            print("Reserva efetuada com sucesso")
            print(f"A reserva está no nome de:  {Fore.CYAN}{nome}{Style.RESET_ALL}")
            print(f"Quantidade de dias: {Fore.RED}{qtd_dias}{Style.RESET_ALL}")
            print(f"Quantidade de Pessoas: {Fore.RED}{qtd_pessoas}{Style.RESET_ALL}")
            print(f"\nO total a pagar é de: {Fore.GREEN}R${total:.2f}{Style.RESET_ALL}")
            input("Aperte enter para finalizar!")
            break

    except ValueError:
        print("Por favor, insira números válidos para pessoas e dias.")
