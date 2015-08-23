import time
a = range(500)

sum(a)

for i in range(1000000): #just to create a time interval, seems this disturb cpu cache?
    pass


st = time.time()
sum(a)
print (time.time() - st)*1e6
