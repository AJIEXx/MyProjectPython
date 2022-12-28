# Mad Libs Generator
# This is one of the most fun beginner Python projects,
# not to mention it lets you practice how to use strings,
# variables, and concatenation.
# The Mad Libs Generator gathers and manipulates
# user input data as an adjective,
# a pronoun, and a verb. The program takes this data and arranges
# it to build a story.
#
# Генератор Mad Libs
# Это один из самых веселых проектов для начинающих Python,
# не говоря уже о том, что он позволяет вам практиковаться в использовании строк,
# переменных и конкатенации.
# Генератор Mad Libs собирает и обрабатывает введенные
# пользователем данные в виде прилагательного,
# местоимения и глагола.
# Программа берет эти данные и упорядочивает их для создания истории.

'''
Mad Libs Generator
-------------------------------------------------------------
'''

# Questions for the user to answer

noun = input('Choose a noun: ')

p_noun = input('Choose a plural noun: ')

noun2 = input('Choose a noun: ')

place = input('Name a place: ')

adjective = input('Choose an adjective (Describing word): ')

noun3 = input('Choose a noun: ')

# Print a story from the user input

print('------------------------------------------')

print('Be kind to your', noun, '- footed', p_noun)

print('For a duck may be somebody\'s', noun2, ',')

print('Be kind to your', p_noun, 'in', place)

print('Where the weather is always', adjective, '. \n')

print('You may think that is this the', noun3, ',')

print('Well it is.')

print('------------------------------------------')
