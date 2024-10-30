import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Objects
import Round

Start_people = 9
Mutation_factor = 0
Tree_count = 15

def main():
    People = [Objects.Person(Group=i%3, Mutation_factor=Mutation_factor, Apples=0, age=0) for i in range(Start_people)]
    Trees = [Objects.Tree() for i in range(Tree_count)]
    for i in People:
        print(i.Apples)
    Round.new_round(Trees=Trees,people=People)
    for i in People:
        print(i.Apples)

if __name__ == "__main__":
    main()