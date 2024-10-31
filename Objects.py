from SETTINGS import *

class Person():
    def __init__(self, Group, Mutation_factor, Apples) -> None:
        self.Group = Group
        self.Mutation_factor = Mutation_factor
        self.Apples = Apples
    
    def get_won(self, Guy, Enemy):
        if Guy == Enemy:
            self.Apples += 1
        elif Guy == ROCK and Enemy == SCISSORS or Guy == PAPER and Enemy == ROCK or Guy == SCISSORS and Enemy == PAPER:
            self.Apples += 3
        else:
            pass
        
class Tree():
    def __init__(self) -> None:
        self.People: list[Person] = []
        self.Person_count = 0
        
    
    def add_Person(self, Person):
        self.People.append(Person)
        self.Person_count += 1
    
    def get_Winner(self):
        if self.Person_count == 0:
            pass
        elif self.Person_count == 1:
            self.People[0].Apples += 2
        elif self.Person_count == 2:
            self.People[0].get_won(self.People[0].Group, self.People[1].Group)
            self.People[1].get_won(self.People[1].Group, self.People[0].Group)
        self.People = []
        self.Person_count = 0