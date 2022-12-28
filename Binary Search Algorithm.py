# It’s a rite of passage for all aspiring coders to tackle Binary Search in one of their
# Python programming projects at some point!
# This Python project for binary search takes in a sorted list (array),
# then continually compares a search value with the middle of the array.
# Depending on whether the search value is less than or greater than the middle value,
# the list is split (divide and conquer strategy) to reduce the search space,
# which hones in on the given search value. This continual division results in logarithmic time complexity.
# If you look at the code below, you’ll see that we’ve implemented two solutions:
# conditional loops and recursion. Both approaches are elegant, so feel free to experiment with each.
# If you’re new to recursion, this is a great introduction as it demonstrates how we
# ‘reduce’ the size of the problem with each recursive call, namely by splitting the list to one side of
# the current middle element.
# We’ve also defined the recursive base case as the point when the middle element is equal
# to the search element. In this case, the recursion will stop and return the
# True value up through the call stack.
#
# Это обряд посвящения для всех начинающих программистов - в какой-то момент заняться бинарным поиском
# в одном из своих проектов по программированию на Python!
# Этот проект Python для двоичного поиска принимает отсортированный список (массив),
# затем постоянно сравнивает значение поиска с серединой массива.
# В зависимости от того, является ли значение поиска меньше или больше среднего значения,
# список разделяется (стратегия "разделяй и властвуй"), чтобы уменьшить пространство поиска,
# которое зависит от заданного значения поиска.
# Это непрерывное разделение приводит к логарифмической временной сложности.
# Если вы посмотрите на приведенный ниже код, вы увидите, что мы реализовали два решения:
# условные циклы и рекурсию. Оба подхода элегантны, поэтому не стесняйтесь экспериментировать с каждым.
# Если вы новичок в рекурсии, это отличное введение, поскольку оно демонстрирует,
# как мы "уменьшаем" размер проблемы с каждым рекурсивным вызовом,
# а именно путем разделения списка на одну сторону от текущего среднего элемента.
# Мы также определили рекурсивный базовый вариант как точку, когда средний элемент равен элементу поиска.
# В этом случае рекурсия остановится и вернет истинное значение через стек вызовов.

'''
Binary Search
-------------------------------------------------------------
'''


def binary_search(a_list, an_item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item:
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return False


def binary_search_rec(a_list, first, last, an_item):
    if len(a_list) == 0:
        return False
    else:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item:
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
                return binary_search_rec(a_list, first, last, an_item)
            else:
                first = mid_point + 1
                return binary_search_rec(a_list, first, last, an_item)


if __name__ == '__main__':
    a_list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]

    print('Binary Search:', binary_search(a_list, 4))
    print('Binary Search Recursive:',
          binary_search_rec(a_list, 0, len(a_list) - 1, 4))
