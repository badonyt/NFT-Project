# DONT TOUCH THIS FILE IF YOU DONT KN0W WHAT YOURE DOING

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random
from settings import imagiane, nphotos, nlayers


randomizer = []
saveeeeed = []


def getfiles(path):
    files = os.listdir(path)
    random_file = random.choice(files)
    randomizer.append(os.path.abspath(os.path.join(path, random_file)))
   


def mainss():
    # "lASDosdAadasM"
    # on pog depending on how much layers you have you will add getfiles2 3 etc
    def pog():
        randomizer.clear()
        getfiles(imagiane[0])
        getfiles(imagiane[1])
   


    for i in range(0, nphotos):
        
        pog()
        saveeeeed.append(randomizer[0])
        saveeeeed.append(randomizer[1])
        
        for i in range(0, nlayers):
            plt.imshow(plt.imread(randomizer[i]))
        plt.savefig(f'final/finalrender{i + 1}.png')
        plt.clf()
        
        


mainss()
print(saveeeeed)




