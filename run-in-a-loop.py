from timeit import default_timer as timer
a = range(500)

times = []
for i in range(100000):
    st = timer()
    sum(a)
    times.append(timer() - st)
print("min=%.2f us, max=%.2f us" % (min(times)*1e6, max(times)*1e6))
