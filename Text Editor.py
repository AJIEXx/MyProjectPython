# Building on our last tkinter example, this fun Python project creates a GUI to simulate our very own text editor. This example also uses standard GUI components, including labels, buttons, and entry fields.
# However, we’ve also added the ability to open and save files like a real text editor. If you’re new to file handling, this Python project is a great way to understand how to read-in and save files.
# Experiment with the code below to solidify your understanding, and see if you can expand on this code to create other features you’re used to using with a text editor, like a ‘find word’ function.
#
# Основываясь на нашем последнем примере с tkinter, этот забавный проект на Python создает графический интерфейс для имитации нашего собственного текстового редактора. В этом примере также используются стандартные компоненты графического интерфейса, включая метки, кнопки и поля ввода.
# Тем не менее, мы также добавили возможность открывать и сохранять файлы, как в настоящем текстовом редакторе. Если вы новичок в обработке файлов, этот проект на Python - отличный способ понять, как считывать и сохранять файлы.
# Поэкспериментируйте с приведенным ниже кодом, чтобы закрепить свое понимание, и посмотрите, сможете ли вы расширить этот код, чтобы создать другие функции, которые вы привыкли использовать в текстовом редакторе, например, функцию ‘найти слово’.

'''
Text Editor
-------------------------------------------------------------
'''


import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def text_editor():
   def open_file():
       filepath = askopenfilename(
           filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
       )

       if not filepath:
           return

       txt_edit.delete(1.0, tk.END)
       with open(filepath, 'r') as input_file:
           text = input_file.read()
           txt_edit.insert(tk.END, text)
       window.title(f'TextEditor - {filepath}')

   def save_file():
       filepath = asksaveasfilename(
           defaultextension='txt',
           filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')],
       )

       if not filepath:
           return

       with open(filepath, 'w') as output_file:
           text = txt_edit.get(1.0, tk.END)
           output_file.write(text)
       window.title(f'Text Editor - {filepath}')

   window = tk.Tk()
   window.title('Text Editor')
   window.rowconfigure(0, minsize=800, weight=1)
   window.columnconfigure(1, minsize=800, weight=1)

   txt_edit = tk.Text(window)
   fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
   btn_open = tk.Button(fr_buttons, text='Open', command=open_file)
   btn_save = tk.Button(fr_buttons, text='Save As...', command=save_file)

   btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
   btn_save.grid(row=1, column=0, sticky='ew', padx=5)

   fr_buttons.grid(row=0, column=0, sticky='ns')
   txt_edit.grid(row=0, column=1, sticky='nsew')

   window.mainloop()


if __name__ == '__main__':
  text_editor()