# This Python project uses the langdetect module (see pip install instructions) to help us identify the language that has been entered. This can be really useful if you’re unsure which language you’re dealing with.
# This is another example where we’ve used tkinter to create a simple GUI involving labels, buttons, and an entry field. We can then collect text from the entry field and process this with the langdetect to determine which language was entered. Finally, we print this result to the GUI to let the user know the result.
# Note that the results returned by langdetect are abbreviated language codes. For example, if we enter English text, we will see ‘en’ as the return value.
#
# Этот проект на Python использует модуль langdetect (см. Инструкции по установке pip), чтобы помочь нам определить введенный язык. Это может быть действительно полезно, если вы не уверены, с каким языком имеете дело.
# Это еще один пример, когда мы использовали tkinter для создания простого графического интерфейса, включающего метки, кнопки и поле ввода. Затем мы можем собрать текст из поля ввода и обработать его с помощью langdetect, чтобы определить, какой язык был введен. Наконец, мы выводим этот результат в графический интерфейс, чтобы пользователь знал результат.
# Обратите внимание, что результаты, возвращаемые langdetect, являются сокращенными языковыми кодами. Например, если мы введем текст на английском языке, мы увидим ‘en’ в качестве возвращаемого значения.

'''
Language Detector
-------------------------------------------------------------
pip install langdetect
'''


from langdetect import detect
import tkinter as tk


def detect_lang():
   window = tk.Tk()
   window.geometry('600x400')
   head = tk.Label(window, text='Language Detector', font=('Calibri 15'))
   head.pack(pady=20)

   def check_language():
       new_text = text.get()
       lang = detect(str(new_text))
       tk.Label(window, text=lang, font=('Calibri 15')).place(x=260, y=200)

   text = tk.StringVar()
   tk.Entry(window, textvariable=text).place(
       x=200, y=80, height=30, width=280)
   tk.Button(window, text='Check Language',
             command=check_language).place(x=285, y=150)
   window.mainloop()


if __name__ == '__main__':
   detect_lang()