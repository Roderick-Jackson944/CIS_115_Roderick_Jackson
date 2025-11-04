#dissplay of product
print('                         PRODUCT CATALOG')
print('--------------------------------------------------------------')
print('1      |   USB Drive(128 GB)                 |   $12.00')
print('2      |   Mac Book Pro(15 inch)             |   $2900.00')
print('3      |   Arduino 1010(with blue tooth)     |   $48.00')
print('4      |   Ring Camera(wireless)             |   $156.00')
print('5      |   Smart TV(TCL 70 inch)             |   $359.00')
print('--------------------------------------------------------------')

#shipping info lines 12-29
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