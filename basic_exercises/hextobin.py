#Input a Hexadecimal number and Convert it to Decimal
if __name__=="__main__":
    nonHex='ghijklmnopqrstuvwxyz'
    hexFlag=True
    while True:
        hexIn=input("    Insert HEX: ")
        
        if hexIn == 'exit':
            break
        #Check if input is a valid Hexadecimal Number
        for i in nonHex:
            if i in hexIn:
                hexFlag=False
        if hexFlag is False:
            print("    You did not insert a HEX Number")            
            hexFlag=True
        else:
            print("    You Inserted 0x"+ hexIn)

            decValue = str(int(hexIn, 16))
            print("    0x"+hexIn + " Converted to Decimal is "+ decValue)
