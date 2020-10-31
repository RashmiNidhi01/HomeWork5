

import sys
import os
import logging

a_logger = logging.getLogger()
a_logger.setLevel(logging.DEBUG)

output_file_handler = logging.FileHandler("log.txt", mode='w')
stdout_handler = logging.StreamHandler(sys.stdout)

a_logger.addHandler(output_file_handler)
a_logger.addHandler(stdout_handler)

def average_score():
    return sum(my_list)/len(my_list)

fname = 'score1.txt'
try:
    with open(fname, 'r') as f:
        my_list = []
        for line in f:
            try:
                content = line.split(' ')
                scores = float(content[1])
                my_list.append(scores)
            except ValueError:
                a_logger.debug("Bad score value for " + content[0] + ", ignored.")
        out = "The class average is " + str(int(average_score())) + " for " + str(len(my_list)) + " students."
        a_logger.debug(out)
except IOError:
    a_logger.debug("Error: can't find the file or read the data.")