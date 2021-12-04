def main():
    userAns = input("What is your BMI? ")

    if userAns=="q":
        return 'q'
    try:
        if (float(userAns) < 18.5):
            return "Underweight"
        elif (float(userAns) >= 18.5 and float(userAns) < 25.0):
            return "Normal"
        elif (float(userAns) >= 25.0 and float(userAns) < 30.0):
            return "Overweight"
        else:
            return "Obese"
    except:
        return "User Input is not an integer"

if __name__=="__main__":
    while True:
        output=main()
        if output=='q':
            break
        else:
            print(output)


