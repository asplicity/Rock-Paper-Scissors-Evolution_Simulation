import pandas as pd
import matplotlib.pyplot as plt
from SETTINGS import *

def analyze(path):
    Data = pd.read_csv(path)
    plt.plot(Data['day'], Data['count_people'])
    plt.title("population per day")
    plt.xlabel("Day")
    plt.ylabel("population")
    plt.savefig("diagrams/day.png")
    
    plt.cla()
    
    plt.plot(Data["day"], Data["count_rock"], label="Rock")
    plt.plot(Data["day"], Data["count_paper"], label="Paper")
    plt.plot(Data["day"], Data["count_scissors"], label="scissors")
    plt.legend(loc='upper left')
    plt.savefig("diagrams/Evolution.png")