
# running the program-- python star_tree.py n  (n being the size of the tree)
# pattern divided as even line or odd line
# main calls tree with arguement n
#

import math
import sys;

# draw middle pattern for even line
def even_pattern(i):
    stars = i/2;
    for l in xrange(1,stars+1):
        print('*'),
    for m in xrange(1,4):
        print('_'),
        for x in xrange(1,stars+1):
            print('*' ),

# central function that loops over n values
# calling even() or odd function as required
# even
def tree(n):
    global es;
    global os;
    #print "making tree of size ",n;
    if(n%2==0):
        k=n/2
        es=k-1   # even space
        os = n+1  # odd space
    else:
        k=(n-1)/2
        es = k-1
        os = n

    for i in xrange(1,n+1):
        if(i%2 == 0):

            even(i);
        else:

            odd(i);
        print '\n';

#module for odd line
def odd(i):
    global os;

    for d in xrange(1,os+1):
        print('_'),
    for x in xrange(1,i+1):
        print('*'),
    for d in xrange(1,os+1):
        print('_'),
    os=os-1;

# module for even line
def even(i):
    global es;
    #dashes = math.pow(2,es)
    dashes = 2*es;
    if(es==0):
        dashes=0;
    for x in xrange(1,int(dashes)+1) :
        print '_',
    even_pattern(i);
    for x in xrange(1,int(dashes)+1):
        print '_',
    es=es-1
    
#main function calls tree with arguement
if __name__ == '__main__':

    n = 6;
    n= int(sys.argv[1]);
    tree(n);
