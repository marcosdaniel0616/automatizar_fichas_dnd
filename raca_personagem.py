import ficha

racas = ['Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato',
         'Gnomo', 'Meio-Elfo', 'Meio-Orc', 'Tiefling']

raca = [(indice, raca) for indice, raca in enumerate(racas)]
print([raca for raca in raca])

print()

raca_escolhida = int(input('Informe a raca escolhida: '))

print()


def anao():
    ficha.atributos['constituicao'] += 2
    ficha.deslocamento += 7.5
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Resiliência anã')
    ficha.proficiencias_classe.append('Treinamento anão em combate')
    ficha.proficiencias_classe.append('Proficiência com ferramentas')
    ficha.proficiencias_classe.append('Especialização em rochas')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('anão')
    print('[0] Anão da colina')
    print('[1] Anão da montanha')
    sub_anao = int(input('Informe a sub-raça do seu anão: '))
    if sub_anao == 0:
        anao_colina()
    elif sub_anao == 1:
        anao_montanha()
    else:
        print('Informe o índice correto da subraça.')
        exit()


def anao_colina():
    ficha.atributos['sabedoria'] += 1
    ficha.proficiencias_classe.append('Tenacidade Anã')


def anao_montanha():
    ficha.atributos['forca'] += 2
    ficha.proficiencias_classe.append('Treinamento Anão com Armaduras.')


def elfo():
    ficha.atributos['destreza'] += 2
    ficha.deslocamento += 9
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Sentidos aguçados')
    ficha.proficiencias_classe.append('Ancestral feérico')
    ficha.proficiencias_classe.append('Transe')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Élfico')
    print('[0] Alto Elfo')
    print('[1] Elfo da floresta')
    print('[2] Elfo negro (Drow)')
    sub_elfo = int(input('Informe a sub-raça do seu elfo: '))
    if sub_elfo == 0:
        alto_elfo()
    elif sub_elfo == 1:
        elfo_floresta()
    elif sub_elfo == 2:
        elfo_negro()
    else:
        print('Informe o índice correto da sub-raça.')
        exit()


def alto_elfo():
    ficha.atributos['inteligencia'] += 1
    ficha.proficiencias_classe.append('Treinamento Élfico com armas.')
    ficha.proficiencias_classe.append('Truque')
    ficha.proficiencias_classe.append('Idioma adicional')


def elfo_floresta():
    ficha.atributos['sabedoria'] += 1
    ficha.proficiencias_classe.append('Treinamento Élfico com armas.')
    ficha.deslocamento += 1.5
    ficha.proficiencias_classe.append('Pés-Ligeiros.')
    ficha.proficiencias_classe.append('Máscara da natureza.')


def elfo_negro():
    ficha.atributos['carisma'] += 1
    ficha.proficiencias_classe.append('Visão no escuro superior.')
    ficha.proficiencias_classe.append('Sensibilidade à luz solar')
    ficha.proficiencias_classe.append('Magia Drow')
    ficha.proficiencias_classe.append('Treinamento Drow com armas.')


def halfling():
    ficha.atributos['destreza'] += 2
    ficha.deslocamento += 7.5
    ficha.proficiencias_classe.append('Sortudo')
    ficha.proficiencias_classe.append('Bravura')
    ficha.proficiencias_classe.append('Agilidade Halfling')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Halfling')
    print('[0] halfling pés-leve')
    print('[1] halfling robusto')
    sub_halfling = int(input('Informe a sub-raça do seu halfling: '))
    if sub_halfling == 0:
        halfling_pes_leve()
    elif sub_halfling == 1:
        halfling_robusto()
    else:
        print('Informe o índice correto da sub-raça.')
        exit()


def halfling_pes_leve():
    ficha.atributos['carisma'] += 1
    ficha.proficiencias_classe.append('Furtividade natural')


def halfling_robusto():
    ficha.atributos['constituicao'] += 1
    ficha.proficiencias_classe.append('Resiliência dos robustos')


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
    print('[0] Azul - Elétrico')
    print('[1] Branco - Frio')
    print('[2] Bronze - Elétrico')
    print('[3] Cobre - Ácido')
    print('[4] Latão - Fogo')
    print('[5] Negro - Ácido')
    print('[6] Ouro - Fogo')
    print('[7] Prata - Frio')
    print('[8] Verde - Veneno')
    print('[9] Vermelho - Fogo')
    sub_draconato = int(input('Informe a sub-raça do seu draconato: '))
    if sub_draconato == 0 or sub_draconato == 2:
        ficha.proficiencias_classe.append('Arma de sopro elétrica.')
        ficha.proficiencias_classe.append('Resistência a dano elétrica.')
    elif sub_draconato == 1 or sub_draconato == 7:
        ficha.proficiencias_classe.append('Arma de sopro frio.')
        ficha.proficiencias_classe.append('Resistência a dano frio.')
    elif sub_draconato == 3 or sub_draconato == 5:
        ficha.proficiencias_classe.append('Arma de sopro ácida.')
        ficha.proficiencias_classe.append('Resistência a dano ácido.')
    elif sub_draconato == 4 or sub_draconato == 6 or sub_draconato == 9:
        ficha.proficiencias_classe.append('Arma de sopro de fogo.')
        ficha.proficiencias_classe.append('Resistência a dano de fogo.')
    elif sub_draconato == 8:
        ficha.proficiencias_classe.append('Arma de sopro de veneno.')
        ficha.proficiencias_classe.append('Resistência a dano de veneno.')
    else:
        print('Informe o índice correto da sub-raça.')
        exit()


def gnomo():
    ficha.atributos['inteligencia'] += 2
    ficha.deslocamento += 7.5
    ficha.proficiencias_classe.append('Visão no escuro')
    ficha.proficiencias_classe.append('Esperteza gnômica')
    ficha.idiomas.append('Comum')
    ficha.idiomas.append('Gnômico')


def gnomo_floresta():
    ficha.atributos['destreza'] += 1
    ficha.proficiencias_classe.append('Ilusionista nato.')
    ficha.proficiencias_classe.append('Falar com bestas pequenas.')


def gnomo_rochas():
    ficha.atributos['constituicao'] += 1
    ficha.proficiencias_classe.append('Conhecimento de artifíce.')
    ficha.proficiencias_classe.append('Engenhoqueiro.')


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

else:
    print('O valor informado foi incorreto, informe a raça pelo seu índice!')
    exit()

print()
print(f'Atributos: {ficha.atributos}')
print(f'Deslocamento: {ficha.deslocamento}m')
print(f'Proficiencias da classe: {ficha.proficiencias_classe}')
print(f'Idiomas: {ficha.idiomas}')
