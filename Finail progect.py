#dissplay of product
print('                         PRODUCT CATALOG')
print('--------------------------------------------------------------')
print('1      |   USB Drive (128 GB)                |   $12.00')
print('2      |   Mac Book Pro (15 inch)            |   $2900.00')
print('3      |   Arduino 1010 (with blue tooth)    |   $48.00')
print('4      |   Ring Camera (wireless)            |   $156.00')
print('5      |   Smart TV (TCL 70 inch)            |   $359.00')
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
    Namesandadresses['email'] = input("E-Mail Adresses:")
    Namesandadresses['phoneNumber'] = input('Phone Number:')
Assighnpairs()
def print_dictanary():
    print(f"{Namesandadresses}")
print_dictanary()#prints
#loop for proper CCV
finding = True
while finding:
    creditcardnum = input("enter valid credit card number:")
    def validateCreditCard(ccNum):
        digits = [int(d) for d in str(ccNum) if d.isdigit()] #D is  all the numbers
        Sumofitall = 0
        dubbledit = False #looks untioll snd num

        for i in range(len(digits) -1, -1, -1): #cycles back one by one thrugh the individual number
            digit = digits[i]
            if dubbledit:
                digit *= 2
                if digit > 9:
                    digit -= 9
            Sumofitall += digit
            dubbledit = not dubbledit #alternates
        if Sumofitall % 10 == 0:
            return True
        else:
            return False
    if validateCreditCard(creditcardnum) == True:
        print('Number is valid')
        finding = False
    else:
        print('number is not valid, try a diffrent card!')