image = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for stacks in image:
  dots=[]
  for pixels in stacks:
    dots.append(" ") if pixels ==0 else dots.append("*")
  print(''.join(dots))
