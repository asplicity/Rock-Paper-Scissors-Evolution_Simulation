import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as r
import Objects
import Round

Start_people = 9
Mutation_factor = 0
Tree_count = 15
Days = 2

def main():
    print("--Day 1--")
    People = [Objects.Person(Group=i%3, Mutation_factor=Mutation_factor, Apples=0, age=0) for i in range(Start_people)]
    r.shuffle(People)
    Trees = [Objects.Tree() for i in range(Tree_count)]
    for i in People:
        print(i.Apples)
    Round.new_round(Trees=Trees,people=People)
    for i in People:
        print(i.Apples)
    
    for i in range(Days - 1):
        print(f"--Day {i + 2}--")
        People = Round.new_Generation(people=People)
    
    

if __name__ == "__main__":
    main()