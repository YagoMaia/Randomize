from random import randint
from time import sleep

def lin():
    print('==' * 30)

while True:
    itens = []
    
    question = int(input('How many list do you want to add? '))
    
    for b in range(0, question):
        itens.append([])
    while True:
        for v in range(0, question):
            while True:
                itens[v].append(str(input(f'What do you want to place in the {v + 1}º list ')))
                stop = input('Do you wish to continue? [Y/N] ').upper().strip()[0]
                while stop not in 'YN':
                    stop = input('Do you wish to continue? [Y/N] ').upper().strip()[0]
                lin()
                if stop == 'N':
                    break
    
        for l in range(0, len(itens)):
            print(f'{l + 1}º List:')
            for i in range(0,len(itens[l])):
                random = randint(0, len(itens[l]) - 1)
                print(itens[l][random], end='; ')
                del(itens[l][random])
            print('\n')
            lin()
        break
    finish = input('End the program? [Y/N] ').upper().strip()[0]
    while finish not in 'YN': 
        finish = input('End the program? [Y/N] ').upper().strip()[0]
    if finish =='Y':
        break
    else:
        for c in range(0, len(itens) - 1):
            del(itens[c])

thanks ='Thanks you very much for use this program, I hope you are satisfied' 

for l in thanks:
    print(l, end='', flush=True)
    sleep(0.1)
