from random import randint
from time import sleep

# function for the = line 
def lin():
    print('==' * 30)

# Do the program play until the user say no
while True:
    # Create the main list
    items = []
    
    lin()
    # Ask how many lis the user want to add
    list_amount = int(input('How many list do you want to add? '))
    # Create the lists 
    for amount_lists in range(0, list_amount):
        items.append([])
    
    # Repeat until the user have the randomized lists
    while True:

        # Repeat list amount times 
        for moment_list in range(0, list_amount):
            item = 0
            # Repeat until the lists are complete
            while True:
                # Add the items
                items[moment_list].append(str(input(f'What do you want to place in the {item}° index of the {moment_list + 1}º list: ')))
                stop = ' '
                item += 1

                # Ask if the user want to continue
                while stop not in 'YN':
                    stop = input('Do you want to continue? [Y/N] ').upper().strip()[0] 
                lin()
                if stop == 'N':
                    break

        # Randomize and show the lists         
        for items_list in range(0, len(items)):
            print(f'{items_list + 1}º List:', end=' ')

            # Randomize a int that is a valid index of the list the program is showing at the moment
            # Than show the item of the randomized index and remove it from the list to not repeat the same item
            # So, next time the list will be one index smaller don't giving error for index out of range 
            for index in range(0, len(items[items_list])):
                random = randint(0, len(items[items_list]) - 1)
                print(f'→ {items[items_list][random]}', end=' ')
                del(items[items_list][random])
            print()
            lin()
        break

    # Ask if the user want to finish the program
    finish = ' '
    while finish not in 'YN': 
        finish = input('End the program? [Y/N] ').upper().strip()[0]
    if finish =='Y':
        break
    else:
        # In case the user want to continue using the program it will delete the list to create more
        for c in range(0, len(items) - 1):
            del(items[c])

# Thanks the user for using this program 
thanks ='Thanks you very much for use this program. I hope you are satisfied!' 

for letter in thanks:
    print(letter, end='', flush=True)
    sleep(0.05)
print()