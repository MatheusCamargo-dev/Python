#! python

generator = (i ** 2 for i in range (10) if i % 2 == 0)


for num in generator:
    print(num)