def main():
    userAns = input("What year is it? ")

    if userAns=="q":
        return 'q'
    try:
        userAns = int(userAns)
        if (userAns % 12 == 0 ):
            return "It the year of the monkey"
        elif (userAns % 12 == 1 ):
            return "It the year of the rooster"
        elif (userAns % 12 == 2 ):
            return "It the year of the dog"
        elif (userAns % 12 == 3 ):
            return "It the year of the pig"
        elif (userAns % 12 == 4 ):
            return "It the year of the rat"
        elif (userAns % 12 == 5 ):
            return "It the year of the ox"
        elif (userAns % 12 == 6 ):
            return "It the year of the tiger"
        elif (userAns % 12 == 7 ):
            return "It the year of the rabit"
        elif (userAns % 12 == 8 ):
            return "It the year of the dragon"
        elif (userAns % 12 == 9 ):
            return "It the year of the snake"
        elif (userAns % 12 == 10 ):
            return "It the year of the horse"
        elif (userAns % 12 == 11 ):
            return "It the year of the sheep"
    except:
        return "User Input is not a year"

if __name__=="__main__":
    while True:
        output=main()
        if output=='q':
            break
        else:
            print(output)
