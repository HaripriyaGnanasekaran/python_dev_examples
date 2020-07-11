wordlist = [
  'Never odd or even',
  'dogma I am God',
  "Madam Im Adam" ,
  "Able was I ere I saw Elba",
  'I am not a palindrome'
]


for rawword in wordlist:
  count = 0
  word = rawword.replace(" ","")
  word = word.lower()
  for letter in set(word):
    even = (word.count(letter))%2
    if even==True:
      count += 1


  print(f'{rawword}: Cannot be a palindrome') if count >1 else print(f'{rawword}: Can be made into palindrome')
