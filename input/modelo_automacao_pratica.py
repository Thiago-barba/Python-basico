#Modelo de automação utilizando a biblioteca webbrowser e randow
import webbrowser as wb
import random as rd

print('Welcome to the jungle')

print('-------------------')
print('Sites favoritos ')
print('-------------------')

def randomica():
    ran = rd.randint(1, 5)
    if ran == 1:
        wb.open('https://www.espn.com.br/')
    elif ran == 2:
        wb.open('https://www.instagram.com/')
    elif ran == 3:
        wb.open('https://www.youtube.com.br/')
    elif ran == 4:
        wb.open('https://www.marca.com/')
    elif ran == 5:
        wb.open('https://www.nba.com/')

def main():
    while True:
        print('ESPN[1], INSTAGRAM[2], YOUTUBE[3], MARCA[4], NBA[5], RANDOMIZAR[6], EXIT[7].' )
        x = int(input('>>>'))
        #condições:
        if x == 1:
            wb.open('https://www.espn.com.br/')
        elif x == 2:
            wb.open('https://https://www.instagram.com/')
        elif x == 3:
            wb.open('https://www.youtube.com.br/')
        elif x == 4:
            wb.open('https://www.marca.com/')
        elif x == 5:
            wb.open('https://www.nba.com/')
        elif x == 6:
            randomica()
        elif x == 7:
            input('Aperte enter para sair')
            break
        else:
            print('Opção não aceita, por favor digite uma opção valida. ')
        print()
main()

