#dictanary
Namesandadresses = {
    'firstName' : 'not found',
    'lastName' : "not found",
    'city' : 'not found',
    'zipCode' : 'not found',
    'phoneNumber' : 'not found'
}
def Assighnpairs(): #assighs Var to dictanary
    Namesandadresses['firstName'] = input("First Name:")
    Namesandadresses['lastName'] = input('Last Name:')
    Namesandadresses['city'] = input('City:')
    Namesandadresses['zipCode'] = input('Zip Code:')
    Namesandadresses['phoneNumber'] = input('Phone Number:')
Assighnpairs()
def print_dictanary():
    print(f"{Namesandadresses}")
print_dictanary()#prints