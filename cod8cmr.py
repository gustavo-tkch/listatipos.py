
#
#
# implementar o pip install colorama
#
#

from colorama import Fore, Style, init
from datetime import datetime, timedelta

init()

print(f'''{Fore.BLUE}
  _   _  ____  ________ ________ __
 | | | |/ __ \\|___  ___|  ______|  |
 | |_| | |  | |  |  |  |  |_____|  |
 |  _  | |  | |  |  |  |  ______|  |
 | | | | |__| |  |  |  |  |_____|  |____
 |_| |_|\\____/   |__|  |________|_______|
{Style.RESET_ALL}''')

tipos_lista1 = [20.00, 28.00, 35.00, 42.00, 48.00, 53.00]  # Tipos 1 ao 6
tipos_lista2 = [28.00, 35.00, 42.00, 50.00, 57.00, 63.00]  # Tipos 7 ao 12

# função para exibir os valores de uma lista
def exibir_lista(lista):
    for i, valor in enumerate(lista, start=1):
        print(f"{Fore.GREEN}{i} - R${valor:.2f}{Style.RESET_ALL}")

reservas = []  # lista para armazenar as reservas com nome, valor, data de início e data de término
nome_usuario = input("Por favor, informe seu nome: ").strip()

while True:  # loop para repetir caso o usuário deseje fazer nova reserva
    if reservas and nome_usuario:  # verifica se já houve uma reserva anterior
        print(f"\nBem-vindo de volta, {nome_usuario}!")

    print(f"\n{nome_usuario}, vamos iniciar sua reserva.")
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
        else:
            print("Opção inválida. Escolha um número dentro do intervalo válido.")
            continue
    elif escolha_lista == "2":
        print("\nVocê selecionou a Lista 2 (Escolha um dos apartamentos 1 a 6): ")
        exibir_lista(tipos_lista2)
        escolha = int(input("\nEscolha um apartamento do tipo 1 a 6: ")) - 1
        if 0 <= escolha < len(tipos_lista2):
            valor_selecionado = tipos_lista2[escolha]
        else:
            print("Opção inválida. Escolha um número dentro do intervalo válido.")
            continue
    else:
        print("Opção inválida! Por favor, escolha entre as listas 1 e 2.")
        continue

    try:
        data_reserva = input("\nInforme a data da reserva (dd/mm/aaaa): ").strip()
        data_inicio = datetime.strptime(data_reserva, "%d/%m/%Y")  # converte a data para o formato correto
        qtd_pessoas = int(input("\nInforme a quantidade de pessoas: "))
        qtd_dias = int(input("Informe a quantidade de dias que ficará hospedado: "))
        if qtd_pessoas > 0 and qtd_dias > 0:
            data_termino = data_inicio + timedelta(days=qtd_dias)  # calcula a data de término
            total = valor_selecionado * qtd_pessoas * qtd_dias
            reservas.append((nome_usuario, total, data_inicio, data_termino))  # adiciona nome, total e datas à lista
            print(f"\nO total desta reserva é: {Fore.GREEN}R${total:.2f}{Style.RESET_ALL}")
            print(f"A hospedagem começa em: {Fore.RED}{data_inicio.strftime('%d/%m/%Y')}{Style.RESET_ALL} "
                  f"e termina em: {Fore.RED}{data_termino.strftime('%d/%m/%Y')}{Style.RESET_ALL}")
        else:
            print("Por favor, insira valores positivos para pessoas e dias.")
            continue
    except ValueError:
        print("Por favor, insira dados válidos para a data, pessoas e dias.")
        continue
    
    resposta = input("\nDeseja fazer uma nova reserva? (sim/não): ").strip().lower()
    if resposta == "não":
        print("\nResumo das Reservas:")
        for i, (usuario, valor, inicio, termino) in enumerate(reservas, start=1):
            print(f"Reserva {i} - Usuário: {Fore.CYAN}{usuario}{Style.RESET_ALL}, "
                  f"Valor: {Fore.GREEN}R${valor:.2f}{Style.RESET_ALL}, "
                  f"Período: {Fore.RED}{inicio.strftime('%d/%m/%Y')}{Style.RESET_ALL} a {Fore.RED}{termino.strftime('%d/%m/%Y')}{Style.RESET_ALL}")
        total_geral = sum(valor for _, valor, _, _ in reservas)
        print(f"\nO total geral a pagar é: {Fore.GREEN}R${total_geral:.2f}{Style.RESET_ALL}")
        
        # opção de parcelamento
        parcelar = input("\nDeseja parcelar o valor? (sim/não): ").strip().lower()
        if parcelar == "sim":
            print("\nVocê pode parcelar em até 6 vezes.")
            parcelas = int(input("Escolha o número de parcelas (2 a 6 vezes): "))
            if 1 <= parcelas <= 6:
                valor_parcela = total_geral / parcelas
                print(f"\nO valor será parcelado em {parcelas}x de {Fore.GREEN}R${valor_parcela:.2f}{Style.RESET_ALL}")
            else:
                print("Número de parcelas inválido. O valor será cobrado à vista.")
        
        print("\nReservas foram feitas com sucesso!")
        break
    elif resposta == "sim":
        mesma_pessoa = input("É a mesma pessoa? (sim/não): ").strip().lower()
        if mesma_pessoa == "não":
            nome_usuario = input("Por favor, informe o nome do novo usuário: ").strip()
        else:
            outra_data = input("Esta reserva será para outra data específica? (sim/não): ").strip().lower()
            if outra_data == "sim":
                print("Ok! Vamos prosseguir com a nova reserva para a data específica.")
    else:
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
        