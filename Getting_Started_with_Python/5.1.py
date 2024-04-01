# Write a program which repeatedly reads number until the user enters "done".
#Once "done" is entered, print out the total, count, and average of the numbers.
#If the User enters anything other than a number, detect their mistake using try
#and execpt and print an error message abd skip to the next number.

cnt = 0
ttl = 0.0

while 1 :
    ipt = input('Enter a number:')
    if ipt == 'done' :
        break
    
    try:
        f_ipt = float(ipt)
    except:
        print('Enter a valid number.')
        continue

    cnt = cnt + 1
    ttl = ttl + f_ipt
    
print('All Done')
print( 'Count=',cnt,'Total=',ttl,'Average=',ttl/cnt)
