from Tabuleiro import Tabuleiro
from Jogador import Jogador


class Estado:
    def __init__(self, tabuleiro: Tabuleiro, jogadores: list[Jogador]):
        self.tabuleiro = tabuleiro 
        self.jogadores = jogadores

    def __str__(self):
        return f"Tabuleiro:  {self.tabuleiro} Jogadores:  {self.jogadores}"

    # reorganizar lista de jogadores pela carta de personagem
    def ordenar_jogadores(self):
