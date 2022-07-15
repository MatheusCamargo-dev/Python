#! python
produto = {'nome': 'Caneta Chic ', 'preço' : 14.99,
           'importada': True, 'estoque': 793}
           
for chave, valor in produto.items():
    print (f'{chave} = {valor}')
    