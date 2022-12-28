# As one of the more advanced Python projects, this program uses object-oriented programming to simulate a library management system.
# In this example, we create a Library and Student class, which we can use to create our library system and its users. We’ve then implemented a simple user interface that asks the user to select from a range of standard library actions, like borrowing or returning books.
# This is a simple yet powerful example of how you can build out real-world systems via Python and object-oriented programming. Feel free to expand the classes to include other useful features, like unique book IDs, multiple copies of the same book, return dates, fees for returning books late, or any other features you think a library should have!
#
# Как один из наиболее продвинутых проектов на Python, эта программа использует объектно-ориентированное программирование для моделирования системы управления библиотеками.
# В этом примере мы создаем библиотеку и класс Student, которые мы можем использовать для создания нашей библиотечной системы и ее пользователей. Затем мы внедрили простой пользовательский интерфейс, который предлагает пользователю выбирать из ряда стандартных библиотечных действий, таких как заимствование или возврат книг.
# Это простой, но мощный пример того, как вы можете создавать реальные системы с помощью Python и объектно-ориентированного программирования. Не стесняйтесь расширять классы, включив в них другие полезные функции, такие как уникальные идентификаторы книг, несколько копий одной и той же книги, даты возврата, плата за поздний возврат книг или любые другие функции, которые, по вашему мнению, должны быть в библиотеке!

'''
Library
-------------------------------------------------------------
'''


class Library:

   def __init__(self, books):
       self.books = books

   def show_avail_books(self):
       print('Our Library Can Offer You The Following Books:')
       print('================================================')
       for book, borrower in self.books.items():
           if borrower == 'Free':
               print(book)

   def lend_book(self, requested_book, name):
       if self.books[requested_book] == 'Free':
           print(
               f'{requested_book} has been marked'
               f' as \'Borrowed\' by: {name}')
           self.books[requested_book] = name
           return True
       else:
           print(
               f'Sorry, the {requested_book} is currently'
               f' on loan to: {self.books[requested_book]}')
           return False

   def return_book(self, returned_book):
       self.books[returned_book] = 'Free'
       print(f'Thanks for returning {returned_book}')


class Student:
   def __init__(self, name, library):
       self.name = name
       self.books = []
       self.library = library

   def view_borrowed(self):
       if not self.books:
           print('You haven\'t borrowed any books')
       else:
           for book in self.books:
               print(book)

   def request_book(self):
       book = input(
           'Enter the name of the book you\'d like to borrow >> ')
       if self.library.lend_book(book, self.name):
           self.books.append(book)

   def return_book(self):
       book = input(
           'Enter the name of the book you\'d like to return >> ')
       if book in self.books:
           self.library.return_book(book)
       else:
           print('You haven\'t borrowed that book, try another...')


def create_lib():
   books = {
       'The Last Battle': 'Free',
       'The Hunger Games': 'Free',
       'Cracking the Coding Interview': 'Free'
   }
   library = Library(books)
   student_example = Student('Your Name', library)

   while True:
       print('''
           ==========LIBRARY MENU===========
           1. Display Available Books
           2. Borrow a Book
           3. Return a Book
           4. View Your Books
           5. Exit'''
             )

       choice = int(input('Enter Choice: '))
       if choice == 1:
           print()
           library.show_avail_books()
       elif choice == 2:
           print()
           student_example.request_book()
       elif choice == 3:
           print()
           student_example.return_book()
       elif choice == 4:
           print()
           student_example.view_borrowed()
       elif choice == 5:
           print('Goodbye')
           exit()


if __name__ == '__main__':
   create_lib()