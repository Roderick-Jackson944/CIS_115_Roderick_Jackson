#loop_over_list.py
#defines list
def getmylist():
    #is list
    mylist = [10, 20, 30, 40, 50, 60]
    #loop
    for item in mylist:
        print(item)
    listlen = len(mylist)
    #Prints
    print (f'how many var in list is {listlen}')
getmylist()
#