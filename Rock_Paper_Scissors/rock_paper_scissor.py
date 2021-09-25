# Names (Me, Partner): Shima Abdulla, Victoria Holmes

while True:
    player1_input = input("Player one: What is your hand shape? Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    player2_input = input("Player two: What is your hand shape? Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    if player1_input == player2_input:
        print("Tie!")
    elif player1_input == "r" and player2_input == "p":
        print("Player 2 wins!")
    elif player2_input == "r" and player1_input == "p":
        print("Player 1 wins!")
    elif player1_input == "r" and player2_input == "s":
        print("Player 1 wins!")
    elif player2_input == "r" and player1_input == "s":
        print("Player 2 wins!")
    elif player1_input == "s" and player2_input == "p":
        print("Player 1 wins!")
    elif player1_input == "p" and player2_input == "s":
        print("Player 2 wins!")
        
    replay_input = input("Do you want to play another round? Enter 'y' for yes or 'n' for no: " )
    if replay_input == "n":
        print("Goodbye!")
        break


        