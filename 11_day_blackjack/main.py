from art import logo
import random
import os

os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def current_time_print(player_cards, comp_cards):
    print(f'Your cards {player_cards}, current score {sum(player_cards)}')
    print(f'Computer\'s first card: {comp_cards[0]}')


def final_hand_print(player_cards, comp_cards):
    print(f'Your final hand {player_cards}, final score: {sum(player_cards)}')
    print(f'Computer\'s final hand {comp_cards}, final score: {sum(comp_cards)}')



def start_game(card_list):
    os.system('clear')
    print(logo)
    player_cards = random.choices(card_list, k=2)
    comp_cards = random.choices(card_list, k=2)

    if sum(player_cards) == 21:
        final_hand_print(player_cards, comp_cards)
        print('It\'s black jack in your hands. You win')
    else:
        current_time_print(player_cards, comp_cards)
        player_taking_cards = True
        while player_taking_cards:
            next_action = input('Type \'y\' to get another card, type \'n\' to pass: ').lower()
            if next_action == 'y':
                player_cards.append(random.choice(card_list))
                current_time_print(player_cards, comp_cards)
                if sum(player_cards) > 21:
                    final_hand_print(player_cards, comp_cards)
                    print('You lose')
                    player_taking_cards = False
            else:
                player_taking_cards = False
                continue
                
        if sum(comp_cards) < 17:
            while sum(comp_cards) < 17:
                comp_cards.append(random.choice(card_list))

        if sum(comp_cards) > 21:
            final_hand_print(player_cards, comp_cards)
            print('You win')
        else:
            final_hand_print(player_cards, comp_cards)
            if 22 > sum(player_cards) > sum(comp_cards):
                print('You win')
            elif sum(player_cards) == sum(comp_cards):
                print('It is a draw')
            else:
                print('You lose')



game_is_on = True
while game_is_on:
    intro_question = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ').lower()
    if intro_question == 'y':
        start_game(cards)
    else:
        game_is_on = False
