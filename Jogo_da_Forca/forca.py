# -*- coding: utf-8 -*-

# Hangman Game (Jogo da forca)

# Programação orientada a objeto

import random

# Bord (tabuleiro

bord = [ '''

>>>>>>>> Hangman <<<<<<<<
+___+
|   |
    |
    |
    |
    |
======= ''','''

+___+
|   |
0   |
    |
    |
    |
======= ''','''


+___+
|   |
0   |
|   |
    |
    |
======= ''','''



+___+
|   |
0   |
|\  |
    |
    |
======= ''','''


 +___+
 |   |
 0   |
/|\  |
     |
     |
======= ''','''



 +___+
 |   |
 0   |
/|\  |
  \  |
     |
======= ''','''

 +___+
 |   |
 0   |
/|\  |
/ \  |
     |
======= 

''']

class Hangman:
    # Metodo Construtor
    def __init__(self,word):
        self.word = word

    # Metodo para ativar a letra
    def guest(self,letter):
        if letter in bank
    # Metodo para verificar se o jogo terminou
    def hangman_over(self):
    # Metodo para verificar se o jogador venceu

    def hangman_won(self):
    # Metodo para não mostra a letra no board

        print(self.letter)
    def hide_word(self):
    # Metodo para checar o status do game e imprimir a bord na tela
    def print_game_status(self):

# função para ler uma palvra de forma aleatoria
def ran_word():
    with open('palavras.txt','rt') as f:
        bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()

# Função main - Execucao do Programa
def main():
    #Objeto
    game = Hangman(ran_word())

    #Enquando o jogo não tiver terminado. print do status .solcita uma letra e faz a leitura do caracter
    # verificar o status

    game.print_game_status()

    # De acordo com o status,imprime mensagem na tela para o usuarios

    if game.hangman_won():
        print('\nParabéns! Você venceu')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era' + game.word)
    print('\nFoi bom jogar com você! Agora vá estudar!\n')

if __name__=='__main__':
    main()