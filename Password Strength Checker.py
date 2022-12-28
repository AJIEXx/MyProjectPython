# This Python project lets you check whether your password is strong enough.
# It does this by checking the number of letters, numbers, special characters,
# and whitespace characters within a given password and generating a score based on these results.
# So, it’s another great way to learn about conditional statements, functions, and string formatting.
# We also use the string and getpass modules from the Python standard library.
# This allows us to access the full range of string characters to compare with our
# password’s character composition, while the .getpass() function lets us hide our
# password when we enter it.
#
# Этот проект на Python позволяет вам проверить, достаточно ли надежен ваш пароль.
# Это делается путем проверки количества букв, цифр,
# специальных символов и пробелов в заданном пароле и создания оценки на основе этих результатов.
# Итак, это еще один отличный способ узнать об условных операторах, функциях и форматировании строк.
# Мы также используем модули string и getpass из стандартной библиотеки Python.
# Это позволяет нам получить доступ к полному набору строковых символов для сравнения с составом
# символов нашего пароля, в то время как функция .getpass() позволяет нам скрывать наш пароль
# при его вводе.

'''
Password Strength Checker
-------------------------------------------------------------
'''


import string
import getpass


def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

   if strength == 1:
       remarks = ('That\'s a very bad password.'
           ' Change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s a weak password.'
           ' You should consider using a tougher password.')
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
           ' But you could make it even more secure.')
   elif strength == 5:
       remarks = ('Now that\'s one hell of a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')


def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input(
           'Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input(
           'Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Exiting...')
           return False
       else:
           print('Invalid input...please try again. \n')


if __name__ == '__main__':
   print('===== Welcome to Password Strength Checker =====')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)

