# Tic-Tac-Toe is a classic two-player game that involves a nine-square grid.
# Each player alternately marks their space with an O or an X,
# and whichever player manages to mark three Os or Xs diagonally, horizontally,
# or vertically wins. Each player must also block their opponent while attempting to make their chain.
# This is one of the most fun Python projects that is also unique for beginners
# as it uses object-oriented programming to create a new class called TicTacToe.
# We use this to represent the game's features via the class attributes and methods.
# Carefully study these methods to see how we can use object-oriented
# programming to neatly package the various behaviors needed to simulate this game.
# Some new aspects of this Python project idea for beginners include nested loops to
# check the grid's columns, rows, and diagonals for a winning state,
# along with the Python set data type, which is used to contain unique values.
# This program also uses the Python random module to select a random player to start the game,
# but this is more familiar to you now.
#
# Крестики-нолики - классическая игра для двух игроков,
# в которой используется сетка из девяти квадратов.
# Каждый игрок поочередно помечает свое место буквой O или X,
# и тот игрок, которому удастся отметить три буквы Os или X по диагонали,
# горизонтали или вертикали, выигрывает. Каждый игрок также должен блокировать своего противника,
# пытаясь создать свою цепочку.
# Это один из самых веселых проектов на Python, который также уникален для начинающих,
# поскольку он использует объектно-ориентированное программирование для создания нового класса
# под названием TicTacToe. Мы используем это для представления возможностей игры с помощью атрибутов
# и методов класса.
# Внимательно изучите эти методы, чтобы увидеть,
# как мы можем использовать объектно-ориентированное программирование для аккуратной упаковки
# различных поведений, необходимых для имитации этой игры.
# Некоторые новые аспекты этой идеи проекта Python для начинающих включают вложенные циклы
# для проверки столбцов, строк и диагоналей сетки на предмет выигрышного состояния,
# а также тип данных Python set, который используется для хранения уникальных значений.
# Эта программа также использует модуль Python random для выбора случайного игрока для запуска игры,
# но теперь это вам более знакомо.

'''
Tic Tac Toe
-------------------------------------------------------------
'''

import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        n = len(self.board)
        board_values = set()

        # check rows
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check cols
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[j][i])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check diagonals
        for i in range(n):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()

        board_values.add(self.board[0][2])
        board_values.add(self.board[1][1])
        board_values.add(self.board[2][0])
        if board_values == {player}:
            return True
        else:
            return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')

                row, col = list(
                    map(int, input(
                        'Enter row & column numbers to fix spot: ').split()))
                print()

                if col is None:
                    raise ValueError(
                        'not enough values to unpack (expected 2, got 1)')

                self.fix_spot(row - 1, col - 1, player)

                game_over = self.has_player_won(player)
                if game_over:
                    print(f'Player {player} wins the game!')
                    continue

                game_over = self.is_board_filled()
                if game_over:
                    print('Match Draw!')
                    continue

                player = self.swap_player_turn(player)

            except ValueError as err:
                print(err)

        print()
        self.show_board()


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
