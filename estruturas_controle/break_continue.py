#! python 
for x in range (1, 11):
    if x % 2 == 0:
        continue
    print(x)

print('Fim')

for x in range (1, 11):
    if x == 5:
        break
    print(x)
