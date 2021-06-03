racas = ['Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato',
         'Gnomo', 'Meio-Elfo', 'Meio-Orc', 'Tiefling']

for indice, raca in enumerate(racas):
    print(f'[{indice}]: {raca}')

print()

raca_escolhida = int(input('Informe a raca escolhida: '))

print()


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


if raca_escolhida == 0:
    anao()

elif raca_escolhida == 1:
    elfo()

elif raca_escolhida == 2:
    halfling()

elif raca_escolhida == 3:
    humano()

elif raca_escolhida == 4:
    draconato()

elif raca_escolhida == 5:
    gnomo()

elif raca_escolhida == 6:
    meio_elfo()

elif raca_escolhida == 7:
    meio_orc()

elif raca_escolhida == 8:
    tiefling()
