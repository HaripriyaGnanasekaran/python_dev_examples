import pandas as pd
dictionary = {
  'username':['Ram', 'Daphne', 'Ashan', 'Momota'],
  'rank':[4,2,3,1]
}

# Just trying out curious stuff!
df=pd.DataFrame.from_dict(dictionary)
print(df)

'''
keys should be immutable in dictionary. (TypeError occurs unless)
key has to unique. (overwritten otherwise)
'''

# some dictionary methods
print(dictionary.keys())
print(dictionary.get('username'))
print(dictionary.values())
