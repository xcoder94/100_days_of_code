# from art import *
# Art = text2art("TICTACTOE", font='block',)
board = '\n 1 | 2 | 3\n-----------\n 4 | 5 | 6\n-----------\n 7 | 8 | 9'

print(board)
poses = {
    '1': '',
    '2': '',
    '3': '',
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': '',
    '9': ''
}


def update_winner_positions(poses):
    return [
        [poses['1'], poses['2'], poses['3']],
        [poses['4'], poses['5'], poses['6']],
        [poses['7'], poses['8'], poses['9']],
        [poses['1'], poses['4'], poses['7']],
        [poses['2'], poses['5'], poses['8']],
        [poses['3'], poses['6'], poses['9']],
        [poses['1'], poses['5'], poses['9']],
        [poses['3'], poses['5'], poses['7']]
    ]


def check(list_for_check, player_symbol):
    return all(i == player_symbol for i in list_for_check)


def check_winner(winner_positions_list, player_symbol):
    for positions in winner_positions_list:
        if check(positions, player_symbol):
            return True
    return False


first_player_name = input("Enter your name player 1 for X: ").capitalize()
second_player_name = input("Enter your name player 2 for O: ").capitalize()

x_count = 0
o_count = 0
game_is_going = True
while game_is_going:
    print(board)
    available_positions = [k for k, v in poses.items() if v == '']
    if not available_positions:
        print("The game is a tie!")
        break
    firs_player_position = None
    right_pos_for_first_player = True
    while right_pos_for_first_player:
        firs_player_position = input(f"Player {first_player_name} enter a position between {available_positions}: ")
        if firs_player_position in available_positions:
            right_pos_for_first_player = False
        else:
            print(f"Position is not available. Please choose available position in {available_positions}")
    poses[firs_player_position] = 'X'
    board = board.replace(firs_player_position, 'X')
    x_count += 1
    if x_count >= 3:
        if check_winner(update_winner_positions(poses), 'X'):
            print(f'{first_player_name} wins')
            game_is_going = False
            break
    print(board)
    available_positions = [k for k, v in poses.items() if v == '']
    if not available_positions:
        print("The game is a tie!")
        break
    second_player_position = None
    right_pos_for_second_player = True
    while right_pos_for_second_player:
        second_player_position = input(f"Player {second_player_name} enter a position between {available_positions}: ")
        if second_player_position in available_positions:
            right_pos_for_second_player = False
        else:
            print(f"Position is not available. Please choose available position in {available_positions}")
    poses[second_player_position] = 'O'
    board = board.replace(second_player_position, 'O')
    o_count += 1
    if o_count >= 3:
        if check_winner(update_winner_positions(poses), 'O'):
            print(f'{second_player_name} wins')
            game_is_going = False
            break
    print(board)
