class RabbitCare:
    def __init__(self, food, playing):
        self.__food = food
        self.__playing = playing
    def info(self):
        print(f"Rabbit care: food eaten - {self.__food}, playing - {self.__playing}")
    def play(self):
        print(f"The rabbit jumps and plays!")
    def get_food(self):
        return self.__food
    def set_food(self, new_food):
        if new_food >= 0:
            self.__food = new_food
            print(f"Food eaten updated to {self.__food}")
        else:
            print("Food eaten cannot be negative")
class BirdCare:
    def __init__(self, food, playing):
        self.__food = food
        self.__playing = playing
    def info(self):
        print(f"Bird care: food eaten - {self.__food}, playing - {self.__playing}")
    def play(self):
        print(f"The bird flies around and plays!")
    def get_food(self):
        return self.__food
    def set_food(self, new_food):
        if new_food >= 0:
            self.__food = new_food
            print(f"Food eaten updated to {self.__food}")
        else:
            print("Food eaten cannot be negative")
rabbit = RabbitCare(3, "30 minutes")
bird = BirdCare(2, "20 minutes")
print("=== Pet Care ===\n")
for pet in (rabbit, bird):
    pet.info()
    pet.play()
    print()
print("=== Direct change attempt ===")
rabbit.__food = 99999
print(f"get_food() still shows: {rabbit.get_food()}")
print("\n=== Updating food ===")
rabbit.set_food(5)
bird.set_food(4)
