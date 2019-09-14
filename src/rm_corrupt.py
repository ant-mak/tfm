from os import listdir, remove
from PIL import Image
import warnings
warnings.filterwarnings("error")

file_path = '../data/paintings/test/'

for filename in listdir(file_path):
    if filename.endswith('.jpg'):
        try:
            img = Image.open(file_path+filename) # open the image
            img.verify() # verify that it is, in fact an image
        except:
            print('Bad file:', filename) # print out the name of the corrupt file
            remove(file_path+filename) # remove corrupt file