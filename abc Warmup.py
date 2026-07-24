class fruit:
    print("An apple is a fruit that is sweet and it can be red or green")
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def intro(self):
        print("Hello I am", self.name)
#obj = apple()
apple = fruit("Apple", "Red")
apple.intro()