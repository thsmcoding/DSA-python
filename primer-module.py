import random as rd

def finding_number():
    try:
        n=int(input("Please enter an integer "))
        if n<=0:
            raise ValueError("Detected problem with your input. Check")
    finally:
        print("You have chosen number:", n)
        s=rd.sample(range(n),k=(n-1))
        print("This is the initialized sequence ",s)
        missing=sum(range(n)) - sum(s)
        print("The missing number is", missing)
        
if __name__== '__main__':
    finding_number()
