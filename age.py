import datetime

class age_calculator:

  birth_year = input('what year were you born, dear! \n')
  current_year = datetime.datetime.now().year
  try:
    int(birth_year)
    print (f'You age is : {current_year-int(birth_year)}')
  except ValueError:
    print('Enter a number dumbo!')