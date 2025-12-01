#dissplay of product
print('                         PRODUCT CATALOG')
print('--------------------------------------------------------------')
print('1      |   USB Drive (128 GB)                |   $12.00')
print('2      |   Mac Book Pro (15 inch)            |   $2900.00')
print('3      |   Arduino 1010 (with blue tooth)    |   $48.00')
print('4      |   Ring Camera (wireless)            |   $156.00')
print('5      |   Smart TV (TCL 70 inch)            |   $359.00')
print('--------------------------------------------------------------')

catalog = {'usb_k981' : '1',
           'mbpro_490' : '2',
           'chip_1010' : '3',
           'cam_78' : '4',
           'smt_tv_100' : '5'}
usb_k981 = 12.00
mbpro_490 = 2900.00
chip_1010 = 48.00
cam_78 = 156.00
smt_tv_100 = 359.00
#list of shopping cart
Usb = []
macbookpro = []
arduino = []
ringcam = []
smorttv = []

list =[]#list
list.append(input('input Item whanted:'))
done = True
while done:#loop
    produtct_select = input('input the item number: ')
    if produtct_select == 1:
        print('Item; Usb Drive (128gb), selected: ')
        numberwhanted = int(input('Amount needed: '))
        Usb.append( 12 * numberwhanted )
    elif produtct_select == 2:
        print('Item; Mac book Pro (15 in), selected: ')
        numberwhanted = int(input('Amount needed: '))
        macbookpro.append( 2900 * numberwhanted )
    elif produtct_select == 3:
        print('Item; Arduino 1010 (with blue tooth), selected: ')
        numberwhanted = int(input('Amount needed: '))
        arduino.append( 48 * numberwhanted )
    elif produtct_select == 4:
        print('Item; Ring Camera (wireless), selected: ')
        numberwhanted = int(input('Amount needed: '))
        ringcam.append( 156 * numberwhanted )
    elif produtct_select == 5:
        print('Item; Smart TV (TCL 70 inch), selected: ')
        numberwhanted = int(input('Amount needed: '))
        smorttv.append( 359 * numberwhanted )
    else: 
        print('Erorr, try again')
        produtct_select = input('input the item number: ')
        yes = input('Would you like to enter another item to the cart?(y or n):')
if yes == 'n':
        print(f'{list}')
        done = False #ends loop
elif yes == 'y':
        list.append(input('Insert any item into the cart:'))
        yes = input('Would you like to enter another item into the cart?(y or n):')
else:
        done = False #ends loop
#list of shopping cart
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

#printing of puchaced itams
