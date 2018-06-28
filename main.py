from chatterbot import ChatBot #import chatbot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Debot')
bot.set_trainer(ListTrainer)
for files in os.listdir('/home/farfar/PycharmProjects/dbot/data/english/'):
    data=open('/home/farfar/PycharmProjects/dbot/data/english/' +files, 'r').readlines()
    bot.train(data)
while True:
    # form =cgi.FieldStorage()
    # searchchat = form.getvalue("chat")
    message=input('you:')
    if message.strip !='Bye':
       reply=bot.get_response(message)
       print('ChatBot:',reply)
    if message.strip() =='Bye':
        print('ChatBot:Bye')
        break




