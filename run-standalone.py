from timeit import default_timer as timer # allow Windows friends to play
a = range(500)

sum(a)

for i in range(1000000): #just to create a time interval, seems this disturb cpu cache?
    pass


st = timer()
sum(a)
print("%.2f us" % ((timer() - st)*1e6,))
