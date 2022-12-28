# This is one of several Python project ideas that require us to install a new Python library,
# in this case, the requests module. This is not included with the Python standard library,
# so use the pip command shown in the source code to install it on your system.
# With the requests module, we can make HTTP requests to the Fixer API, allowing us to convert one
# currency to another. You’ll likely notice that we’re using a 3rd party API,
# so you’ll need to sign up to get a free API key here. You can then enter your API key into the field shown
# in the source code, and you’ll be ready to go!
# This project allows you to gain some more practice with loops and user input,
# but it expands on this with HTTP requests to retrieve API data in JSON format.
# If you’re unfamiliar with JSON, it’s very similar to a Python dictionary,
# meaning we can access key-value pairs to fetch the data we’re after. In this case,
# we are looking for the currency conversion result from the API call.
# Look at the docs on the Fixer API site for more details on the different data you can retrieve.
#
# Это одна из нескольких идей проекта Python, которые требуют от нас установки новой библиотеки Python,
# в данном случае модуля requests. Это не входит в стандартную библиотеку Python,
# поэтому используйте команду pip, указанную в исходном коде, чтобы установить ее в вашей системе.
# С помощью модуля requests мы можем отправлять HTTP-запросы к API Fixer,
# что позволяет нам конвертировать одну валюту в другую. Вы, вероятно, заметите,
# что мы используем сторонний API, поэтому вам нужно зарегистрироваться, чтобы получить бесплатный ключ
# API здесь. Затем вы можете ввести свой ключ API в поле, указанное в исходном коде,
# и вы будете готовы к работе!
# Этот проект позволяет вам получить больше практики с циклами и пользовательским вводом,
# но он расширяет это с помощью HTTP-запросов для извлечения данных API в формате JSON.
# Если вы не знакомы с JSON, он очень похож на словарь Python, что означает,
# что мы можем получить доступ к парам ключ-значение для извлечения нужных нам данных.
# В данном случае мы ищем результат конвертации валюты из вызова API.
# Посмотрите документы на сайте Fixer API для получения более подробной информации о различных данных,
# которые вы можете получить.

'''
Currency Converter
-------------------------------------------------------------
pip install requests
'''


import requests


def convert_currency():
   init_currency = input('Enter an initial currency: ')
   target_currency = input('Enter a target currency: ')

   while True:
       try:
           amount = float(input('Enter the amount: '))
       except:
           print('The amount must be a numeric value!')
           continue

       if not amount > 0:
           print('The amount must be greater than 0')
           continue
       else:
           break

   url = ('https://api.apilayer.com/fixer/convert?to='
          + target_currency + '&from=' + init_currency +
          '&amount=' + str(amount))

   payload = {}
   headers = {'apikey': 'YOUR API KEY'}
   response = requests.request('GET', url, headers=headers, data=payload)
   status_code = response.status_code

   if status_code != 200:
       print('Uh oh, there was a problem. Please try again later')
       quit()

   result = response.json()
   print('Conversion result: ' + str(result['result']))


if __name__ == '__main__':
   convert_currency()