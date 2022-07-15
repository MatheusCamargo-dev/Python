#! python

dicionary = {f'item {i}': i * 2 for i in range(10) if i % 2 == 0}
print (dicionary)
for numero, dobro in dicionary.items():
    print(f'{numero} x 2 = {dobro}')