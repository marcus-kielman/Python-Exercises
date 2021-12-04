import random

def main(charOne):
    userAns = input("Guess what letter: ")
    
    if userAns=="quit":
        return 'quit'
    try:
        userAns = ord(userAns)
        if (userAns == charOne):
            return True
        elif(ord(userAns) < charOne):
            return "Too Low"
        elif(ord(userAns) > charOne):
            return "Too High"
    except:
        return "User Input is not an character"
if __name__=="__main__":
    charOne = random.randint(ord('a'), ord('z'))
    while True:
        output=main(charOne)
        if output=='quit':
            break
        else:
            if (output==True):
                print(output)
                charOne = random.randint(ord('a'), ord('z'))
            else:
                print(output)
