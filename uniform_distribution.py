#!/usr/bin/env python

import sys, os, math, time
import multiprocessing
cores = multiprocessing.cpu_count()
from threading import Thread
import threading

class pithread(Thread):
        work = {}
        divisions = 0
        isRunning = False
        
        def __init__(self, divisions):
                Thread.__init__(self)
                self._stop_event = threading.Event()
                
        def run(self):
                self.isRunning = True
                while True:
                        done = True
                        if len(self.work.keys()) < 1:
                                time.sleep(1)
                        for opp in self.work.keys():
                                if self.work[opp] == '':
                                        print "Processing %s" % opp
                                        done = False
                                        adj = math.cos(math.asin(opp))
                                        self.work[opp] = divisions - int(adj*divisions)
                        if done:
                                self.isRunning = False
                                return

# as "spacing" approaches zero, accuracy goes up (as does required time)
# based on sys.float_info.min, which on amd64/python 2.7.16 is ~2.22507 x 10^-308
# since the exponent is -308, we can adjust "spacing" to determine how many divisions we want
spacing = -300 
step = float(sys.float_info.min) / 10**spacing
divisions = int(1/(float(sys.float_info.min)/10**spacing))
samples = divisions**2

print "Current settings will give %s divisions from 0.0 to 1.0 for a sample size of %s" % (divisions, samples)
print "Starting %s threads to perform calculations..." % cores

miss = 0
i = step

# create threads
threads = {}
for j in range(0,cores):
        worker = pithread(divisions)
        threads[j] = worker

# distribute work
while i < 1.0:
        for j in range(0, cores):
                threads[j].work[i] = ''
                i = i + step

for j in range(0,cores):
        threads[j].start()
                
# work is distributed, now we need to collect the data
while len(threads) > 0:
        for j in threads.keys():
                if not threads[j].isRunning:
                        print sum(threads[j].work.values())
                        miss = miss + sum(threads[j].work.values())
                        del threads[j]
                
print "samples: %s misses: %s" % (samples, miss)

p = ((samples - miss) / float(samples))*4   # like monte carlo integration, but we're intentionally making a uniform sample space.
print "math.pi       =  %.20f" % math.pi
print "calculated pi =  %.20f" % p
print "Accuracy      = %.20f" % (100*(math.pi - abs(p - math.pi)) / math.pi)
