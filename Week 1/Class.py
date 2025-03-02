class names:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def printSelfName(self): #first variable = self
        print(self.name)

    def weirdName(yay):
        print(yay.name)

    def printName(self, name): 
        print(name) #change this to return
    

#names("your name", your age)
me = names("John Smith",36)

me.printSelfName()
me.weirdName()
me.printName("yay")

me.name = "David"
me.printSelfName()

"""
nameyay = me.printName("Yay")
print(nameyay)
print(me.printName("hmm"))
"""