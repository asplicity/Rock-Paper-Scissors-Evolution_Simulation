import Objects

def new_round(Trees: list[Objects.Tree], people: list[Objects.Person]) -> None:
    for i, Person in enumerate(people):
        if i // 2 <= len(Trees):
            Trees[i//2].add_Person(Person=Person)
    for i in Trees:
        print(f"{i.People},{i.Person_count}")
    
    for i in Trees:
        i.get_Winner()

def new_Generation(people: list[Objects.Person]):
    children = []
    for i in people:
        for j in i.Apples:
            children.append(Objects.Person(i.Group))

if __name__ == "__main__":
    pass