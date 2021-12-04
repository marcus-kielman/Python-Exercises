# Allows the user to input enter the interest rate, number of years
# and loan amount to compute monthly payment and total payment

if __name__=="__main__":
    while True:
        continue = input("    Continue (Y/N)? ")
        if continue==N or continue==n:
            break
        interestRate = input("      Interest Rate: ")
        numYears =     input("    Number of Years: ")
        loanAmount =   input("        Loan Amount: ")
        
        print( interestRate, numYears, loanAmount)
