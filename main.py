import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as r
import Objects
import Round
from SETTINGS import *
import analyze

Data = pd.DataFrame(columns=['day', 'count_people', 'count_rock', 'count_paper', 'count_scissors'])


def append_data(People: list, day):

    new_data = pd.DataFrame([{
        'day': day,
        'count_people': len(People),
        'count_rock': sum(1 for i in People if i.Group == ROCK),
        'count_paper': sum(1 for i in People if i.Group == PAPER),
        'count_scissors': sum(1 for i in People if i.Group == SCISSORS)
    }])
    
    global Data
    Data = pd.concat([Data, new_data], ignore_index=True)

def save_data():
    Data.to_csv(path_to_data,index=False)
    

def main():
    People: list[Objects.Person] = [Objects.Person(Group=i%3, Mutation_factor=Mutation_factor, Apples=0) for i in range(Start_people)]
    r.shuffle(People)
    Trees = [Objects.Tree() for i in range(Tree_count)]
    
    for i in range(Days):
        print(f"--Day {i + 1}--")
        if i > 0:
            People = Round.new_Generation(people=People)
        r.shuffle(People)
        Round.new_round(Trees=Trees,people=People)
#       for j in People:
#           print(f"{j.Apples}, {j.Group}")
        append_data(People=People, day=i)
    
    save_data()
    
    analyze.analyze(path_to_data)
    

if __name__ == "__main__":
    main()