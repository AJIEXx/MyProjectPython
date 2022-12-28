# This Python project uses the standard smtplib, EmailMessage, and datetime modules,
# in addition to pandas and openpyxl (these need to be pip installed,
# as shown below) to send automated birthday emails.
# This program reads from an excel sheet that contains all of your friends’ details
# (see excel sheet format in source code below). It then sends them an email if today is their big day,
# before making a note in your spreadsheet to say they’ve received their email.
# We’ve used the smtplib and EmailMessage modules to create an SSL connection to our email account
# and message. We’ve then used a pandas dataframe to store spreadsheet-style data within the
# Python program (an essential skill for data scientists). Finally, we used date formatting with the
# datetime module’s .strftime() function.
# So, lots of new skills to get to grips with!
# Important note: since May 2022, Google has tightened its restrictions on ‘less secure apps’ accessing Gmail.
# You’ll need to follow some extra steps to use this code with your Gmail account. But don’t worry,
# they’re easy to do, and we’ve listed them for you.
# Go to the ‘manage account’ page for your google account
# Click on Security
# Enable 2FA (use whichever method you prefer)
# Click on ‘App Passwords’
# Click on ‘Select App’ and select ‘Mail’
# Click on ‘Select Device’ & select ‘Other (custom name)’, enter ‘Python Birthday App’
# Click on ‘Generate’ then save this password
# You can now use this app password in the code below to access your Gmail account with no trouble!
#
# Этот проект на Python использует стандартные модули smtplib, EmailMessage и datetime,
# в дополнение к pandas и openpyxl (у них должен быть установлен pip, как показано ниже) для
# автоматической отправки электронных писем на день рождения.
# Эта программа считывает данные с листа Excel, который содержит все данные ваших друзей
# (см. Формат листа Excel в исходном коде ниже). Затем он отправляет им электронное письмо,
# если сегодня у них важный день, прежде чем сделать пометку в вашей электронной таблице, чтобы сообщить,
# что они получили свое электронное письмо.
# Мы использовали модули smtplib и EmailMessage для создания SSL-соединения с нашей учетной записью
# электронной почты и сообщением. Затем мы использовали фрейм данных pandas для хранения данных в формате
# электронных таблиц в программе Python (необходимый навык для специалистов по обработке данных).
# Наконец, мы использовали форматирование даты с помощью функции .strftime() модуля datetime.
# Итак, много новых навыков, с которыми нужно разобраться!
# Важное примечание: с мая 2022 года Google ужесточил свои ограничения на доступ
# "менее безопасных приложений" к Gmail. Вам нужно выполнить несколько дополнительных шагов,
# чтобы использовать этот код в своей учетной записи Gmail. Но не волнуйтесь, их легко сделать,
# и мы перечислили их для вас.
# Перейдите на страницу ‘Управление учетной записью’ для своей учетной записи Google
# Нажмите на Безопасность
# Включите 2FA (используйте любой метод, который вы предпочитаете)
# Нажмите ‘Пароли приложений’
# Нажмите "Выбрать приложение" и выберите "Почта"
# Нажмите "Выбрать устройство" и выберите "Другое (пользовательское имя)", введите "Приложение для дня рождения Python’
# Нажмите "Сгенерировать", затем сохраните этот пароль
# Теперь вы можете использовать этот пароль приложения в коде ниже, чтобы без проблем получить доступ к своей учетной записи Gmail!

'''
Birthday Email Sender
-------------------------------------------------------------
pip install pandas openpyxl
excel file cols:
Name, Email, Birthday (MM/DD/YYYY), Last Sent (YYYY)
'''


import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage


def send_email(recipient, subject, msg):
   GMAIL_ID = 'your_email_here'
   GMAIL_PWD = 'your_password_here'

   email = EmailMessage()
   email['Subject'] = subject
   email['From'] = GMAIL_ID
   email['To'] = recipient
   email.set_content(msg)

   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:
       gmail_obj.ehlo()
       gmail_obj.login(GMAIL_ID, GMAIL_PWD)
       gmail_obj.send_message(email)
   print('Email sent to ' + str(recipient) + ' with Subject: \''
         + str(subject) + '\' and Message: \'' + str(msg) + '\'')


def send_bday_emails(bday_file):
   bdays_df = pd.read_excel(bday_file)
   today = datetime.now().strftime('%m-%d')
   year_now = datetime.now().strftime('%Y')
   sent_index = []

   for idx, item in bdays_df.iterrows():
       bday = item['Birthday'].to_pydatetime().strftime('%m-%d')
       if (today == bday) and year_now not in str(item['Last Sent']):
           msg = 'Happy Birthday ' + str(item['Name'] + '!!')
           send_email(item['Email'], 'Happy Birthday', msg)
           sent_index.append(idx)

   for idx in sent_index:
       bdays_df.loc[bdays_df.index[idx], 'Last Sent'] = str(year_now)

   bdays_df.to_excel(bday_file, index=False)


if __name__ == '__main__':
   send_bday_emails(bday_file='your_bdays_list.xlsx')