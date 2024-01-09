# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
     # Windows
     if name == 'nt':
          _ = system('cls')
     
     # Mac ou Linux
     else:
          _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>> Hangman Game (Jogo da Forca) - Frutas <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman():

	# Método Construtor
     def __init__(self, palavras):
          self.palavras = palavras
          self.palavra_secreta = random.choice(palavras)
          self.board_atual = ['_' for _ in range(len(self.palavra_secreta))]
          self.tentativas_restantes = len(board) - 1

	# Método para adivinhar a letra
     def adivinhar(self, letra):
          encontradas = False
          for idx, char in enumerate(self.palavra_secreta):
               if char == letra:
                    self.board_atual[idx] = letra
                    encontradas = True
          if not encontradas:
               self.tentativas_restantes -= 1
	
	# Método para verificar se o jogo terminou
     def verifica_fim(self):
          return self.tentativas_restantes <= 0 or '_' not in self.board_atual
		
	# Método para verificar se o jogador venceu
     def verifica_vitoria(self):
          return '_' not in self.board_atual
		
	# Método para não mostrar a letra no board
     def letra_escondida(self, letra):
          return letra if letra in self.board_atual else '_'
		
	# Método para checar o status do game e imprimir o board na tela
     def imprime_board(self):
          print(board[len(board) - self.tentativas_restantes - 1])
          
          palavra_escondida = ' '.join([self.letra_escondida(letra) for letra in self.palavra_secreta])
          print(' '.join(palavra_escondida))
          
# Função para jogar o jogo
def play_game():
     while True:
          limpa_tela()
          lista_palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'maça', 'pera', 'manga', 'kiwi']
          jogo = Hangman(lista_palavras)
          
          while not jogo.verifica_fim():
               jogo.imprime_board()
               letra = input("Digite uma letra: ").lower()
               jogo.adivinhar(letra)
               
          if jogo.verifica_vitoria():
               print("Parabéns! Você ganhou!")
          else:
               print("Fim de jogo! A palavra era:", jogo.palavra_secreta)
          
          jogar_novamente = input("Gostaria de jogar novamente? (s/n): ").lower()
          if jogar_novamente != 's':
               break
          
play_game()