import os

from bounding_boxes_random_remove import bounding_boxes_random_remove
from plot_inkml_random_remove import plot_inkml_random_remove
from plot_inkml_remove_text import plot_inkml_remove_text


def inkml2png_augmented(inkml_folder):  # inkml_folder must be in the same directory as this script
    png_folder = 'FCinkML' + '_aug'  # New png folder name

    if not os.path.exists(png_folder):  # Creates folder if it doesn't already exist (to avoid 'directory not found' errors)
        os.makedirs(png_folder)

    print('Dataset conversion started...')

    for filename in os.listdir(inkml_folder):
            if '.inkml' in filename:  # Only considers inkml files in folder
                print('Converting ' + filename + '... ', end='')
                if not ('b' in filename):
                    data_frame_removed_random_elements = plot_inkml_random_remove(inkml_folder + '/' + filename) # genera immagini senza un elemento scelto a random
                    name = filename.replace('writer', 'writer_rand_').replace('.inkml', '.png')
                    bounding_boxes_random_remove(data_frame_removed_random_elements, name)
                    print('done!')
                else:
                    print('Test File')


    print('Dataset conversion completed.')