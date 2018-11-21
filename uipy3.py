#!/usr/bin/env python3
from IPython import embed

def uipy3_load_file(filename):
    f = open(filename, "r")
    t = []
    
    for l in f:
        if l != "\n" or l != "" :
            t.append(l)
    return t

things = uipy3_load_file("home.uipy3")

for thing in things:
    
    exec(thing)

print ("uipy -> home.uipy3")
embed()
