import random as r
import Objects
from SETTINGS import *

def new_round(Trees: list[Objects.Tree], people: list[Objects.Person]) -> None:
    for i, Person in enumerate(people):
        if i // 2 < len(Trees):
            Trees[i//2].add_Person(Person=Person)
    
    for i in Trees:
        i.get_Winner()

def new_Generation(people: list[Objects.Person]):
    children = []
    for i in people:
        for j in range(i.Apples):
            if round(r.random(), 2) > Mutation_factor:
                children.append(Objects.Person(i.Group, Mutation_factor=Mutation_factor, Apples=0))
            else:
                children.append(Objects.Person(Group=r.randint(0, 2), Mutation_factor=Mutation_factor, Apples=0))
    return children

if __name__ == "__main__":
    pass