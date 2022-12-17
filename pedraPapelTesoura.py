from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
PC = randint(0, 2)

def linha():
    print('-=' * 12)

print('''Suas opções
[0] Pedra
[1] Papel
[2} Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!!')
linha()
print(f'Computador jogou {itens[PC]}')
print(f'O Jogador jogou {itens[jogador]}')
linha()

if PC == 0:
  if jogador == 0:
    print('EMPATE')
  elif jogador == 1:
    print('JOGADOR GANHOU!!')
  elif jogador == 2:
    print('MAQUINA VICTOR EST')
  else:
    print('Jogada inválida')

elif PC == 1:
  if jogador == 0:
    print('PC ganhou')
  elif jogador == 1:
    print('Empate')
  elif jogador == 2:
    print('Jogador Vence!!!!!!')
  else:
    print('Jogada inválida')

elif PC == 2:
  if jogador == 0:
    print('JOGADOR GANHOU!!')
  elif jogador == 1:
    print('MAQUINA VICTOR EST')
  elif jogador == 2:
    print('EMPATE')
else:
  print('Jogada inválida')
linha()
