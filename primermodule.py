import random as rd

def finding_number(n,s):
    try:
        if n<=0:
            raise ValueError("Detected problem with your input. Check")
        if len(s)==0 or s is None:
            raise IndexError("The list is empty or not declared.")
    finally:
        print("You have chosen number:", n)
        print("This is the initialized sequence ",s)
        missing=sum(range(n)) - sum(s)
        print("The missing number is", missing)
        return missing

