# This Python project uses a range of new libraries to convert an existing article into a playable mp3 file. You’ll need to install nltk (natural language toolkit), newspaper3k, and gtts (see pip install instructions).
# You’ll see that the program is simple, as we simply pass in a URL for an article to convert, then let the function we’ve defined handle the text-to-speech conversion with our newly installed modules.
# So, consider trying this out the next time you fancy turning an article into a playable podcast as it’s definitely one of the cool Python codes to copy!
#
# Этот проект на Python использует ряд новых библиотек для преобразования существующей статьи в воспроизводимый mp3-файл. Вам нужно будет установить nltk (natural language toolkit), newspaper3k и gtts (см. Инструкции по установке pip).
# Вы увидите, что программа проста, поскольку мы просто передаем URL-адрес статьи для преобразования, а затем позволяем функции, которую мы определили, обрабатывать преобразование текста в речь с помощью наших недавно установленных модулей.
# Итак, попробуйте это в следующий раз, когда вам захочется превратить статью в воспроизводимый подкаст, поскольку это определенно один из самых классных кодов Python для копирования!

'''
Text To Speech
-------------------------------------------------------------
pip install nltk newspaper3k gtts
'''


import nltk
from newspaper import Article
from gtts import gTTS


def text_to_speech(url):
   article = Article(url)
   article.download()
   article.parse()
   nltk.download('punkt')
   article.nlp()
   article_text = article.text
   language = 'en'
   my_obj = gTTS(text=article_text, lang=language, slow=False)
   my_obj.save("read_article.mp3")


if __name__ == '__main__':
   text_to_speech(
       url='https://hackr.io/blog/top-tech-companies-hiring-python-developers'
   )
