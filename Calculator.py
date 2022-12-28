As one of the easy Python projects, this program creates a basic calculator application
with addition, subtraction, multiplication, and division functions.
This is one of the Python practice projects that are great for learning how to use loops,
functions, conditional statements, user input, and string formatting.
We’ve also used the Python os module to clear the screen after the user completes their calculation actions.

Как один из простых проектов на Python, эта программа создает базовое приложение-калькулятор с функциями
сложения, вычитания, умножения и деления.
Это один из практических проектов на Python, который отлично подходит для изучения того,
как использовать циклы, функции, условные операторы, пользовательский ввод и форматирование строк.
Мы также использовали модуль Python os для очистки экрана после завершения пользователем своих
вычислительных действий.

'''
Calculator
-------------------------------------------------------------
'''


import os


def addition():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Addition')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   ans = num_1 + num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans += num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def subtraction():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Subtraction')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   ans = num_1 - num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans -= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def multiplication():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Multiplication')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   ans = num_1 * num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       ans *= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def division():
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Division')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   while num_2 == 0.0:
       print('Please enter a second number > 0')
       num_2 = float(input('Enter another number: '))

   ans = num_1 / num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       while num == 0.0:
           print('Please enter a number > 0')
           num = float(input('Enter another number: '))
       ans /= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]


def calculator():
   quit = False
   while not quit:
       results = []
       print('Simple Calculator in Python!')
       print('Enter \'a\' for addition')
       print('Enter \'s\' for substraction')
       print('Enter \'m\' for multiplication')
       print('Enter \'d\' for division')
       print('Enter \'q\' to quit')

       choice = input('Selection: ')

       if choice == 'q':
           quit = True
           continue

       if choice == 'a':
           results = addition()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 's':
           results = subtraction()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 'm':
           results = multiplication()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 'd':
           results = division()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       else:
           print('Sorry, invalid character')


if __name__ == '__main__':
   calculator()