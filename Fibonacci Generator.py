# The Fibonacci numbers may be some of the most important numbers in our lives as
# they appear so often in nature.
# The Python code below generates the Fibonacci numbers up to a certain length using recursion
# (yes, more recursion!). To stop the computation times from getting out of hand,
# we’ve implemented memoization to cache values as we calculate them.
# You’ll notice that for this recursive algorithm, the base case is set to check whether the given
# Fibonacci sequence value is already stored in the cache. If so, it returns this
# (which is a constant time complexity operation), which saves a tremendous amount of computation time.
#
# Числа Фибоначчи могут быть одними из самых важных чисел в нашей жизни,
# поскольку они так часто встречаются в природе.
# Приведенный ниже код Python генерирует числа Фибоначчи до определенной длины с использованием рекурсии
# (да, еще больше рекурсии!). Чтобы время вычислений не выходило из-под контроля,
# мы внедрили запоминание значений кэша по мере их вычисления.
# Вы заметите, что для этого рекурсивного алгоритма базовый вариант настроен на проверку того,
# сохранено ли заданное значение последовательности Фибоначчи в кэше. Если это так,
# он возвращает this (что является операцией постоянной сложности по времени),
# что экономит огромное количество времени вычислений.

'''
Fibonacci Sequence
-------------------------------------------------------------
'''

fib_cache = {}


def fib_memo(input_val):
   if input_val in fib_cache:
       return fib_cache[input_val]

   if input_val == 0:
       val = 0
   elif input_val < 2:
       val = 1
   else:
       val = fib_memo(input_val - 1) + fib_memo(input_val - 2)

   fib_cache[input_val] = val
   return val


if __name__ == '__main__':
   print('======== Fibonacci Series ========')
   for i in range(1, 11):
       print(f'Fibonacci ({i}) : {fib_memo(i)}')