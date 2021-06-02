class RacaPersonagem:
    raca_personagem: int
    minha_raca: str
    print('''[0] Anão
    [1] Elfo
    [2] Halfling
    [3] Humano
    [4] Draconato
    [5] Gnomo
    [6] Meio-Elfo
    [7] Meio-Orc
    [8] Tiefling
    ''')
    def escolher_raca(self, raca_personagem):
        self.minha_raca = raca_personagem

