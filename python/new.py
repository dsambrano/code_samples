import time
timer_start = time.time()

for i in xrange(1, 100000):
    print "Hi!"
#End for

print "Finished!"

timer_end = time.time() - timer_start

print timer_end
