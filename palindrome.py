wordlist = [
  'madam',
  'madame'
]


for word in wordlist:
  even = True 
  count = 0
  for letter in set(word):
    even = (word.count(letter))%2
    if even==True:
      count += 1


  print(f'{word}: Cannot be a palindrome') if count >1 else print(f'{word}: Can be made into palindrome')
