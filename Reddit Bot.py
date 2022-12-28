# This Python project creates an automated reddit bot with some new modules,
# namely praw and enchant (see the pip install commands).
# This is a fairly simple concept as the program checks every comment in a selected subreddit,
# and then replies to any comments that contain a predefined ‘trigger phrase’. To do this,
# we use the praw module to interact with reddit, and enchant to generate similar words to the comment,
# allowing us to make an appropriate reply.
# This idea is really useful if you’re looking for Python projects to learn how to answer questions
# in your own subreddit. You’d just need to expand this code to include automated responses for
# predefined questions (you’ve probably already noticed this being used by others on reddit!).
# Important note: You’ll need to check out these instructions to get hold of a client_id,
# client_secret, username, password, and user_agent.
# You’ll need this information to make comments to reddits via the API interface.
#
# Этот проект на Python создает автоматизированного бота reddit с некоторыми новыми модулями,
# а именно praw и enchant (см. Команды установки pip).
# Это довольно простая концепция, поскольку программа проверяет каждый комментарий в выбранном subreddit,
# а затем отвечает на любые комментарии, содержащие предопределенную ‘триггерную фразу’.
# Для этого мы используем модуль praw для взаимодействия с reddit и enchant для генерации слов,
# похожих на комментарий, что позволяет нам сделать соответствующий ответ.
# Эта идея действительно полезна, если вы ищете проекты на Python, чтобы научиться отвечать на вопросы
# в своем собственном субреддите. Вам просто нужно расширить этот код, чтобы включить автоматические ответы
# на предопределенные вопросы (вы, наверное, уже заметили, что это используется другими пользователями reddit!).
# Важное примечание: вам нужно будет ознакомиться с этими инструкциями, чтобы получить client_id,
# client_secret, имя пользователя, пароль и user_agent. Вам понадобится эта информация,
# чтобы оставлять комментарии в reddits через интерфейс API.

'''
Reddit Reply Bot
-------------------------------------------------------------
pip install praw pyenchant
'''


import praw
import enchant


def reddit_bot(sub, trigger_phrase):
   reddit = praw.Reddit(
       client_id='your_client_id',
       client_secret='your_client_secret',
       username='your_username',
       password='your_pw',
       user_agent='your_user_agent'
   )

   subreddit = reddit.subreddit(sub)
   dict_suggest = enchant.Dict('en_US')

   for comment in subreddit.stream.comments():
       if trigger_phrase in comment.body.lower():
           word = comment.body.replace(trigger_phrase, '')
           reply_text = ''
           similar_words = dict_suggest.suggest(word)
           for similar in similar_words:
               reply_text += (similar + ' ')
           comment.reply(reply_text)


if __name__ == '__main__':
   reddit_bot(sub='Python', trigger_phrase='useful bot')