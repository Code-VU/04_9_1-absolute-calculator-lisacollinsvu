def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    if in_num > 21:
        print("Result: "+str(2*(in_num-21)))
    else:
        print("Result: "+str(21-in_num))
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
