import os


while True:
    os.system("cls")
    print('MENU CALCULADORA')
    print('0 : Somar \n1 : Subtração \n2 : Multiplicação \n3 : Divisão \n4 : Exponenciação ')
    operacao = int(input('Qual operação você deseja fazer? '))
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if operacao == 0:
        print(f'{n1} + {n2} = {n1+n2}')
    elif operacao == 1:
        print(f'{n1} - {n2} = {n1-n2}')
    elif operacao == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif operacao == 3:
        print(f'{n1} / {n2} = {n1/n2}')
    elif operacao == 4:
        print(f'{n1} ^ {n2} = {n1**n2}')
    else:
        print('Opção inválida. Escolha um dos números acima.')
    dnv = input('Você deseja fazer outra operação? ').lower()[0]
    if dnv in 'n':
        break
    
    