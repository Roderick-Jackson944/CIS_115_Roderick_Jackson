def printwordlist():
    #is list
    mylist = ['Apples', 'Bannannas', 'Pears', 'Carrots']
    #loop
    for item in mylist:
        print(item)
        for char in item:
            print(char)

loops = input('Input number: ')
here = int(loops)
for num in range(here):
    printwordlist()
