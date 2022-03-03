# DONT TOUCH THIS FILE IF YOU DONT KN0W WHAT YOURE DOING

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random
from settings import imagiane, nphotos, nlayers


randomizer = []
saveeeeed = []
Stillindevelopment = True


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
        
        
if Stillindevelopment == True:
    print("Hello, Thank you for downloading this Project, Its still in development so its still not functional so then please wait till it works")
elif len(imagiane) < 2 or isinstance(nphotos, int) == False or isinstance(nlayers, int) == False:
    print("Make sure that you dont leave the none of the settings.py variables are blank. If you dont know what that does please read the settings.py")    
    print("Any questions make sure to ask on the github page or in a our discord server")
else:
    mainss()
    print(saveeeeed)




