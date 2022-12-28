# This Python project creates a new class to implement a Queue.
# This is a common data structure in computer science when you need to handle First-In-First-Out
# (FIFO) scenarios, such as message queues, CPU tasks, etc.
# The code is straightforward and offers some more practice with object-oriented programming.
# Test out the queue to get your head around how it works, and then you’ll be ready to
# use this data structure in your other projects.
#
# Этот проект на Python создает новый класс для реализации очереди.
# Это обычная структура данных в информатике, когда вам нужно обрабатывать сценарии
# "Первый вход-первый выход" (FIFO), такие как очереди сообщений, задачи процессора и т. Д.
# Код прост и предлагает больше практики в объектно-ориентированном программировании.
# Протестируйте очередь, чтобы понять, как она работает, и тогда вы будете готовы использовать эту структуру
# данных в других своих проектах.

'''
Queue Data Structure
-------------------------------------------------------------
'''


class Queue:

   def __init__(self):
       self.items = []

   def __repr__(self):
       return f'Queue object: data={self.items}'

   def is_empty(self):
       return not self.items

   def enqueue(self, item):
       self.items.append(item)

   def dequeue(self):
       return self.items.pop(0)

   def size(self):
       return len(self.items)

   def peek(self):
       return self.items[0]


if __name__ == '__main__':
   q = Queue()
   print(q.is_empty())
   q.enqueue('First')
   q.enqueue('Second')
   print(q)
   print(q.dequeue())
   print(q)
   print(q.size())
   print(q.peek())