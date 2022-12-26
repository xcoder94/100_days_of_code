from game_data import data
from art import logo, vs
import random
import os



people_data = data
player_score = 0

a_rand_pos = None
b_rand_pos = None
next_a_pos = None

game_is_on = True
while game_is_on:
    os.system('clear')
    print(len(people_data))
    print(logo)
    if player_score == 0:
        a_rand_pos = random.randint(0, len(people_data))
    else:
        a_rand_pos = next_a_pos
        print(f'You\'re right! current score: {player_score}')
    a_name = people_data[a_rand_pos]['name']
    a_descr = people_data[a_rand_pos]['description']
    a_followers = people_data[a_rand_pos]['follower_count']
    a_country = people_data[a_rand_pos]['country']
    b_rand_pos = random.randint(0, len(people_data))
    b_name = people_data[b_rand_pos]['name']
    b_descr = people_data[b_rand_pos]['description']
    b_followers = people_data[b_rand_pos]['follower_count']
    b_country = people_data[b_rand_pos]['country']    
        
    print(f'Compare A: {a_name}, {a_descr}, from {a_country}')
    print(vs)
    print(f'Against B: {b_name}, {b_descr}, from {b_country}')
    player_choice = input('Who has more followers? \'A\' or \'B\': ').lower()
    
    if player_choice == 'a' and a_followers > b_followers:
        player_score += 1
        next_a_pos = a_rand_pos
        people_data.pop(b_rand_pos)
        print('correct')
    elif player_choice == 'b' and b_followers > a_followers:
        player_score += 1
        next_a_pos = b_rand_pos
        people_data.pop(a_rand_pos)
    else:
        game_is_on = False
        print('not correct')


