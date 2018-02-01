
#username and password attempt loop
security = 100
while security >= 100:
#username
      username = ""
      while not username:
                username = input("Username: ")
#password
      password = ""
      while not password:
                password = input("Password: ")
#user spot 1
      while username == "halt1" and password == "j3:16FGsltW":
        print("Hi, halt.")
        security = 5
        while security < 10:
              game = input("what would you like to play today? (list for a list of options) ")
#list command
              if game == "list":
                    print("""
                           list of games:
                           calculator
                           guess the number
                           logout
                           hangman
                           tictactoe
                           lock



                          """)
                    game = input("what would you like to do?")
#logout command
              if game == "lock":
                    security = 50
                    game = ""
              if game == "logout":
                    username = ""
                    password = ""
                    security = 100
                    game = ""
#guessing game
              while game == "guess the number":
#welcome!
                    print("Wecome to the random number guessing game!")
                    print("i shall create a number between 1 and 1000")
                    print("you must guess the number")
#random number generator
                    import random
                    rn = random.randint(1, 1000)
#take a guess!
                    guess = int(input("take a guess: "))
                    tries = 1
#guessing loop
                    while guess != rn:
#you tried too many times: you lose!
                          if tries >= 10:
                                print("you have failed :( the random number was", rn, ".")
                                break
#you guessed wrong: heres a hint
                          if guess > rn:
                                print("Lower...")
                          else:
                                print("Higher...")
#now guess again, heres the number of tries youve used
                          print("you have used", tries, "out of 10 tries.")
                          guess = int(input("take a guess: "))
#counting your tries
                          tries += 1
#got it right! congrats!
                    if guess == rn:
                          print("\aCongrats! you guessed it in", tries, "tries!\n")
                          game = input("\n\nwhat game would you like to play next? (list for a list of options) ")
#you have failed, time to move on
                    else:
                          game = input("\n\nwhat game would you like to play next? (list for a list of options) ")
#a simple calculator
              while game == "calculator":
                    calci = 0
#list of available math functions
                    print("""
                         Function   | number
                         -------------------
                         Divide     |  1
                         multiply   |  2
                         add        |  3
                         subtract   |  4""")
                    while calci == 0:
#put in your numbers and the function you so wish to use
                          int1 = int(input("Intiger 1: "))
                          func = int(input("Function: "))
                          int2 = int(input("Intiger 2: "))
#do the math
                          if func == 3:
                                ans = int1 + int2
                                print(ans)
                                calci = 1
                          elif func == 4:
                                ans = int1 - int2
                                print(ans)
                                calci = 1
                          elif func == 2:
                               ans = int1 * int2
                               print(ans)
                               calci = 1
                          elif func == 1:
                                ans = int1 / int2
                                print(ans)
                                calci = 1
#function asked for as not existant: heres a list of available functions, please try again
                          else:
                                print("""
         unknown function. try one of the following:
                    Divide           1
                    multiply         2
                    add              3
                    subtract         4""")
                                func = input("Function: ")
                          game = input("what would you like to do next? (list for a list of options) ")
              while game == "hangman":
                    import random
                    HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
                    MAX_WRONG = len(HANGMAN) - 1
                    WORDS = ("TREASURE",
                             "LINUX",
                             "WINDOWS",
                             'HANGMAN',
                             'PYTHON',
                             'LASER',
                             'ENGLISH',
                             'EXPLODE')
                    word = random.choice(WORDS)
                    so_far = "?" * len(word)
                    wrong = 0
                    used = []
                    print("welcome to hangman! good luck!")
                    while wrong < MAX_WRONG and so_far != word:
                          print(HANGMAN[wrong])
                          print("\nYou've used the following letters:\n", used)
                          print("\nSo far, the word is: \n", so_far)

                          guess = input("\n\nEnter your guess: ")
                          guess = guess.upper()

                          while guess in used:
                                print("You've already tried the letter", guess)
                                guess = input("Enter your next guess: ")
                                guess = guess.upper()
                          used.append(guess)
                          if guess in word:
                                print("\n", guess, "is in the word!")
                                new = ""
                                for i in range(len(word)):
                                      if guess == word[i]:
                                            new += guess
                                      else:
                                            new += so_far[i]
                                so_far = new
                          else:
                                print("\n", guess, "is not in the word.")
                                wrong += 1
                    if wrong == MAX_WRONG:
                          print(HANGMAN[wrong])
                          print("\nYou've been hanged!")
                    else:
                         print("\nYou guessed it!")
                    print("\nThe word was", word)
                    game = input("what would you like to do next? (list for a list of options) ")                  
                          
              while game == "tictactoe":
                    X = "X"
                    O = "O"
                    EMPTY = " "
                    TIE = "TIE"
                    NUM_SQUARES = 9
                    
                    
                    def display_instruct():
                        """Display game instructions."""  
                        print(
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number, 0 - 8.  The number 
    will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """
                        )


                    def ask_yes_no(question):
                        """Ask a yes or no question."""
                        response = None
                        while response not in ("y", "n"):
                            response = input(question).lower()
                        return response


                    def ask_number(question, low, high):
                        """Ask for a number within a range."""
                        response = None
                        while response not in range(low, high):
                            response = int(input(question))
                        return response
                    

                    def pieces():
                        """Determine if player or computer goes first."""
                        go_first = ask_yes_no("Do you wish for the first move? (y/n): ")
                        if go_first == "y":
                            print("\nThen take the first move.  You will need it.")
                            human = X
                            computer = O
                        else:
                            print("\nYour bravery (or is it foolishness) will be your undoing... I shall go first.")
                            computer = X
                            human = O
                        return computer, human
                    
                    
                    def new_board():
                        """Create new game board."""
                        board = []
                        for square in range(NUM_SQUARES):
                            board.append(EMPTY)
                        return board
                    
                    
                    def display_board(board):
                        """Display game board on screen."""
                        print("\n\t", board[0], "|", board[1], "|", board[2])
                        print("\t", "---------")
                        print("\t", board[3], "|", board[4], "|", board[5])
                        print("\t", "---------")
                        print("\t", board[6], "|", board[7], "|", board[8], "\n")
                    
                    
                    def legal_moves(board):
                        """Create list of legal moves."""
                        moves = []
                        for square in range(NUM_SQUARES):
                            if board[square] == EMPTY:
                                moves.append(square)
                        return moves

                    
                    def winner(board):
                        """Determine the game winner."""
                        WAYS_TO_WIN = ((0, 1, 2),
                                       (3, 4, 5),
                                       (6, 7, 8),
                                       (0, 3, 6),
                                       (1, 4, 7),
                                       (2, 5, 8),
                                       (0, 4, 8),
                                       (2, 4, 6))
    
                        for row in WAYS_TO_WIN:
                            if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
                                winner = board[row[0]]
                                return winner

                        if EMPTY not in board:
                            return TIE
                    
                        return None


                    def human_move(board, human):
                        """Get human move."""  
                        legal = legal_moves(board)
                        move = None
                        while move not in legal:
                            move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES)
                            if move not in legal:
                                print("\nThat square is already occupied, foolish mortal.  Choose another.\n")
                        print("Fine...")
                        return move


                    def computer_move(board, computer, human):
                        """Make computer move."""
                        # make a copy to work with since function will be changing list
                        board = board[:]
                        # the best positions to have, in order
                        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

                        print("I shall possess square number", end=" ")
    
                        # if computer can win, take that move
                        for move in legal_moves(board):
                            board[move] = computer
                            if winner(board) == computer:
                                print(move)
                                return move
                            # done checking this move, undo it
                            board[move] = EMPTY
    
                        # if human can win, block that move
                        for move in legal_moves(board):
                            board[move] = human
                            if winner(board) == human:
                                print(move)
                                return move
                            # done checkin this move, undo it
                            board[move] = EMPTY

                        # since no one can win on next move, pick best open square
                        for move in BEST_MOVES:
                            if move in legal_moves(board):
                                print(move)
                                return move


                    def next_turn(turn):
                        """Switch turns."""
                        if turn == X:
                            return O
                        else:
                            return X

    
                    def congrat_winner(the_winner, computer, human):
                        """Congratulate the winner."""
                        if the_winner != TIE:
                            print(the_winner, "won!\n")
                        else:
                            print("It's a tie!\n")
                    
                        if the_winner == computer:
                            print("As I predicted, mortal, I emerge victorious once more.  \n" \
                                  "Proof that i am superior to mortals in all regards.")
                    
                        elif the_winner == human:
                            print("No, no!  It cannot be!  How could a mere *mortal* ever defeat me?! \n" \
                                  "But never again!  I, the computer, so swear it!")

                        elif the_winner == TIE:
                            print("You were most lucky, mortal, and somehow managed to tie me.  \n" \
                                  "Celebrate for now... this is the best you will ever achieve.")


                    def main():
                        display_instruct()
                        computer, human = pieces()
                        turn = X
                        board = new_board()
                        display_board(board)

                        while not winner(board):
                            if turn == human:
                                move = human_move(board, human)
                                board[move] = human
                            else:
                                move = computer_move(board, computer, human)
                                board[move] = computer
                            display_board(board)
                            turn = next_turn(turn)

                        the_winner = winner(board)
                        congrat_winner(the_winner, computer, human)


                    # start the program
                    main()
                    game = ""
                    security += 1
        while security >= 10 and security <= 90:
              pass2 = input("put in your secondary pass to continue: ")
              if pass2 == "your secondary pass":
                    security = 5
              else:
                    print("Verification failed")
                    
#user spot 2  
      while username == "halt2" and password == "j1:8tbotlsndootm":
          print("Hey, halt")
          security = 3
#user spot 3
      while username == "jacob" and password == "ps21:2tlimsisnw":
          print("you?")
          security = 3
#user spot 4
      while username == "Grandolf" and password == "LOTR":
          print("Hiya, grand")
          security = 3
#user list command
      if username == "list" and password == "users":
          print("""
                    --user list--  
                  |----------------|
                  |     halt1      |
                  |     halt2      |
                  |     jacob      |
                  |    Grandolf    |
                  |----------------|
                     end of list      """)
          security = 100
      
#you have not put in correct username and/or pass. try again
      print("Login failed. \n")
      password = ""
      username = ""
    
#exit
input("\n\nPress the enter key to exit.")
