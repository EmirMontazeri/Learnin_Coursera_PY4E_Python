# A program that asks for hours and pay per hours to calculate gross pay
#in a way that handles non integer inputs.

hours = input('Enter Work Hours: ')
try:
    hf = float(hours)
except: 
    print('Please enter a valid number.')
    quit()

pph = input('Enter Pay / Hours: ')
try:
    pf = float(pph)
except: 
    print('Please enter a valid number.')
    quit()

gpay = hf * pf
print('Gross Pay:', gpay)
