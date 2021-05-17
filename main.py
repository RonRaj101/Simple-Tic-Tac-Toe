
print("--- TIC TAC TOE --- \n")

game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def show_board():
    print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
    print('-+-+-')
    print(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
    print('-+-+-')
    print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])
    print("\n")


def start_game():
    turn_of = 'X'
    num_of_turns = 0

    show_board()

    for x in range(10):
        print('Player '+turn_of+'')
        position = int(input("Enter Position (1-9): ")) - 1

        if game_board[position] == ' ':
            game_board[position] = turn_of
            num_of_turns += 1
        else:
            print('Cell Already Occupied! Choose Another Position: ')
            continue

        show_board()

        if num_of_turns >= 5:

            if game_board[6] == game_board[7] == game_board[8] != ' ':

               print("\nGame Over.")
               print("Player " + turn_of + " Wins")
               break

            elif game_board[3] == game_board[4] == game_board[5] != ' ':

                print("\nGame Over.")
                print("Player " + turn_of + " Wins")
                break

            elif game_board[0] == game_board[1] == game_board[2] != ' ':

                print("\nGame Over.")
                print("Player " + turn_of + " Wins")
                break

            elif game_board[0] == game_board[3] == game_board[6] != ' ':

               print("\nGame Over.")
               print("Player " + turn_of + " Wins")
               break

            elif game_board[1] == game_board[4] == game_board[7] != ' ':

               print("\nGame Over.")
               print("Player " + turn_of + " Wins")
               break
            elif game_board[2] == game_board[5] == game_board[8] != ' ':

               print("\nGame Over.")
               print("Player " + turn_of + " Wins")
               break

            elif game_board[6] == game_board[4] == game_board[2] != ' ':

               print("\nGame Over.")
               print("Player " + turn_of + " Wins")
               break

            elif game_board[0] == game_board[4] == game_board[8] != ' ':

               print("\nGame Over.")
               print("Player " + turn_of + " Wins")
               break

            elif num_of_turns >= 8:
                print('Game Tied!')

        if turn_of == 'X':
            turn_of = 'O'
        else:
            turn_of = 'X'



start_game()




