import matplotlib.pyplot as plt
from parse_inkml import parse_inkml
import random
import pylab as pl
from remove_random_elements_inkml import remove_random_elements_inkml


def plot_inkml_random_remove(data):
    plt.clf()
    print('file da plottare:', data)
    filename = None
    with open('colors', 'r') as c:  # List of colors for each class, read from the 'colors' file
        colors = eval(c.read())

    if isinstance(data, str):
        filename = data
        data = remove_random_elements_inkml(data)
        data = data.reset_index(drop=True)

    for i in range(0, len(data[
                              'trace'])):  # data['trace'] is a list of traces; each element contains a trace, and each trace has a list of [x, y] coordinates
        x = []
        y = []
        for j in range(0, len(data['trace'][i])):  # Returns j-th point of each trace
            x.append(data['trace'][i][j][0])  # Returns x coordinate of the j-th point of each trace
            y.append(data['trace'][i][j][1])  # Returns y coordinate of the j-th point of each trace
            plt.plot(x, y, color='black', linewidth=0.6)

    plt.axis('equal')  # Constrain proportions
    plt.axis('off')  # Remove axes from figure

    fig1 = plt.gcf()
    fig1.savefig(
        'path/FCinkML_remove_random/' + filename.partition('/')[2].replace(
            'FCinkML',
            'FCinkML_random').replace(
            'writer', 'writer_rand_').replace('inkml',
                                              'png'))  # cambio il nome in modo da non sovrascrivere le immagini

    plt.cla()
    plt.clf()
    plt.close(fig1)
    return data
