#!/usr/bin/env python

import animals

import sys        #gets arguments on the command line
#import argparse - more powerful

filename = sys.argv[1]
animal = sys.argv[2]

try:
    mean_count = animals.mooat(filename,animal)
except ZeroDivisionError:
    print "There were no", animal
    mean_count = 0

#print "the mean count of", animal, "is", mean_count
print "The mean count of %s is %6.2f" % (animal, mean_count)
