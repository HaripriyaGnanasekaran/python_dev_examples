
selfish = 'ramanathaN varadharajaN 34 @##$'
print(selfish.upper())
print(selfish.lower())
print(selfish.replace('#','@', 1))

word = 'madame'
print(word.find(word[::-1]))
p = bool(word.find(word[::-1]) +1 )
print(p) #True