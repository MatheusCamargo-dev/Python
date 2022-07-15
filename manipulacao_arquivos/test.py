#! python
import os
from time import sleep
print("""======================================
      SIMULATOR OF BATTLE
  O                         O
 /|\<=|====>   X   <====|=>/|\ 
 / \                       / \ 
   PLAYER 01               CPU
======================================
Olá você está num simulador de batalha""")
Player = str(input('Digite aqui o nome de seu personagem:'))
os.system("clear")


def Interface():
    print("""======================================
           SIMULATOR OF BATTLE
        O                         O
       /|\<=|====>   X   <====|=>/|\ 
       / \                       / \ 
        {}        CPU
======================================""".format(Player))


def Status():
    print(f"""======================================
      STATUS DO PERSONAGEM {Player}
Pontos de ATK:{AtkP}
Pontos de DEF:{DefP}
Pontos de Vida:{VidP}
======================================""")


def StatusCPU():
    print(f"""======================================
      STATUS DA CPU
Pontos de ATK:{AtkC}
Pontos de DEF:{DefC}
Pontos de Vida:{VidC}
======================================""")
def Traço():
    print('=' * 38)


Interface()
R = str(input("Você quer qual dificuldade facil, medio ou dificil:")).upper()
os.system("clear")
if R == 'FACIL':
    print("     Você escolheu FACIL !")
    AtkC = 2000
    DefC = 2500
    VidC = 3500
    AtkP = 3500
    DefP = 2800
    VidP = 6000
    Status()
elif R == 'MEDIO':
    print("     Você escolheu MEDIO")
    AtkC = 3000
    DefC = 3200
    VidC = 4500
    AtkP = 5000
    DefP = 5500
    VidP = 5200
    Status()
elif R == 'DIFICIL':
    print("     Você escolheu DIFICIL")
    AtkC = 5000
    DefC = 6800
    VidC = 9000
    AtkP = 8200
    DefP = 6500
    VidP = 4500
    Status()
R2 = 'N'
while R2 == 'N':
    if  R2 == 'N':
        Traço()
        print(f"""    MODO DE BATALHA: OFF
         O                         O
        /|\<=|====>   X   <====|=>/|\ 
        / \                       / \ 
        {Player}             CPU""")
        Traço()
        R2 = str(input("Você deseja iniciar o modo de batalha?S/N:")).upper()
        os.system('clear')
for c in range (3, -1, -1):
    Interface()
    Status()
    StatusCPU()
    Traço()
    print("INICIANDO O MODO DE BATALHA")
    Traço()
    print(f"Em {c}")
    sleep(1.5)
    if c == 0:
        print("GO GO GO GO!!!!!")
        Traço()
sleep(1.5)
os.system('clear')
Traço()
print(f"""    MODO DE BATALHA:ON
         O                         O
        /|\<=|====>   X   <====|=>/|\ 
        / \                       / \ 
        {Player}             CPU""")
Traço()
