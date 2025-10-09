def surch():
    #list
    months= ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'October', 'November', 'December',
             'january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'augest', 'september', 'october', 'november', 'december']
    surching = input('what month are you looking for?:')
    #lookup
    if surching in months:
        print(f'we found {surching} in the list, Search successful!')
    else:
        print(f'cannot find {surching} in the months list')
surch()