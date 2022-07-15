#! python
PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'politica'}
textos = ['João gosta de futebol e politica',
          'A praia foi divertida',
]   
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print(' O texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado: ', texto)