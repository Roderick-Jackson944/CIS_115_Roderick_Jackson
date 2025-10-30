creditcardnum = input("enter credit card number:")
def validateCreditCard(ccNum):
    digits = [int(d) for d in str(ccNum) if d.isdigit()]
    Sumofitall = 0
    dubbledit = False

    for i in range(len(digits) -1, -1, -1):
        digit = digits[i]
        if dubbledit:
            digit *= 2
            if digit > 9:
                digit -= 9
        Sumofitall += digit
        dubbledit = not dubbledit
    if Sumofitall % 10 == 0:
        return True
    else:
        return False
if validateCreditCard(creditcardnum) == True:
    print('Number is valid')
else:
    print('number is not valid')