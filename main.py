import os
import telebot
from jokes_engine.joke_fetcher import get_joke

API_KEY = os.getenv('BOT_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
  resposne = "Hey! Hello {fName}.\nI can make your Day by telling you some jokes\nif interested type \"joke <joke_category>\".\nAvailable Joke categories are:\nMisc, Programming, Dark, Pun, Spooky and Christmas Or just type \"joke\" for a random hilarious Joke.\nExample: \n1] joke Pun\n2] joke\nAt Any Point of time you need help just type \"\help\" ".format(fName = message.from_user.first_name)
  bot.send_message(message.chat.id, resposne)

# def request_validator(message):
#   request = message.text.split()
#   print(request)
#   if request[0].lower() == 'joke':
#     return True
#   else:
#     return False

def get_required_response(request):
  response = 'Wrong Input, naughty boi'
  request = request.split()
  if request[0].lower() == "joke":
    joke_category = request[1:1] if len(request) >= 2 else ['Any'] 
    print(joke_category)
    response = get_joke(joke_category)
  return response


@bot.message_handler()
def handle_request(message):
  response = get_required_response(message.text)
  bot.send_message(message.chat.id, response)

bot.polling()