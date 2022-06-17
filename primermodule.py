import random as rd

def finding_number(n,s):
        if n <= 1:
            raise ValueError("Detected problem with your input. Check")
        elif len(s) < 2 or s is None:
            raise IndexError("The list is empty or None.")
        else:
            print("You have chosen number:", n)
            print("This is the initialized sequence ",s)
            missing=sum(range(n)) - sum(s)
            print("The missing number is", missing)
            return missing
    
