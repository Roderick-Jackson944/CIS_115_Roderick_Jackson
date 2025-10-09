
start = int(input('Input start month (input 4):'))
end = int(input('input end month(input 6):'))

def slice_list():
    #is list
    mylist = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'October', 'November', 'Desember']
    print(f'{mylist[start: end]}')

slice_list()