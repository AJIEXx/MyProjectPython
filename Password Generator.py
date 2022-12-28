# This is an interesting Python project that uses the secrets and string modules to generate
# a strong and secure password, much like you can with popular password managers.
# The string module obtains all possible letters, digits, and special characters,
# while the secrets module allows us to obtain cryptographically secure passwords.
# The code for this project is relatively simple as it uses a loop to continually generate passwords
# until it contains at least one special character and two digits.
# You can, of course, modify this to fit your own super-strong password rules!
#
# Это интересный проект на Python, который использует секретные и строковые модули для создания надежного и
# безопасного пароля, как вы можете с помощью популярных менеджеров паролей.
# Модуль string получает все возможные буквы, цифры и специальные символы, в то время как
# модуль secrets позволяет нам получать криптографически безопасные пароли.
# Код для этого проекта относительно прост, поскольку он использует цикл для непрерывной генерации паролей,
# пока он не будет содержать хотя бы один специальный символ и две цифры. Вы, конечно, можете изменить это,
# чтобы соответствовать вашим собственным правилам сверхнадежного пароля!

'''
Password Generator
-------------------------------------------------------------
'''


import secrets
import string


def create_pw(pw_length=12):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False

   while not pw_strong:
       pwd = ''
       for i in range(pw_length):
           pwd += ''.join(secrets.choice(alphabet))

       if (any(char in special_chars for char in pwd) and
               sum(char in digits for char in pwd) >= 2):
           pw_strong = True

   return pwd


if __name__ == '__main__':
   print(create_pw())

