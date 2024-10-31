import pandas as pd
import matplotlib.pyplot as plt
from SETTINGS import *

def analyze(path):
    Data = pd.read_csv(path)
    plt.plot(Data['day'], Data['count_people'])
    plt.title("population per day")
    plt.xlabel("Day")
    plt.ylabel("population")
    plt.savefig("diagrams/population.png")
    
    plt.cla()
    
    plt.plot(Data["day"], Data["count_rock"], label="Rock", color='gold')
    plt.plot(Data["day"], Data["count_paper"], label="Paper", color='red')
    plt.plot(Data["day"], Data["count_scissors"], label="scissors", color='green')
    plt.legend(loc='upper left')
    plt.savefig("diagrams/Evolution.png")
    
    plt.cla()
    
    plt.hist(Data["count_rock"])
    plt.title("Histogram Rock")
    plt.savefig("diagrams/Rock.png")
    
    plt.cla()
    
    plt.hist(Data["count_paper"])
    plt.title("Histogram Paper")
    plt.savefig("diagrams/Paper.png")
    
    plt.cla()
    
    plt.hist(Data["count_scissors"])
    plt.title("Histogram Scissors")
    plt.savefig("diagrams/Scissors.png")