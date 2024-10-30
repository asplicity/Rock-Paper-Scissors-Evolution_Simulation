import Objects

def new_round(Trees: list[Objects.Tree], people: list[Objects.Person]) -> None:
    for i, Person in enumerate(people):
        if i // 2 <= len(Trees):
            Trees[i//2].add_Person(Person=Person)
    for i in Trees:
        print(i.People)
    
        

if __name__ == "__main__":
    pass