# As one of the most relatable Python projects for beginners with code,
# this program simulates rolling one or two dice.
# It’s also a great way to solidify your understanding of user-defined functions,
# loops, and conditional statements.
# As one of the Python easy projects, it’s a fairly simple program that uses the
# Python random module to replicate the random nature of rolling dice.
# You’ll also notice that we use the os module to clear the screen after you’ve rolled the dice.
# Note that you can change the maximum dice value to any number,
# allowing you to simulate polyhedral dice often used in many board and roleplaying games.
#
# Являясь одним из наиболее подходящих проектов на Python для начинающих программистов,
# эта программа имитирует бросание одного или двух кубиков.
# Это также отличный способ укрепить ваше понимание пользовательских функций,
# циклов и условных операторов.
# Как один из проектов Python easy, это довольно простая программа,
# которая использует модуль Python random для воспроизведения случайного характера бросания кубиков.
# Вы также заметите, что мы используем модуль операционной системы для очистки экрана после того,
# как вы бросили кости.
# Обратите внимание, что вы можете изменить максимальное значение кубика на любое число,
# что позволяет имитировать многогранные кубики,
# часто используемые во многих настольных и ролевых играх.

'''
Dice Roll Generator
-------------------------------------------------------------
'''


import random
import os


def num_die():
  while True:
      try:
          num_dice = input('Number of dice: ')
          valid_responses = ['1', 'one', 'two', '2']
          if num_dice not in valid_responses:
              raise ValueError('1 or 2 only')
          else:
              return num_dice
      except ValueError as err:
          print(err)


def roll_dice():
   min_val = 1
   max_val = 6
   roll_again = 'y'

   while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
       os.system('cls' if os.name == 'nt' else 'clear')
       amount = num_die()

       if amount == '2' or amount == 'two':
           print('Rolling the dice...')
           dice_1 = random.randint(min_val, max_val)
           dice_2 = random.randint(min_val, max_val)

           print('The values are:')
           print('Dice One: ', dice_1)
           print('Dice Two: ', dice_2)
           print('Total: ', dice_1 + dice_2)

           roll_again = input('Roll Again? ')
       else:
           print('Rolling the die...')
           dice_1 = random.randint(min_val, max_val)
           print(f'The value is: {dice_1}')

           roll_again = input('Roll Again? ')


if __name__ == '__main__':
   roll_dice()
