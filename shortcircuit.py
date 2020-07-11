import time as dt 

success = True
can_test = True 


time = 0

for i in range(10000000):
  start = dt.time()
  if success and can_test:
    stop = dt.time()
    time+= stop-start


print(f'"and" operation took: {time} seconds')


time = 0

for i in range(10000000):
  start = dt.time()
  if success or can_test:
    stop = dt.time()
    time += stop-start


print(f'"or" operation took: {time} seconds')
