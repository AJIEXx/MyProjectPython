# This is a really fun and interesting project as we’ve used the Python turtle module to emulate the classic arcade game Pong!
# We’ve used various methods from the turtle module to create our game components and detect ball collisions with the player paddles. We’ve also defined a range of keybindings to set the user controls for the left and right player paddles. Feel free to experiment with the game’s settings to better understand how each setting works and affects the overall game.
# Outside of these newly introduced turtle graphics functions, we’ve used string formatting to output the current scoreboard and user-defined functions to keep our code tidy. These are concepts you should be familiar with at this stage.
#
# Это действительно веселый и интересный проект, поскольку мы использовали модуль Python turtle для эмуляции классической аркадной игры Pong!
# Мы использовали различные методы из модуля turtle для создания наших игровых компонентов и обнаружения столкновений мяча с лопастями игрока. Мы также определили диапазон привязок клавиш для настройки пользовательских элементов управления для левой и правой клавиш проигрывателя. Не стесняйтесь экспериментировать с настройками игры, чтобы лучше понять, как работает каждая настройка и влияет на игру в целом.
# Помимо этих недавно представленных графических функций turtle, мы использовали форматирование строк для вывода текущего табло и пользовательских функций, чтобы поддерживать порядок в нашем коде. Это концепции, с которыми вы должны быть знакомы на данном этапе.

'''
Pong Arcade Game
-------------------------------------------------------------
'''


import turtle


def update_score(l_score, r_score, player, score_board):
   if player == 'l':
       l_score += 1
   else:
       r_score += 1

   score_board.clear()
   score_board.write('Left Player: {} -- Right Player: {}'.format(
       l_score, r_score), align='center',
       font=('Arial', 24, 'normal'))
   return l_score, r_score, score_board


def setup_game():
   screen = turtle.Screen()
   screen.title('Pong Arcade Game')
   screen.bgcolor('white')
   screen.setup(width=1000, height=600)

   l_paddle = turtle.Turtle()
   l_paddle.speed(0)
   l_paddle.shape('square')
   l_paddle.color('red')
   l_paddle.shapesize(stretch_wid=6, stretch_len=2)
   l_paddle.penup()
   l_paddle.goto(-400, 0)

   r_paddle = turtle.Turtle()
   r_paddle.speed(0)
   r_paddle.shape('square')
   r_paddle.color('black')
   r_paddle.shapesize(stretch_wid=6, stretch_len=2)
   r_paddle.penup()
   r_paddle.goto(400, 0)

   ball = turtle.Turtle()
   ball.speed(40)
   ball.shape('circle')
   ball.color('blue')
   ball.penup()
   ball.goto(0, 0)
   ball.dx = 5
   ball.dy = -5

   score_board = turtle.Turtle()
   score_board.speed(0)
   score_board.color('blue')
   score_board.penup()
   score_board.hideturtle()
   score_board.goto(0, 260)
   score_board.write('Left Player: 0 -- Right Player: 0',
                     align='center', font=('Arial', 24, 'normal'))

   return screen, ball, l_paddle, r_paddle, score_board


def pong_game():
   game_components = setup_game()
   screen = game_components[0]
   ball = game_components[1]
   l_paddle = game_components[2]
   r_paddle = game_components[3]
   score_board = game_components[4]
   l_score = 0
   r_score = 0

   def l_paddle_up():
       l_paddle.sety(l_paddle.ycor() + 20)

   def l_paddle_down():
       l_paddle.sety(l_paddle.ycor() - 20)

   def r_paddle_up():
       r_paddle.sety(r_paddle.ycor() + 20)

   def r_paddle_down():
       r_paddle.sety(r_paddle.ycor() - 20)

   screen.listen()
   screen.onkeypress(l_paddle_up, 'e')
   screen.onkeypress(l_paddle_down, 'x')
   screen.onkeypress(r_paddle_up, 'Up')
   screen.onkeypress(r_paddle_down, 'Down')

   while True:
       screen.update()
       ball.setx(ball.xcor()+ball.dx)
       ball.sety(ball.ycor()+ball.dy)

       if ball.ycor() > 280:
           ball.sety(280)
           ball.dy *= -1

       if ball.ycor() < -280:
           ball.sety(-280)
           ball.dy *= -1

       if ball.xcor() > 500:
           ball.goto(0, 0)
           ball.dy *= -1
           l_score, r_score, score_board = update_score(
               l_score, r_score, 'l', score_board)
           continue

       elif ball.xcor() < -500:
           ball.goto(0, 0)
           ball.dy *= -1
           l_score, r_score, score_board = update_score(
               l_score, r_score, 'r', score_board)
           continue

       if ((ball.xcor() > 360) and
           (ball.xcor() < 370) and
           (ball.ycor() < r_paddle.ycor()+40) and
               (ball.ycor() > r_paddle.ycor()-40)):
           ball.setx(360)
           ball.dx *= -1

       if ((ball.xcor() < -360) and
               (ball.xcor() > -370) and
               (ball.ycor() < l_paddle.ycor()+40) and
               (ball.ycor() > l_paddle.ycor()-40)):
           ball.setx(-360)
           ball.dx *= -1


if __name__ == '__main__':
   pong_game()