#! python
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print (f'{penultimo}, {ultimo}', end =',')
    num = 0
    while num < limite:
        num = (penultimo + ultimo)
        print(num, end =',')
        penultimo = ultimo
        ultimo = num

if __name__ == '__main__':
    fibonacci(100000)
