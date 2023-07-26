from random import randrange

###########################################################################
#Function to display the current board condition
###########################################################################
def display_board(board):

    #Creating the view of the board
    boundary = "+-------+-------+-------+"
    blank_line = "|       |       |       |"
    numbered_line = "|   {a}   |   {b}   |   {c}   |"

    #Printing the board
    print(boundary)

    #Looping through each row in the board
    for row in board :
        print(blank_line)

        #Printing the proper move at each position in the board
        print(numbered_line.format(a = row[0], b = row[1], c = row[2]))
        
        print(blank_line)
        print(boundary)

###########################################################################
#Function to input the move from the user
###########################################################################
def enter_move(board):

    #Calling the function to get the list of free fields on the board
    free_fields = make_list_of_free_fields(board)

    #Looping until the conditon is met inside the loop to break it
    while True :
        #Prompting the user to enter the number of the field for his/her move
        move = int(input("Enter your move: "))

        #Checking if the move entered by the user is valid or not
        if move >= 1 and move <= 9 :
            #Counter to confirm that a valid and free move has been entered by the user
            counter = 0

            #Looping through each row in the board
            for row in range(3) :

                #Looping through each column in the row
                for column in range(3) :

                    #Checking if a particular field is a part of free fields list
                    if (row, column) in free_fields :

                        #Checking if the field contains the user move or not
                        if board[row][column] == move :
                            #Assigning the user's value to the field
                            board[row][column] = '0'

                            #Incrementing the counter to show that a proper move has been entered
                            counter += 1
                            #Breaking through the loop
                            break

                #Checking the counter value to see if a proper move has been made
                if counter != 0 :
                    #Breaking through the loop
                    break

            #Checking the counter value to see if a proper move has been made
            if counter != 0 :
                #Breaking through the loop
                break

            #Otherwise, the field is not free
            else :
                #Printing the relevant message to the user
                print("The cell is already occupied.....Try again !")

        #Otherwise, the move is invalid
        else :
            #Printing the relevant message to the user
            print("Invalid move.....Try again !")

###########################################################################
#Function to get the list of free fields
########################################################################### 
def make_list_of_free_fields(board):

    #Initializing the list of free fields
    free_fields = []

    #Looping through each row in the board
    for row in range(3) :

        #Looping through each column in the row
        for column in range(3) :
            #Assigning the current value in a variable
            value = board[row][column]

            #If the value is not a 0 or x, then this is a free field
            if value not in ('x', '0') :
                #Appending the field into the free fields list
                free_fields.append((row, column))

    #Returning the free fields list
    return free_fields

###########################################################################
#Function to check and declare the winner, if any
########################################################################### 
def victory_for(board, sign):

    #Initializing the scenarios for winning
    win_scenario = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
        ]

    #Initializing the variables
    sign_occupied_fields = []
    v_sign = False

    #Looping through each row in the board
    for row in range(3) :

        #Looping through each column in the row
        for column in range(3) :
            #If the field contains a value
            if board[row][column] == sign :
                #Append that field in the list
                sign_occupied_fields.append((row, column))

    #If the fields containing the particular sign are greater than or equal to 3, only then it can be a win scenario
    if len(sign_occupied_fields) >= 3 :
        #Sorting the list
        sign_occupied_fields.sort()
        
        #Looping through the win scenarios
        for w in win_scenario :
            #Initializing the counter to count the match
            win_counter = 0

            #Looping through each list of the win scenario nested list
            for i in range(3) :

                #If any win scenario tuple matches the field occupied by the particular sign
                if w[i] in sign_occupied_fields :
                    #Increment the counter by 1
                    win_counter += 1

                #Otherwise, move to the next list of win scenario nested list
                else :
                    break

            #If the counter has reached 3, then its a win
            if win_counter == 3 :
                #Initializing the variable to indicate a win
                v_sign = True

                #If the sign is a 0, the user has won
                if sign == '0' :
                    #Printing the relevant message
                    print("You won!")

                #Otherwise, the computer has won
                else :
                    #Printing the relevant message
                    print("Computer won!")

                #Exiting the loop in case a win scenario has been found
                break

    #Returning the value of the variable indicating a win or not
    return v_sign

###########################################################################
#Function to enter the computer's move
########################################################################### 
def draw_move(board):

    #Calling the function to get the list of free fields on the board
    free_fields = make_list_of_free_fields(board)

    #Generating a random number from 0 till the maximum length of the free fields list
    c_move = randrange(len(free_fields))

    #Getting the row of the field corresponding to the index number picked up randomly by the code
    row = (free_fields[c_move])[0]

    #Getting the column of the field corresponding to the index number picked up randomly by the code
    column = (free_fields[c_move])[1]

    #Assigning x to the value in that field
    board[row][column] = 'x'

###########################################################################
#Main Logic to run the Tic Tac Toe Game
########################################################################### 

#Initializing the variable to put the default value on the board
num = 1

#Creating an empty list for the board at the starting of the game
board = [[], [], []]

#Looping through each row in the board
for row in range(3) :

    #Looping through each column in the row
    for column in range(3) :
        #Assigning the default value to each field on the board
        board[row].append(num)

        #Incrementing the value to the next default value
        num += 1

#Assigning x to the middle field of the board showing the computer's first turn
board[1][1] = 'x'

#Display the board after the computer's first turn
display_board(board)

#Initializing the variable to identify user's or computer's turn
counter = 0

#Initializing the value to show the sign - 0 or x
sign = ''

#Setting the default value of the victory variable as False indicating no victory
victory_sign = False

#Initializing the list of free fields
free_sign = []

#Looping through the loop until the specific condition is satisfied inside the loop
while True :

    #If the counter is an even number
    if counter % 2 == 0 :
        #This is the user's turn
        sign = '0'

        #Entering the user's move
        enter_move(board)

    #Otherwise, if the counter is an odd number
    else :
        #This is the computer's turn
        sign = 'x'

        #Entering the computer's move
        draw_move(board)

    #Incrementing the ocunter to decide the next turn
    counter += 1

    #Displaying the board after each move
    display_board(board)

    #Checking if its a victory or not after each move
    victory_sign = victory_for(board, sign)

    #If the victory sign is True
    if victory_sign :
        #Either the user or the computer has won so breaking the loop and exiting
        break

    #Calling the function to get the list of free fields on the board 
    free_sign = make_list_of_free_fields(board)

    #If there is no free field left on the board
    if not free_sign :
        #Then its a draw
        print("Draw")
        #Breaking the loop and exiting
        break
