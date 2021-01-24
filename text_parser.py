import argparse
import pandas as pd
from pandasgui import show
import re

#/Users/orennelson/Desktop/meeting_saved_chat.txt

def topic_parser(file_path, topic_array):
    #init topic array, the shorter the better, longer words are more specific
    # topic_array = ['sleep', 'food', ' eat ', 'relax', 'workout', 'hack reactor', 'imposter', 'help desk', 'water', 'docs']

    topics = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            for i in topic_array:
                if (re.search(i, line, re.IGNORECASE) != None):      #alternate is line.find(i) != -1 but it is case sensitive
                    if (i in topics.keys()):
                        topics[i].append(line)
                    else:
                        topics[i] = [line]
    
    return topics

def arrayEqualizer(topics):
    #need all arrays the same length so consider all dictionary property arrays, find one with longest length
    #now consider them all again and append until length is == longest length with '--' chars
    longest_length = 0
    for key in topics:
       if (len(topics[key]) > longest_length):
           longest_length = len(topics[key])
           
    for key in topics:
        if (len(topics[key]) < longest_length):
            difference = longest_length - len(topics[key])
            for i in range(difference):
                topics[key].append('--')

    ##check if all arrays are same length
    for key in topics:
        if (len(topics[key]) != longest_length):
            return f'failed test... longest_length is: {longest_length} and current array is: {len(topics[key])}'

    return f'all arrays same length'        


def printout(topics):
    #intakes a topics dictionary, outputs a human readable printout
    #convert dictionary to dict to pandas dataFrame
    #print dataframe

    df = pd.DataFrame.from_dict(topics, orient='columns')
    show(df)
       

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file")
parser.add_argument('-l','--list', nargs='+', help='<Required> Set flag', required=True)
args = parser.parse_args()

file_path = args.input
lst = args.list

#execute methods, define methods above
topics = topic_parser(file_path, lst)
arrayEqualizer(topics)
printout(topics)