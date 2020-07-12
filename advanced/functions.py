def exist():
  '''
  Checks if a file exist.

  Every file has a exist function that states it exists and welcomes!
  Use try catch when attemption to check to avoid stopping execution.
  '''
  print('Welcome to the functions world! It exists')
  return None

def even(x):
  '''
  Checks if a number is even.

  param: x
  method: Determines the moduls when x with respect to 2 
          and outputs True if 0. Othewise x is odd, returns False.
  '''
  return x%2 ==0

def highest_even(x):
  '''
  Returns the highest even in the list x.

  No checks implemented.
  TODO: 
    Check if received parameter is an iterable
    Check if the iterable can be made integer
    If contains float always return floats are never odd or even etc.
  '''
  try:
    num=0
    for item in x:
      integer = int(item)
      if even(integer) and integer > num:
        num=integer
    return num
  except:
    return ('What have you done! List items can not be made into integers') 

  