import os
from random import randint
from time import sleep
voce = 0
computador = 0
empate = 0

while True:
    os.system('cls')
    print('PLACAR')
    print(f'VOCÊ: {voce}')
    print(f'COMPUTADOR: {computador}')
    print(f'EMPATES: {empate}')
    
    pc = randint(0,2)
    if pc == 0:
        pc = 'pedra'
    elif pc == 1:
        pc = 'papel'
    elif pc == 2:
        pc = 'tesoura'
    print('='*30)
    print('JOGO PEDRA, PAPEL e TESOURA!')
    print('='*30)
    escolha = input('Escolha entre PEDRA, PAPEL ou TESOURA: ').lower()
    print('\nFazendo a minha escolha...')
    sleep(2)
    if escolha in 'pedrapapeltesoura':
        pass
    else:
        print('Escolha inválida. Tente novamente.')
    if escolha == pc:
        print(f'Empatamos! Nós dois escolhermos {escolha}')
        empate += 1
    elif escolha == 'papel' and pc == 'pedra':
        print(f'Você venceu! Você escolheu {escolha} e eu escolhi {pc}.')
        voce += 1
    elif escolha == 'pedra' and pc == 'tesoura':
        print(f'Você venceu! Você escolheu {escolha} e eu escolhi {pc}.')
        voce += 1
    elif escolha == 'tesoura' and pc == 'papel':
        print(f'Você venceu! Você escolheu {escolha} e eu escolhi {pc}.')
        voce += 1
    elif escolha == 'papel' and pc == 'tesoura':
        print(f'Você perdeu! Você escolheu {escolha} e eu escolhi {pc}.')
        computador += 1
    elif escolha == 'pedra' and pc == 'papel':
        print(f'Você perdeu! Você escolheu {escolha} e eu escolhi {pc}.')
        computador += 1
    elif escolha == 'tesoura' and pc == 'pedra':
        print(f'Você perdeu! Você escolheu {escolha} e eu escolhi {pc}.')
        computador += 1
    continua = input('Você quer continuar? ').lower()[0]
    if continua == 'n':
        break
    else:
        continue