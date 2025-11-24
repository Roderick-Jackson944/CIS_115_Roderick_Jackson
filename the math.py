Usb = []
macbookpro = []
arduino = []
ringcam = []
smorttv = []
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