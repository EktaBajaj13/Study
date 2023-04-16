import random

#Ask the user to enter his/her name
name = input('Enter your name : ')

#Print a message for the user
print('\nGood Luck ! ',name)

#Initialize the word list from which a random word will be picked up by the computer
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

#Prediction done
word = random.choice(words)

#Initialize the number of turns
turns = 12

#Print the message to start the game
print('Guess the characters : ')

#Initialize the string to store the guesses from the user
guesses = ''

#The loop continues until the number of turns reaches 0
while turns != 0 :
    
    #Initialize the fail counter to 0
    f = 0
    
    #Loop through the predicted word to pick up each letter in the word
    for letter in word :
        
        #If the letter in the word matches with the user's guesses
        if letter in guesses :
            
            #Print the letter
            print(letter, end = '')
            
        #Otherwise, if the letter in the word doesn't match with the user's guesses
        else :
            
            #Print the space in its place
            print('_ ', end = '')
            
            #Increase the fail counter to 1
            f = 1
            
    #Bring the cursor in the next line
    print('\n')
    
    #If the fail counter is 0 which means there are no letters left to be guessed
    if f == 0 :
        
        #Print success message for the user
        print('You Win\n')
        
        #Print the whole word which has been predicted
        print('The word is : ',word)
        
        #Break the loop to come of the code
        break
    
    #Otherwise, if the fail counter is 1 which means there are still letters left to be guessed
    else :
        
        #Ask the user to guess a letter
        guess = input('Enter a character : ')
        
        #Add the guessed letter in the string of guessed letters
        guesses += guess
        
    #If the guessed letter is not in the predicted word
    if guess not in word :
        
        #Print the wrong message for the user
        print('Wrong')
        
        #Reduce the number of turns by 1
        turns -= 1
        
        #Print the message for the user displaying the number of turns
        print('You have ',turns,' turns left')

#If number of turns left is 0
if turns == 0 :
    #Print the failed message for the user
    print('You Loose')

#User to press any key to exit the screen
ec = input('Press any key to exit ..... ')