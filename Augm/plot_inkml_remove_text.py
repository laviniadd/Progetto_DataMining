import matplotlib.pyplot as plt
from parse_inkml import parse_inkml


def plot_inkml_remove_text(data, save=True):
    print(data)
    filename = None
    if not ('b' in data):  # controlla che il file su cui fare i bb sia un file di train e NON di test
        with open('colors','r') as c:  # List of colors for each class, read from the 'colors' file
            colors = eval(c.read())

        if isinstance(data, str):
                filename = data
                data = parse_inkml(data)  # Parses the inkml file if the input data is a filename (string) instead of some already processed inkml data (list)


        for i in range(0, len(data['trace'])):  # data['trace'] is a list of traces; each element contains a trace, and each trace has a list of [x, y] coordinates
            x = []
            y = []
            for j in range(0, len(data['trace'][i])):  # Returns j-th point of each trace
                x.append(data['trace'][i][j][0])  # Returns x coordinate of the j-th point of each trace
                y.append(data['trace'][i][j][1])  # Returns y coordinate of the j-th point of each trace

            if not(data['class'][i] == 'Text'): # se ha come classe Text non viene plot
                plt.plot(x, y, color='black', linewidth=0.6)


        plt.axis('equal')  # Constrain proportions
        plt.axis('off')  # Remove axes from figure

        if save and filename is not None:  # If save = True and the input data is a filename (not some already processed data), it saves the plot as a 640x480 px png image in a folder with the same name as the original file folder, with '_png' added at the end
            fig1 = plt.gcf()
            #plt.show()
            plt.draw()
            #plt.cla()
            fig1.savefig('path/FCinkML_aug/' + filename.partition('/')[2].replace('FCinkML', 'FCinkML_aug').replace('writer', 'writer_augm_').replace('inkml', 'png')) #cambio il nome in modo da non sovrascrivere le immagini
            #fig1.savefig(filename.partition('/')[0] + '_aug/' + filename.partition('/')[2].replace('inkml', 'png'))

            plt.cla()  # Clears plot (otherwise subsequent plots would be drawn over the older ones)
    else:
        print('Test File')