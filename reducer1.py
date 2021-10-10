#!/usr/bin/env python 
"""A more advanced Reducer, using Python iterators and generators.""" 
 
from itertools import groupby 
from operator import itemgetter 
import sys 
 
def read_mapper_output(file, separator='\t'): 
    for line in file: 
        yield line.rstrip().split(separator, 1) 
def main(separator='\t'): 
    # input comes from STDIN (standard input) 
    data = read_mapper_output(sys.stdin, separator=separator) 
    # groupby groups multiple word-count pairs by word, 
    # and creates an iterator that returns consecutive keys and their group: 
    #   current_word - string containing a word (the key) 
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
#my code starts
    most = []
    most_count = 0
    least = []
    least_count = 10000
#my code ends 
    for current_word, group in groupby(data, itemgetter(0)): 
        try: 
            total_count = sum(int(count) for current_word, count in group) 
            print("%s%s%d" % (current_word, separator, total_count))
	    if(total_count > most_count):
		most_count = total_count
		most = []
		most.append(current_word)
	    elif(total_count == most_count):
		most.append(current_word) 
	    
	    if(total_count < least_count):
		least_count = total_count
		least = []
		least.append(current_word)
	    elif(total_count == least_count):
		least.append(current_word)

        except ValueError: 
            # count was not a number, so silently discard this item 
            pass 
    for mo in most:
    	print("Most frequent word is: %s. It appreas %s many times."%(mo,most_count))
    for le in least:
	print("Least frequent word is: %s. It appears %s many times."%(le,least_count))
if __name__ == "__main__": 
    main() 
