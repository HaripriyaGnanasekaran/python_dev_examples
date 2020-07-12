binary_tree = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for stacks in binary_tree:
  leaves=[]
  for bits in stacks:
    leaves.append(" ") if bits ==0 else leaves.append("*")
  print(''.join(leaves))
