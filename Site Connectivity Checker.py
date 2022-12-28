# This Python project uses the urllib and tkinter modules to test website connectivity.
# We’ve used the tkinter module to create a GUI allowing users to enter a web address. Much like our previous examples, this includes labels, buttons, and entry fields.
# After we’ve collected the user’s web address, we pass this to our user-defined function to return a HTTP status code for the current website via the urllib .getcode() function.
# For this example, we simply determine whether the HTTP code is 200. If it is, we know the site is working; otherwise, we inform the user that it is unavailable.
# You could expand this code to consider a more granular approach to handling the various HTTP response codes, so feel free to add this!
#
# Этот проект на Python использует модули urllib и tkinter для тестирования подключения к веб-сайту.
# Мы использовали модуль tkinter для создания графического интерфейса, позволяющего пользователям вводить веб-адрес. Как и в наших предыдущих примерах, сюда входят метки, кнопки и поля ввода.
# После того, как мы собрали веб-адрес пользователя, мы передаем его нашей пользовательской функции, чтобы вернуть код состояния HTTP для текущего веб-сайта через функцию модуля urllib .getcode() .
# Для этого примера мы просто определяем, равен ли HTTP-код 200. Если это так, мы знаем, что сайт работает; в противном случае мы сообщаем пользователю, что он недоступен.
# Вы могли бы расширить этот код, чтобы рассмотреть более детальный подход к обработке различных кодов ответов HTTP, поэтому не стесняйтесь добавлять это!

'''
Site Connectivity Checker
-------------------------------------------------------------
Enter websites as http(s)://www.yourwebsite.com
'''


import urllib.request
import tkinter as tk


def test_connectivity():
  window = tk.Tk()
  window.geometry('600x400')
  head = tk.Label(window, text='Website Connectivity Checker',
                  font=('Calibri 15'))
  head.pack(pady=20)

  def check_url():
      web = (url.get())
      status_code = urllib.request.urlopen(web).getcode()
      website_is_up = status_code == 200

      if website_is_up:
          tk.Label(window, text='Website Available',
                   font=('Calibri 15')).place(x=260, y=200)
      else:
          tk.Label(window, text='Website Not Available',
                   font=('Calibri 15')).place(x=260, y=200)

  url = tk.StringVar()
  tk.Entry(window, textvariable=url).place(x=200, y=80, height=30, width=280)
  tk.Button(window, text='Check', command=check_url).place(x=285, y=150)
  window.mainloop()


if __name__ == '__main__':
  test_connectivity()