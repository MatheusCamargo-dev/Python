#! python

dobros_pares = [i * 2 for i in range (10) if i % 2 == 0]
print (dobros_pares)

dobro_par = []
for i in range (10):
    if i % 2 == 0:
        dobro_par.append(i * 2)
print (dobro_par)