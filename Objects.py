ROCK = 0
PAPER = 1
SCISSORS = 2

class Person():
    def __init__(self, Group, Mutation_factor, age) -> None:
        self.Group = Group
        self.Mutation_factor = Mutation_factor
        self.age = age
        
class Tree():
    def __init__(self) -> None:
        self.Person_count = 0
        self.Persons = []
    
    def add_Person(self, Person):
        self.Person_count += 1
        self.Persons.append(Person)