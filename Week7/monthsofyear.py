
start = int(-1) + int(input('Input start month (enter number only):'))
end = int(input('input end month(enter number only):'))

def monthsofyear():
    #is list
    mylist = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'October', 'Nobember', 'Desember']
    print(f'{mylist[start: end]}')

monthsofyear()