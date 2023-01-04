import os
portifolio = [['Chevrolet Tracker', 120], ['Chevrolet Onix', 90], ['Chevrolet Spin', 150], ['Hyundai HB20', 85], ['Hyundai Tucson', 120], ['Fiat Uno', 60], ['Fiat Mobi', 70], ['Fiat Pulse', 130]]
carros_alugados = []
while True:    
    os.system('cls')    
    titulo = ('Bem vindo à locadora de carros!')
    print('='*70)
    print(titulo.center(70))
    print('='*70)
    print('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro')
    escolha = int(input('Qual opção você deseja? '))
    print()
    
    if escolha == 0:
        for i, k in enumerate(portifolio):
            print(f'[{i}] - {k[0]} - R$ {k[1]} /dia')
        print()
        print('Você deseja continuar? ')
        continua = int(input('[0] - SAIR   | [1] - VOLTAR PARA O MENU  '))
        if continua == 0:
            break
    
    if escolha == 1:
        for i, k in enumerate(portifolio):
            print(f'[{i}] - {k[0]} - R$ {k[1]}/dia')
        print()
        codigo = int(input('Escolha o código do carro: '))
        dias = int(input('Por quantos dias deseja alugar: '))
        preco = portifolio[codigo][1] * dias
        print()
        print(f'Você escolheu o carro {portifolio[codigo][0]} e vai custar: {preco} reais.')
        print()
        confirma = input('Deseja alugar esse carro? ').lower()[0]
        if confirma in 's':
            carros_alugados.append(portifolio[codigo])
            portifolio.remove(portifolio[codigo])
        else:
            continue
        
    if escolha == 2:
        if len(carros_alugados) == 0:
            print('Não há carros na lista de alugados.')
            print()
            print('O que você deseja fazer? ')
            continua = int(input('[0] - SAIR   | [1] - VOLTAR PARA O MENU  '))
            if continua == 0:
                break
        else:    
            for i, k in enumerate(carros_alugados):
                print(f'[{i}] - {k[0]} - R$ {k[1]} /dia')
            print()
            confirma = input('Você deseja devolver algum carro? ').lower()[0]
            if confirma in 's':
                print('Qual código do carro que você deseja devolver? ')
                print()
                codigo_devolver = int(input())
                print()
                print(f'Você escolheu devolver o carro {carros_alugados[codigo_devolver][0]}')
                print()
                confirma = input('Deseja devolver esse carro? ').lower()[0]
                if confirma in 's':
                    portifolio.append(carros_alugados[codigo_devolver])
                    carros_alugados.remove(carros_alugados[codigo_devolver])
                else:
                    continue
            else:
                pass
        