
start = int(-1) + int(input('Input start month (enter number only 1-12):'))
end = int(input('input end month(enter number only 1-12):'))

def monthsofyear():
    #is list
    mylist = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'October', 'Nobember', 'Desember']
    print(f'{mylist[start: end]}')

monthsofyear()