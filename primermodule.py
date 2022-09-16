import random as rd
import array as ar

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
    
def permutations(l, start, end, count):
        if start==end:
                print(''.join(l))
                count[0]= count[0]+1
        else:
                for i in range(start,end+1):
                        l[start], l[i] = l[i], l[start]
                        permutations(l,start+1, end, count)
                        l[start], l[i] = l[i], l[start]
def rec_count_div(n,l):
        if n<2:
                print(str(l[0])+ " divisions by 2 before getting a value less than 2.")
        else:
                l[0]=l[0]+1
                rec_count_div(n//2,l)

def ite_count_div(n,l):
        if n<2:
                print(str(l[0])+" divisions by 2 before getting a value less than 2.")
        else:
                while(n>=2):
                        l[0]=l[0]+1
                        n=n//2



def dot_pdt(a,b):
        try:
           a_info, b_info=a.buffer_info(), b.buffer_info()
           a_size, b_size=a_info[1], b_info[1]
           if a_size == b_size:
                   l=[a[i]*b[i] for i in range(a_size)]
           result=ar.array('i',l)
        except IndexError:
                raise("Issue with the length of one of the arrays.")
        return result
