#!/usr/bin/env python3
import sys
from IPython import embed


def uipy3_load_file(filename):
    f = open(filename, "r+")
    t = []
    
    for l in f:
        if l != "\n" or l != "" :
            t.append(l)
    return t

if __name__ == "__main__":
    uipy3_filename = ".default.uipy3"
    
    if len(sys.argv) == 2 :
        uipy3_filename = sys.argv[1]
    
    things = uipy3_load_file(uipy3_filename)
    
    for thing in things:
        
        exec(thing)
    
    print ("uipy -> " + uipy3_filename)
    
    embed()
