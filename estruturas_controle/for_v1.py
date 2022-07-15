#! python 
cont = 1
number = int(input('Digite um numero para saber a sua tabuada: '))
for i in range(1, 11):
    print (f'{number} x {cont} = {number * cont}')
    cont += 1
