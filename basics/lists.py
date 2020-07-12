'''
Two dimensional lists are matrix, but still belong to class lists
'''
lists = [[1,2,4],[3,5]]
print(lists.pop())
print(lists)


# let's do some examples of list methods.
# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.remove('Banana')
print(f'Bananas are removed from the basket: {basket}')

# 2. Remove "Blueberries" from the list.
basket.remove('Blueberries')
print(f'Blueberries are removed from the basekt: {basket}')

# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
print(f'Kiwi is added from the basekt: {basket}')
# 4. Add "Apples" at the beginning of the list
basket.insert(0,'Apples')
print(f'Apples are added from the basekt: {basket}')
# 5. Count how many apples in the basket
apples = basket.count('Apples')
print(f'There are {apples} apples in the basket')
basket.sort() 
basket.append(23)
basket.append(1)
print(basket)
# 6. empty the basket
basket.clear()
print(basket)

one, *rest, end = list(range(101))
print(rest)