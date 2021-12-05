from datetime import date

today = date.today()
class MyDog:
    def __init__(self, breed, name, age, color, home_address):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.home_address = home_address
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
    
    def from_birthyear(self):
        cls = today.year - self.age
        return cls
    
    def move(self, destination):
        self.home_address = destination
        print(f"We moved to {self.home_address}!!")

    @staticmethod
    def checkup_needed(age):
        if((age-1)%3==0):
            return True
        else:
            return False

def main():
    mydogOne = MyDog("german shepard", "Ace", 4, "black", "151 Willmore Road")
    mydogTwo = MyDog("Pitbull", "Luke", 8, "gray", "142 Parkinson street")

    mydogOne.walk()
    mydogOne.sleep()

    mydogTwo.eat()
    mydogTwo.sleep()

    mydogOne.wake_up()
    mydogOne.eat()

    mydogOne.info()
    mydogTwo.info()

    print(f"First Dog address: {mydogOne.home_address}")
    mydogTwo.move("143 Webster Road")
    print(mydogOne.checkup_needed(mydogOne.age))
    print(mydogTwo.checkup_needed(mydogTwo.age))

if __name__=="__main__":
    main()