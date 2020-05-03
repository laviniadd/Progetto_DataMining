import math
from builtins import print
from parse_inkml import parse_inkml
from random import randrange

def remove_random_elements_inkml(inkml_file, percentage = 30):
    data = parse_inkml(inkml_file)  # Parses inkml file
    perc = len(data['group_id'].unique())*percentage/100 # dati quanti group_id ho, faccio il 30%: es ho 25 gropu_id distinti e faccio il 30% di 25.
    numRows = math.ceil(perc) # arrotondo la percentuale
    random_number = [] #lista vuota che servirà per segnare quali sono i numeri random usciti
    for i in range(numRows):
        # randrange gives you an integral value
        irand = randrange(0, len(data['group_id'].unique())) #prendo un numero random tra 0 e il numero di group_id distinti
        while irand in random_number:
            irand = randrange(0, len(data['group_id'].unique()))
        random_number.append(irand)

        # Get names of indexes for which column group_id has value irand
        indexNames = data[data['group_id'] == irand].index

        # Delete these row indexes from dataFrame
        data.drop(indexNames, inplace=True)
    return data

