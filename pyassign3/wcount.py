#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhanzhaohuang"
__pkuid__  = "1700011730"
__email__  = "1700011730@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    for i in lines:
        if i>='A' and i<="Z":
            continue
        elif i>="a" and i<='z':
            continue
        elif i==' ':
            continue
        else:
            lines=lines.replace(i,' ')
    n1=lines.split(' ')
    for i in range(n1.count('')):
        n1.remove('')
    n2=set()
    for i in n1:
        n2.add((i,n1.count(i)))
    
    n3=[]
    for (i,o) in n2:
        n3.append(o)
    for i in range(topn):
        x=max(n3)
        n3.remove(x)
    y=max(n3)
    n4={}
    for (i,o) in n2:
        if o>y:
            n4[o]=i
    n5=list((n4.keys()))
    n5.sort(reverse=True)
    for i in n5:
        print (n4[i], '\t', i)
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)