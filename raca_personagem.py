import ficha

racas = ['Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato',
         'Gnomo', 'Meio-Elfo', 'Meio-Orc', 'Tiefling']

for indice, raca in enumerate(racas):
    print(f'[{indice}]: {raca}')

print()

raca_escolhida = int(input('Informe a raca escolhida: '))

print()


def anao():
    ficha.atributos['forca'] += 2
    ficha.deslocamento += 7.5
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Resiliência anã')
    ficha.proficiencias_classe.append('Treinamento anão em combate')
    ficha.proficiencias_classe.append('Proficiência com ferramentas')
    ficha.proficiencias_classe.append('Especialização em rochas')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('anão')


def elfo():
    ficha.atributos['destreza'] += 2
    ficha.deslocamento += 9
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Sentidos aguçados')
    ficha.proficiencias_classe.append('Ancestral feérico')
    ficha.proficiencias_classe.append('Transe')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Élfico')


def halfling():
    ficha.atributos['destreza'] += 2
    ficha.deslocamento += 7.5
    ficha.proficiencias_classe.append('Sortudo')
    ficha.proficiencias_classe.append('Bravura')
    ficha.proficiencias_classe.append('Agilidade Halfling')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Halfling')


def humano():
    for index, atributo in enumerate(ficha.atributos):
        ficha.atributos[atributo] += 1
    ficha.deslocamento += 9
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('1 a sua escolha')


def draconato():
    ficha.atributos['forca'] += 2
    ficha.atributos['carisma'] += 1
    ficha.deslocamento += 9
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Draconato')


def gnomo():
    ficha.atributos['inteligencia'] += 2
    ficha.deslocamento += 7.5
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Esperteza gnômica')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Gnômico')


def meio_elfo():
    ficha.atributos['carisma'] += 2
    print('Outros dois valores de habilidade a sua escolha aumentam em 1')
    ficha.deslocamento += 9
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Ancestral Feérico')
    ficha.proficiencias_classe.append('Versatilidade em perícia')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Élfico')
    ficha.idiomas.append('Outro idioma a sua escolha')


def meio_orc():
    ficha.atributos['forca'] += 2
    ficha.atributos['constituicao'] += 1
    ficha.deslocamento += 9
    ficha.proficiencias_classe('Visão no escuro')
    ficha.proficiencias_classe('Ameaçador')
    ficha.proficiencias_classe('Resistência implacável')
    ficha.proficiencias_classe('Ataques selvagens')


def tiefling():
    ficha.atributos['inteligencia'] += 1
    ficha.atributos['carisma'] += 2
    ficha.deslocamento += 9
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Resistência Infernal')
    ficha.proficiencias_classe.append('Legado infernal')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Infernal')


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

print(f'Atributos: {ficha.atributos}')
print(f'Deslocamento: {ficha.deslocamento}m')
print(f'Proficiencias da classe: {ficha.proficiencias_classe}')
print(f'Idiomas: {ficha.idiomas}')
