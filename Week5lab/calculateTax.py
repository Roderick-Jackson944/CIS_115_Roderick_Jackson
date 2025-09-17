num1 = input ('input subtotal:')
taxed = float(num1) * .0725
total = float(num1) + float(taxed)
print ('tax is {0} total purchace is {1}'.format(taxed, total))