import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import Objects
import Round

Start_people = 9
Mutation_factor = 0
Tree_count = 15

def main():
    People = [Objects.Person(Group=i%3, Mutation_factor=Mutation_factor, age=0) for i in range(Start_people)]
    Trees = [Objects.Tree() for i in range(Tree_count)]
    Round.new_round(Trees=Trees,people=People)
    

if __name__ == "__main__":
    main()