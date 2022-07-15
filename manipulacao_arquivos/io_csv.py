#! python
import csv

with open ('desafio-ibge.csv') as entrada: 
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))