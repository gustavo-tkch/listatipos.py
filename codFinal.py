# usar pip install colorama
# usar pip install tabulate 

import os
from colorama import Fore, Style, init
from tabulate import tabulate  # importando a biblioteca para criar a tabela

init()

# Função para formatar CPF
def formatar_cpf(cpf):
    # Remove qualquer caractere não numérico
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Formata o CPF
    if len(cpf) == 11:
        cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
        return cpf_formatado
    else:
        return "CPF inválido"

while True:
    os.system("cls")
    print(f'''{Fore.BLUE}
     _   _  ____  ________ _______ ___          ___      ________ ________
    | | | |/ __ \\|___  ___|  ______|  |         |  |    |  ______|   _____|
    | |_| | |  | |  |  |  |  |_____|  |         |  |    |  |_____|  |____
    |  _  | |  | |  |  |  |  ______|  |         |  |    |   _____|  _____|
    | | | | |__| |  |  |  |  |_____|  |____     |  |____|  |_____|  |
    |_| |_|\\____/   |__|  |________|_______|    |_______|________|__|
    {Style.RESET_ALL}''')

    tipos_lista1 = [20.00, 28.00, 35.00, 42.00, 48.00, 53.00]  # dos tipos 1 ao 6
    tipos_lista2 = [28.00, 35.00, 42.00, 50.00, 57.00, 63.00]  # dos tipos 1 ao 2 da tabela 2

    # função para exibir os valores de uma lista
    def exibir_lista(lista):
        for i, valor in enumerate(lista, start=1):
            print(f"{Fore.GREEN}{i} - R${valor:.2f}{Style.RESET_ALL}")

    # a lista
    user = input("Digite seu nome: ")
    cpf = input("Digite o seu CPF (apenas números): ") 
    cpf_formatado = formatar_cpf(cpf)  # Formata o CPF

    print("Selecione qual tipo de apartamento deseja: ")
    print("Apartamento - Tipo 1")
    print("Apartamento - Tipo 2")
    escolha_lista = input("Digite o número da lista que deseja visualizar (1 ou 2): ")

    if escolha_lista == "1":
        print("\nVocê selecionou a Lista 1 (Escolha um dos apartamentos 1 a 6): ")
        print("""
        __________________________________
        |quant de pessoas     Valor      |
        |    1    |          R$20,00     |
        |    2    |          R$28,00     |
        |    3    |          R$35,00     |
        |    4    |          R$42,00     |
        |    5    |          R$48,00     |
        |    6    |          R$53,00     |
        |________________________________|
        """)
       
        escolha = int(input("\nEscolha um apartamento do tipo 1 a 6: ")) - 1
        if 0 <= escolha < len(tipos_lista1):
            valor_selecionado = tipos_lista1[escolha]

    elif escolha_lista == "2":
        print("\nVocê selecionou a Lista 2 (Escolha um dos apartamentos 1 a 6): ")
        print("""
        ___________________________________
        | quant de pessoas     Valor      |
        |     1    |          R$25,00     |
        |     2    |          R$34,00     |
        |     3    |          R$42,00     |
        |     4    |          R$50,00     |
        |     5    |          R$57,00     |
        |     6    |          R$63,00     |
        |_________________________________|
        """)
        escolha = int(input("\nEscolha um apartamento do tipo 1 a 6: ")) - 1
        if 0 <= escolha < len(tipos_lista2):
            valor_selecionado = tipos_lista2[escolha]
    else:
        print("Opção inválida! Por favor, escolha entre as listas 1 e 2.")
        exit()

    # solicitar quantidade de pessoas e dias
    try:
        qtd_pessoas = escolha
        qtd_dias = int(input("Informe a quantidade de dias que ficará hospedado: "))
        if qtd_pessoas > 0 and qtd_dias > 0:
            total = valor_selecionado * qtd_pessoas * qtd_dias
        else:
            print("Por favor, insira valores positivos para pessoas e dias.")
            continue

        # exibir resumo da reserva antes de perguntar sobre parcelamento
        os.system("cls")

        # criando a tabela com o resumo da reserva
        tabela = [
                   ["Nome", f"{Fore.CYAN}{user}{Style.RESET_ALL}"],
                   ["CPF", f"{Fore.CYAN}{cpf_formatado}{Style.RESET_ALL}"],  # Exibindo CPF formatado
                   ["Quantidade de Pessoas", f"{Fore.YELLOW}{qtd_pessoas}{Style.RESET_ALL}"],
                   ["Quantidade de Dias", f"{Fore.YELLOW}{qtd_dias}{Style.RESET_ALL}"],
                   ["Valor do Apartamento", f"{Fore.GREEN}R${valor_selecionado:.2f}{Style.RESET_ALL}"],
                   ["Total a Pagar", f"{Fore.GREEN}R${total:.2f}{Style.RESET_ALL}"]
        ]

        print("\nResumo da Reserva:")
        print(tabulate(tabela, headers=["Descrição", "Valor"], tablefmt="fancy_grid"))

        # perguntar se deseja parcelar
        parcelar = input("\nDeseja parcelar o valor? (sim/não): ").strip().lower()

        if parcelar == "sim":
            os.system("cls")  # limpa a tela
            print("Você optou por parcelar a reserva.")
            print(f"\nO valor total a ser parcelado é de {Fore.GREEN}R${total:.2f}{Style.RESET_ALL}")
            
            # solicitar número de parcelas
            parcelas = int(input("Escolha o número de parcelas (2 a 12 vezes): "))
            if 2 <= parcelas <= 12:
                valor_parcela = total / parcelas
                print(f"\nO valor será parcelado em {parcelas}x de {Fore.GREEN}R${valor_parcela:.2f}{Style.RESET_ALL}")
                
                # para atualizar a tabela com o parcelamento
                tabela_parcelada = [
                    ["Nome", f"{Fore.CYAN}{user}{Style.RESET_ALL}"],
                    ["CPF", f"{Fore.CYAN}{cpf_formatado}{Style.RESET_ALL}"],  # Exibindo CPF formatado
                    ["Quantidade de Pessoas", f"{Fore.YELLOW}{qtd_pessoas}{Style.RESET_ALL}"],
                    ["Quantidade de Dias", f"{Fore.YELLOW}{qtd_dias}{Style.RESET_ALL}"],
                    ["Valor do Apartamento", f"{Fore.GREEN}R${valor_selecionado:.2f}{Style.RESET_ALL}"],
                    ["Total a Pagar", f"{Fore.GREEN}R${total:.2f}{Style.RESET_ALL}"],
                    ["Parcelamento", f"{Fore.GREEN}{parcelas}x de R${valor_parcela:.2f}{Style.RESET_ALL}"]
                ]
                
                print("\nResumo da Reserva com Parcelamento:")
                print(tabulate(tabela_parcelada, headers=["Descrição", "Valor"], tablefmt="fancy_grid"))
            else:
                print("Número de parcelas inválido. O valor será cobrado à vista.")

        elif parcelar == "não":
            os.system("cls")  # Limpa a tela
        

            print("\nResumo da Reserva:")
            print(tabulate(tabela, headers=["Descrição", "Valor"], tablefmt="fancy_grid"))

            print(f"\n{Fore.CYAN}Reserva feita com sucesso, obrigado pela preferência!{Style.RESET_ALL}")

        else:
            print("Resposta está inválida! Por favor, digite apenas 'sim' ou 'não'.")
        
        resposta = input("\nDigite (sim) para fazer uma nova reserva: ").strip().lower()
        if resposta == "não":
            # aqui é para criar a tabela com o resumo da reserva
            tabela = [
                    ["Nome", f"{Fore.CYAN}{user}{Style.RESET_ALL}"],
                    ["CPF", f"{Fore.CYAN}{cpf_formatado}{Style.RESET_ALL}"],  # Exibindo CPF formatado
                    ["Quantidade de Pessoas", f"{Fore.YELLOW}{qtd_pessoas}{Style.RESET_ALL}"],
                    ["Quantidade de Dias", f"{Fore.YELLOW}{qtd_dias}{Style.RESET_ALL}"],
                    ["Valor do Apartamento", f"{Fore.GREEN}R${valor_selecionado:.2f}{Style.RESET_ALL}"],
                    ["Total a Pagar", f"{Fore.GREEN}R${total:.2f}{Style.RESET_ALL}"]
            ]
        if resposta == "sim":
            continue
        input("Aperte enter para finalizar!")
        break  # finaliza o loop após o processo
        
        

    except ValueError:
        print("Por favor, insira números válidos para pessoas e dias")
