# This Python project idea is fun! Here, we’ve created a countdown timer that asks the user for
# a number of seconds via user input, and it then counts down, second by second, until it displays a message.
# We’ve used the Python time module’s .sleep() function to pause for 1-second intervals.
# We combine this with some nifty string formatting to produce the countdown display.
#
# Эта идея проекта на Python - это весело! Здесь мы создали таймер обратного отсчета,
# который запрашивает у пользователя количество секунд с помощью пользовательского ввода,
# а затем отсчитывает секунду за секундой, пока не отобразится сообщение.
# Мы использовали функцию .sleep() модуля Python time для приостановки на 1-секундные интервалы.
# Мы объединяем это с некоторым изящным форматированием строк для отображения обратного отсчета.


'''
Countdown Timer
-------------------------------------------------------------
'''


import time


def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print('Lift off!')


if __name__ == '__main__':
   user_time = int(input("Enter a time in seconds: "))
   countdown(user_time)

