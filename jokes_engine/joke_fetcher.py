from jokeapi import Jokes


def get_joke(joke_category):

  print(joke_category)
  available_categories = ['Misc', 'Programming', 'Dark','Pun', 'Spooky', 'Christmas']


  if (joke_category not in available_categories):
    joke_category = ['Any']
    print(joke_category)

  j = Jokes()
  joke = j.get_joke(category=joke_category)

  print(joke)
  if joke["type"] == "single":
    response = joke["joke"]
  else:
    response = '{setup}\n{delivery}'.format(setup = joke["setup"], delivery = joke["delivery"])
  return response

