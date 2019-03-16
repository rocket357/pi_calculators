#!/usr/bin/env python

import sys, os, math

# as "spacing" approaches zero, accuracy goes up (as does required time)
# based on sys.float_info.min, which on amd64/python 2.7.16 is ~2.22507 x 10^-308
# since the exponent is -308, we can adjust "spacing" to determine how many divisions we want
spacing = -300 
step = float(sys.float_info.min) / 10**spacing
divisions = int(1/(float(sys.float_info.min)/10**spacing))
samples = divisions**2

print "Current settings will give %s divisions from 0.0 to 1.0 for a sample size of %s" % (divisions, samples)

miss = 0

i = step
while i < 1.0:
        # we have hyp = 1, opp = i
        # thus asin(i) is the radians
        # and cos(radians) is the adj (since hyp = 1)
        adj = math.cos(math.asin(i))
        
        # since we know this, we can programatically determine the number of misses
        miss = miss + divisions - math.ceil(adj*divisions)
        
        # I need to see output sometimes.
        #print "opp: %s, adj: %s, misses: %s" % (i, adj, miss)
        i = i + step

print "samples: %s misses: %s" % (samples, miss)

p = ((samples - miss) / float(samples))*4   # like monte carlo integration, but we're intentionally making a uniform sample space.
print "math.pi       =  %.20f" % math.pi
print "calculated pi =  %.20f" % p
print "Accuracy      = %.20f" % (100*(math.pi - abs(p - math.pi)) / math.pi)
