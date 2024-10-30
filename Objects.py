ROCK = 0
PAPER = 1
SCISSORS = 2

class Person():
    def __init__(self, Group, Mutation_factor, Apples, age) -> None:
        self.Group = Group
        self.Mutation_factor = Mutation_factor
        self.age = age
        self.Apples = Apples
    
    def get_won(self, Guy, Enemy):
        if Guy == Enemy:
            self.Apples += 1
        if Guy == ROCK and Enemy == SCISSORS or Guy == PAPER and Enemy == ROCK or Guy == SCISSORS and Enemy == PAPER:
            self.Apples += 2
        
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
        else:
            self.People[0].get_won(self.People[0], self.People[1])
            self.People[1].get_won(self.People[1], self.People[0])