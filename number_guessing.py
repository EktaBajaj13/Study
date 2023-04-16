import random
lb = input('Enter the lower bound : ')
ub = input('Enter the upper bound : ')
lb = int(lb)
ub = int(ub)
gn = random.randint(lb, ub)
print('\nThe computer has predicted the number. Lets start!')
ugn = float('inf')
counter = 0
mn = input('Enter the maximum number of guesses : ')
mn = int(mn)
while ugn != gn :
    f = 0
    ugn = input('Enter the number you are guessing in the range {l} and {u} : '.format(l = lb, u = ub))
    ugn = int(ugn)
    counter += 1
    if ugn < gn :
        tx = 'Try Again! You guessed too small.'
        lb = ugn + 1
        f = 1
    elif ugn > gn :
        tx = 'Try Again! You guessed too high.'
        ub = ugn - 1
        f = 1
    if counter < mn and f == 1 :
        print(tx)
    else :
        print('\n')
        break
if f == 0 :
    print('Congratulations!')
    print('\nTotal Number of Guesses : ',counter)
else :
    print('The predicted number is :', gn, '\nBetter Luck Next Time!')

