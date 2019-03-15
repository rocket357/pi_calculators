#!/usr/bin/env python

import sys, os, math

spacing = -300  # as this approaches zero, accuracy goes up (as does required time)
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
        miss = miss  - 1 + divisions - int(adj*divisions)
        
        # I need to see output sometimes.
        #print "opp: %s, adj: %s, misses: %s" % (i, adj, miss)
        i = i + step

print "samples: %s misses: %s" % (samples, miss)

p = ((samples - miss) / float(samples))*4   # like monte carlo integration, but we're intentionally making a uniform sample space.
print "math.pi       = %s" % math.pi
print "calculated pi = %s" % p
print "Accuracy      = %.5f" % (100*(math.pi - abs(p - math.pi)) / math.pi)