#image = [
#  [0,0,0,1,0,0,0],
#  [0,0,1,1,1,0,0],
#  [0,1,1,1,1,1,0],
#  [1,1,1,1,1,1,1],
#  [0,0,0,1,0,0,0],
#  [0,0,0,1,0,0,0]
#]
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('players.jpg').convert('L')


image = np.array(img)
image = ~image  # invert B&W
#image[image > 100] = 1



print(image.shape)
plt.imshow(image,cmap='Greys')
plt.show()
input('do we run?')

for stacks in image:
  dots=[]
  for pixels in stacks:
    dots.append(" ") if pixels ==0 else dots.append("*")
  print(''.join(dots))

print('       ')
for stacks in image:
  for pixels in stacks:
    print(" ", end='') if pixels ==0 else print("*",end='')
  print('')