import time
a = range(500)

for i in range(100000):
    st = time.time()
    sum(a)
    print (time.time() - st)*1e6
