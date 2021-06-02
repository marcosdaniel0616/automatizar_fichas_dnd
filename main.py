from raca_personagem import RacaPersonagem
"""
escolha_raca = EscolhaRaca()
print(escolha_raca.raca_escolhida)
"""

minha_raca = RacaPersonagem()

raca_personagem = int(input('Informa a raça do seu personagem: '))

"""
print('''[0] Bárbaro
[1] Bardo
[2] Bruxo
[3] Clérigo
[4] Druida
[5] Feiticeiro
[6] Guerreiro
[7] Ladino
[8] Mago
[9] Monge
[10] Pladino
[11] Patrulheiro
''')
classe_personagem = int(input('Informe a classe do personagem: '))
"""


def anao():
    print('Constituição: + 2')
    print('Deslocamento: 7.5m')
    print('Visão no escuro')
    print('Resiliência anã')
    print('Treinamento anão em combate')
    print('Proficiência com ferramentas')
    print('Especialização em rochas')
    print('Idiomas: Comum e anão')


def elfo():
    print('Destreza: + 2')
    print('Deslocamento: 9m')
    print('Visão no escuro')
    print('Sentidos aguçados')
    print('Ancestral feérico')
    print('Transe')
    print('Idiomas: Comum e élfico')


def halfling():
    print('Destreza +2')
    print('Deslocamento: 7.5m')
    print('Sortudo')
    print('Bravura')
    print('Agilidade Halfling')
    print('Idiomas: Comum e Halfling')


def humano():
    print('Todas as habilidades +1')
    print('Deslocamento: 9m')
    print('Idiomas: 1 comum e 1 a sua escolha')


def draconato():
    print('+2 de força, +1 em carisma')
    print('Deslocamento: 9m')
    print('Idiomas: Comum e draconato')


def gnomo():
    print('+2 inteligência')
    print('Deslocamento: 7.5m')
    print('Visão no escuro')
    print('Esperteza gnômica')
    print('Idiomas: Comum e gnômico')


def meio_elfo():
    print('Carisma +2, outros dois a sua escolha +1')
    print('Deslocamento: 9m')
    print('Visão no escuro')
    print('Ancestral Feérico')
    print('Versatilidade em perícia')
    print('Idiomas: Comum e élfico e mais um idioma a sua escolha')


def meio_orc():
    print('Força + 2, + 1 constituição')
    print('Deslocamento: 9m')
    print('Visão no escuro')
    print('Ameaçador')
    print('Resistência implacável')
    print('Ataques selvagens')


def tiefling():
    print('Idiomas: Comum e infernal')
    print('+1 inteligência, +2 carisma')
    print('9 deslocamento')
    print('Visão no escuro')
    print('Resistência infernal')
    print('Legado infernal')


if minha_raca.raca_personagem == 0:
    anao()

elif minha_raca.raca_personagem == 1:
    elfo()

elif minha_raca.raca_personagem == 2:
    halfling()

elif minha_raca.raca_personagem == 3:
    humano()

elif minha_raca.raca_personagem == 4:
    draconato()

elif minha_raca.raca_personagem == 5:
    gnomo()

elif minha_raca.raca_personagem == 6:
    meio_elfo()

elif minha_raca.raca_personagem == 7:
    meio_orc()

elif minha_raca.    raca_personagem == 8:
    tiefling()
