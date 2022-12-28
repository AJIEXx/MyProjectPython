# This Rock Paper Scissors program simulates the universally popular game
# with functions and conditional statements.
# So, what better way to get these critical concepts under your belt?
# As one of many Python coding projects that imports additional libraries,
# this program uses the standard library’s random, os, and re modules.
# Take a look at the code below,
# and you’ll see that this Python project idea asks the user to make
# the first move by passing in a character to represent rock, paper,
# or scissors. After evaluating the input string,
# the conditional logic checks for a winner.
# After evaluating the input string, the conditional logic checks for a winner.
#
# Эта программа "Камень, ножницы, бумага" имитирует популярную игру с функциями и
# условными операторами. Итак, какой лучший способ использовать эти важные концепции?
# Как один из многих проектов программирования на Python,
# который импортирует дополнительные библиотеки, эта программа использует модули random,
# os и re стандартной библиотеки.
# Взгляните на приведенный ниже код, и вы увидите,
# что в этой идее проекта Python пользователю предлагается сделать первый ход,
# передав символ, представляющий камень, ножницы или бумагу.
# После оценки входной строки условная логика проверяет победителя.

'''
Rock Paper Scissors
-------------------------------------------------------------
'''


import random
import os
import re


def check_play_status():
  valid_responses = ['yes', 'no']
  while True:
      try:
          response = input('Do you wish to play again? (Yes or No): ')
          if response.lower() not in valid_responses:
              raise ValueError('Yes or No only')

          if response.lower() == 'yes':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Thanks for playing!')
              exit()

      except ValueError as err:
          print(err)


def play_rps():
   play = True
   while play:
       os.system('cls' if os.name == 'nt' else 'clear')
       print('')
       print('Rock, Paper, Scissors - Shoot!')

       user_choice = input('Choose your weapon'
                           ' [R]ock], [P]aper, or [S]cissors: ')

       if not re.match("[SsRrPp]", user_choice):
           print('Please choose a letter:')
           print('[R]ock, [P]aper, or [S]cissors')
           continue

       print(f'You chose: {user_choice}')

       choices = ['R', 'P', 'S']
       opp_choice = random.choice(choices)

       print(f'I chose: {opp_choice}')

       if opp_choice == user_choice.upper():
           print('Tie!')
           play = check_play_status()
       elif opp_choice == 'R' and user_choice.upper() == 'S':
           print('Rock beats scissors, I win!')
           play = check_play_status()
       elif opp_choice == 'S' and user_choice.upper() == 'P':
           print('Scissors beats paper! I win!')
           play = check_play_status()
       elif opp_choice == 'P' and user_choice.upper() == 'R':
           print('Paper beats rock, I win!')
           play = check_play_status()
       else:
           print('You win!\n')
           play = check_play_status()


if __name__ == '__main__':
   play_rps()
