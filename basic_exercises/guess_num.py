import random

def main(numOne):
    userAns = input("Guess what number: ")
    
    if userAns=="q":
        return 'q'
    try:
        if (int(userAns) == numOne):
            return True
        elif(int(userAns) < numOne):
            return "Too Low"
        elif(int(userAns) > numOne):
            return "Too High"
    except:
        return "User Input is not an integer"

if __name__=="__main__":
    numOne = random.randint(0, 100)
    while True:
        output=main(numOne)
        if output=='q':
            break
        else:
            if (output==True):
                print(output)
                numOne = random.randint(0, 100)
            else:
                print(output)
