from jokeapi import Jokes


def get_joke(joke_category):

  available_categories = ['misc', 'programming', 'dark','pun', 'spooky', 'christmas']


  if (joke_category[0].lower() not in available_categories):
    joke_category = ['Any']

  j = Jokes()
  joke = j.get_joke(category=joke_category)

  if joke["type"] == "single":
    response = joke["joke"]
  else:
    response = '{setup}\n{delivery}'.format(setup = joke["setup"], delivery = joke["delivery"])
  return response

