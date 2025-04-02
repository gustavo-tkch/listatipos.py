import os
from colorama import Fore, Style, init

# Inicia a biblioteca colorama
init()

# Função para exibir os valores de uma lista
def exibir_lista(lista):
    for i, valor in enumerate(lista, start=1):
        print(f"{Fore.GREEN}{i} - R${valor:.2f}{Style.RESET_ALL}")

# Função para exibir os resultados em uma tabela no terminal
def exibir_resultados(user, qtd_pessoas, qtd_dias, total, parcelas=None, valor_parcela=None):
    os.system("cls")

    # Cabeçalho da tabela
    print(f"{Fore.CYAN}+{'-'*44}+")
    print(f"{Fore.CYAN}|{'DETALHES DA RESERVA':^44}|")
    print(f"{Fore.CYAN}+{'-'*44}+")
    
    # Exibindo os dados em forma de tabela
    print(f"| Nome: {user:<33}|")
    print(f"| Quantidade de Pessoas: {qtd_pessoas:<20}|")
    print(f"| Quantidade de Dias: {qtd_dias:<24}|")
    print(f"| Total a Pagar: {Fore.GREEN}R${total:.2f}{Style.RESET_ALL:<14}|")
    
    if parcelas and valor_parcela:
        print(f"| Parcelamento: {parcelas}x de {Fore.GREEN}R${valor_parcela:.2f}{Style.RESET_ALL:<12}|")
    else:
        print(f"| Parcelamento: À vista".ljust(44, ' ') + "|")

    print(f"{Fore.CYAN}+{'-'*44}+")
    print(f"{Style.RESET_ALL}")

# Função para a lógica do parcelamento
def parcelamento(total):
    try:
        parcelas = int(input("\nEscolha o número de parcelas (2 a 12 vezes): "))
        if 2 <= parcelas <= 12:
            valor_parcela = total / parcelas
            return parcelas, valor_parcela
        else:
            print("Número de parcelas inválido. O valor será cobrado à vista.")
            return None, None
    except ValueError:
        print("Opção inválida, o valor será cobrado à vista.")
        return None, None

# Função principal que controla a reserva
def realizar_reserva():
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

    user = input("Digite seu nome: ")
    print("Selecione qual tipo de apartamento deseja: ")
    print("1 - Apartamento 1 ao 6")
    print("2 - Apartamento 7 ao 12")
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
        return

    # Solicitar quantidade de pessoas e dias
    try:
        qtd_pessoas = int(input("\nInforme a quantidade de pessoas: "))
        qtd_dias = int(input("Informe a quantidade de dias que ficará hospedado: "))
        if qtd_pessoas > 0 and qtd_dias > 0:
            total = valor_selecionado * qtd_pessoas * qtd_dias
        else:
            print("Por favor, insira valores positivos para pessoas e dias.")
            return

        novo_cadastro = input("Deseja continuar ou fazer uma nova reserva (Digite sim ou não): ").strip().lower()

        if novo_cadastro == 'não':
            exibir_resultados(user, qtd_pessoas, qtd_dias, total)

            parcelar = input("\nDeseja parcelar o valor? (sim/não): ").strip().lower()
            if parcelar == "sim":
                parcelas, valor_parcela = parcelamento(total)
                if parcelas:
                    exibir_resultados(user, qtd_pessoas, qtd_dias, total, parcelas, valor_parcela)
            else:
                input("Aperte enter para finalizar a reserva.")

    except ValueError:
        print("Por favor, insira números válidos para pessoas e dias.")

if __name__ == "__main__":
    while True:
        realizar_reserva()
