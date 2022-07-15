#! python
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica')
textos = ['João gosta de futebol e politica',
          'A praia foi divertida',
]   

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Foi encontrado uma palavra proibida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado:', texto)
