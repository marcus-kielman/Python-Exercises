def main():
    userAns = input("What year is it? ")

    if userAns=="q":
        return 'q'
    try:
        userAns = int(userAns)
        if ((userAns % 4 == 0 and userAns % 100 != 0)or(userAns%400==0) ):
            return "It is a leap year"
        else:
            return "It is Not a leap year"
    except:
        return "User Input is not a year"

if __name__=="__main__":
    while True:
        output=main()
        if output=='q':
            break
        else:
            print(output)
