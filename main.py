# DONT TOUCH THIS FILE IF YOU DONT KN0W WHAT YOURE DOING

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random
from settings import pathss, nphotos, nlayers


randomizer = []
saveeeeed = []
Stillindevelopment = True


def getfiles(path):
    files = os.listdir(path)
    random_file = random.choice(files)
    randomizer.append(os.path.abspath(os.path.join(path, random_file)))
   


def mainss():
    
    def pog():
        randomizer.clear()
        for i in range(0, nlayers):
            getfiles(pathss[i])
        
   


    for i in range(0, nphotos):
        
        pog()
        # print(randomizer)
        for i in range(0, nlayers):
            saveeeeed.append(randomizer[i])
            # saveeeeed.append(randomizer[0])
            # saveeeeed.append(randomizer[1])
        
        # "lASDosdAadasM"
        # on the part below depending on how much layers you have you will add plt.imshow(plt.imread(randomizer[2])) 3 and so on
        # (Tip just copy and paste for how much layers you need and change the numbers)
        plt.imshow(plt.imread(randomizer[0]))
        plt.imshow(plt.imread(randomizer[1]))
        plt.savefig(f'final/finalrender{i + 1}.png')
        plt.clf()
        
        
if Stillindevelopment == True:
    print("Hello, Thank you for downloading this Project, Its still in development so its still not functional so then please wait till it works")
elif len(pathss) < 2 or isinstance(nphotos, int) == False or isinstance(nlayers, int) == False:
    print("Make sure that you dont leave the none of the settings.py variables are blank. If you dont know what that does please read the settings.py")    
    print("Any questions make sure to ask on the github page or in a our discord server")
else:
    mainss()
    # print(saveeeeed)




