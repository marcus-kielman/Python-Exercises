class MyDog:
    def __init__(self, breed, name, age, color):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.isAsleep = False

    def walk(self):
        print(f"{self.name} is walking!")
    
    def eat(self):
        print(f"{self.name} is eating food!")
    
    def sleep(self):
        if(self.isAsleep==False):
            self.isAsleep=True
            print(f"{self.name} is sleeping!")
        else:
            return
    
    def wake_up(self):
        if(self.isAsleep==True):
            self.isAsleep=False
            print(f"{self.name} is waking up!")
        else:
            return
    
    def info(self):
        print(self.name, self.breed, self.age, self.color)

def main():
    mydogOne = MyDog("german shepard", "Ace", 4, "black")
    mydogTwo = MyDog("Pitbull", "Luke", 8, "gray")

    mydogOne.walk()
    mydogOne.sleep()

    mydogTwo.eat()
    mydogTwo.sleep()

    mydogOne.wake_up()
    mydogOne.eat()

    mydogOne.info()
    mydogTwo.info()

if __name__=="__main__":
    main()