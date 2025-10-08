sliced1 = int(input('Insert what line you whant to slice from:'))
slice2 = int(input('Insurt what line to end slice:'))
#defined string slicer
def slicemystring():
    string = ['1','2','3','4','5']
    print(f"{string [sliced1 : slice2] }")
slicemystring()