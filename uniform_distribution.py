#!/usr/bin/env python

import sys, os, math

# 10**precision "base" divisions, or 100 million * mantissa for a default of 8
precision = 8  

# as "spacing" approaches zero, accuracy goes up (as does required time)
spacing = int(round(math.log10(sys.float_info.min))) + precision  # -308 + 8 = -300, for amd64/Python 2.7.16

# step is the interval between samples, based on the precision and spacing above
step = float(sys.float_info.min) / 10**spacing
divisions = int(1/step)

# total samples across x and y for quadrant I of the circle (r = 1)
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
