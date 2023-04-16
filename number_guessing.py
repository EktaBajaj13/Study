import random

#Ask the user to enter the lower limit number for prediction
lb = input('Enter the lower bound : ')

#Ask the user to enter the upper limit number for prediction
ub = input('Enter the upper bound : ')

#Convert the lower limit number and upper limit number from string to integer
lb = int(lb)
ub = int(ub)

#Generate the random number which is the prediction
gn = random.randint(lb, ub)
print('\nThe computer has predicted the number. Lets start!')

#Initialize the user guessed number to the infinite value
ugn = float('inf')

#Initialize the counter for the number of guesses
counter = 0

#Ask the user to enter the maximum number of guesses which they want
mn = input('Enter the maximum number of guesses : ')

#Convert the maximum number of guesses from string to integer
mn = int(mn)

#The loop will continue until the user guessed number is equal to the prediction
while ugn != gn :
    
    #Initialize the fail counter to 0
    f = 0
    
    #Ask the user to enter the number they are guessing
    ugn = input('Enter the number you are guessing in the range {l} and {u} : '.format(l = lb, u = ub))
    
    #Conver the user guessed number from string to integer
    ugn = int(ugn)
    
    #Increase the counter for the number of guesses
    counter += 1
    
    #If the user has guessed a smaller number as compared to the prediction
    if ugn < gn :
        
        #Initialize the message to be printed on the screen
        tx = 'Try Again! You guessed too small.'
        
        #Change the lower limit for prediction to 1 greater than the user guessed number
        lb = ugn + 1
        
        #Set the fail counter to 1
        f = 1
        
    #Otherwise, if the user has guessed a higher number as compared to the prediction
    elif ugn > gn :
        
        #Initialize the message to be printed on the screen
        tx = 'Try Again! You guessed too high.'
        
        #Change the upper limit for prediction to 1 less than the user guessed number
        ub = ugn - 1
        
        #Set the fail counter to 1
        f = 1
        
    #If the number of guesses counter is less than the maximum number of guesses and the fail counter is 1 which means the user has not guessed properly
    if counter < mn and f == 1 :
        
        #Print the message on the screen which was set previously
        print(tx)
        
    #Otherwise, if the number of guesses counter has reached the maximum number of guesses or the fail counter is 0 which means the user has guessed properly
    else :
        
        print('\n')
        
        #Break the loop so no further guesses are required
        break
    
#If the fail counter is 0 which means the user has guessed properly
if f == 0 :
    
    #Print the success message and the number of guesses
    print('Congratulations!')
    print('\nTotal Number of Guesses : ',counter)
    
#Otherwise, if the number of guesses counter has exceeded the maximum number of guesses
else :
    
    #Print the failure message
    print('The predicted number is :', gn, '\nBetter Luck Next Time!')
    
ec = input('Press any key to exit ..... ')