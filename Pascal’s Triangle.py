# This Python project prints out Pascal’s Triangle by utilizing conditional statements and loops.
# It also uses the standard library’s math module and factorial function to evaluate the
# ‘number of combinations’ equation used to generate the values in the triangle.
# Experiment with the seed number for the triangle to examine how the ‘combinations’ equation is
# used to generate successive values in the triangle.
#
# Этот проект на Python выводит треугольник Паскаля, используя условные операторы и циклы.
# Он также использует математический модуль стандартной библиотеки и факториальную функцию для оценки
# уравнения "количество комбинаций", используемого для генерации значений в треугольнике.
# Поэкспериментируйте с начальным номером треугольника, чтобы изучить,
# как уравнение "комбинаций" используется для генерации последовательных значений в треугольнике.

'''
Pascal's Triangle
-------------------------------------------------------------
Number of combinations via "n choose k" or nCk = n! / [k! * (n-k)!]
'''

from math import factorial


def pascal_triangle(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(end=' ')

        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=' ')

        print()


if __name__ == '__main__':
    pascal_triangle(5)