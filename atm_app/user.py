class User:
  def __init__(self, account, pin, balance):
    self.account = account
    self.pin = pin
    self.balance = balance

user_dictionary = {}

# if the user exists in the dictionary, ensure the pin matches then return it
# if the pins do not match, then return `None`
# if the user isn't in the dictionary, create & return a new user with this info
def get_user(account, pin):
  if account in user_dictionary:
    user = user_dictionary[account]
    if (pin == user.pin):
      return user_dictionary[account]
    else:
      return None
  else:
    new_user = User(account, pin, 100)
    user_dictionary[account] = new_user
    return new_user

