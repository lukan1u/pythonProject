class WhiteDog:
    # it will always run
    def __init__(self, name):
        self.name = name
        print(name)

    # methods 
    def bark(self):
        print("bark")

    # self is linking
    def add_one(self, x):
        return x + 1
    
    def set_new_name(self, name):
        self.name = name
        print(name)
 
d = WhiteDog("Josh")
d.bark()
d.set_new_name("Lol") 
print(d.add_one(5))
