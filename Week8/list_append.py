list =[]#list
list.append(input('input initial value:'))
done = True
while done:#loop
    list.append(input('Insert any value here to input into list:'))
    yes = input('Would you like to enter another value to append to the list?(y or n):')
    if yes == 'n':
        print(f'{list}')
        done = False#ends loop
    elif yes == 'y':
        list.append(input('Insert any value here to input into list again:'))
        yes = input('Would you like to enter another value to append to the list?(y or n):')
    else:
        print(f'error, here is recorded list {list}')
