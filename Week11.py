creditcardnum = input("enter credit card number:")
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
else:
    print('number is not valid')