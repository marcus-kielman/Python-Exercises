def main():
    status = input("What is your tax status? ")
    income = input ("What is your annual income? ")
    if status=="q" or income=='q':
        return 'q'
    try:
        income = float(income)
        if (int(status)==0):
            if (income <= 8350 and income >= 0):
                return "Tax Based on Income: {}".format(0.10*income)
            elif (income <= 33950 and income >= 8351):
                return "Tax Based on Income: {}".format(0.15*income)
            elif (income <= 82250 and income >= 33951):
                return "Tax Based on Income: {}".format(0.25*income)
            elif (income <= 171550 and income >= 82251):
                return "Tax Based on Income: {}".format(0.28*income)
            elif (income <= 372950 and income >= 171551):
                return "Tax Based on Income: {}".format(0.33*income)
            elif (income >= 372951):
                return "Tax Based on Income: {}".format(0.35*income)
            else:
                return "Input is not a valid income"            
        elif (int(status)==1):
            if (income <= 16700 and income >= 0):
                return "Tax Based on Income: {}".format(0.10*income)
            elif (income <= 67900 and income >= 16701):
                return "Tax Based on Income: {}".format(0.15*income)
            elif (income <= 137050 and income >= 67901):
                return "Tax Based on Income: {}".format(0.25*income)
            elif (income <= 208850 and income >= 137051):
                return "Tax Based on Income: {}".format(0.28*income)
            elif (income <= 372950 and income >= 208851):
                return "Tax Based on Income: {}".format(0.33*income)
            elif (income >= 372951):
                return "Tax Based on Income: {}".format(0.35*income)
            else:
                return "Input is not a valid income"
        elif (int(status)==2):
            if (income <= 8350 and income >= 0):
                return "Tax Based on Income: {}".format(0.10*income)
            elif (income <= 33950 and income >= 8351):
                return "Tax Based on Income: {}".format(0.15*income)
            elif (income <= 68525 and income >= 33951):
                return "Tax Based on Income: {}".format(0.25*income)
            elif (income <= 104425 and income >= 68526):
                return "Tax Based on Income: {}".format(0.28*income)
            elif (income <= 186475 and income >= 104426):
                return "Tax Based on Income: {}".format(0.33*income)
            elif (income >= 186476):
                return "Tax Based on Income: {}".format(0.35*income)
            else:
                return "Input is not a valid income"
        elif (int(status)==3):
            if (income <= 11950 and income >= 0):
                return "Tax Based on Income: {}".format(0.10*income)
            elif (income <= 45500 and income >= 11951):
                return "Tax Based on Income: {}".format(0.15*income)
            elif (income <= 117450 and income >= 45501):
                return "Tax Based on Income: {}".format(0.25*income)
            elif (income <= 190200 and income >= 117451):
                return "Tax Based on Income: {}".format(0.28*income)
            elif (income <= 372950 and income >= 190201):
                return "Tax Based on Income: {}".format(0.33*income)
            elif (income >= 372951):
                return "Tax Based on Income: {}".format(0.35*income)
            else:
                return "Input is not a valid income"
        else:
            return "Displayed Wrong Status"
    except:
        return "User Input is not a number"

if __name__=="__main__":
    while True:
        output=main()
        if output=='q':
            break
        else:
            print(output)
