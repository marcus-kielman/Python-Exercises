import random

def main(numOne, numTwo):
    userAns = input("What is {} + {}? ".format(numOne, numTwo))
    
    if userAns=="q":
        return 'q'
    try:
        if (int(userAns) == (numOne+numTwo)):
            return True
        else:
            return False    
    except:
        return "User Input is not an integer"

if __name__=="__main__":
    numOne = random.randint(0, 100)
    numTwo = random.randint(0, 100)
    while True:
        output=main(numOne, numTwo)
        if output=='q':
            break
        else:
            if (output==True):
                print(output)
                numOne = random.randint(0, 100)
                numTwo = random.randint(0, 100)
            else:
                print(output)
