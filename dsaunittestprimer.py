import unittest as ut
import unittest.mock
from math import factorial
from primermodule import rd, finding_number, permutations


class DSATestMethods(ut.TestCase):
    def test_finding_number_success(self):
        print("###### Unit Test : finding_number SUCCESS ####### \n")
        self.input=12
        l=list(range(self.input))
        removed=rd.randrange(self.input)
        l.remove(removed)
        print("TEST : we have removed ",removed)
        actual=finding_number(self.input,l)
        expected= removed
        self.assertEqual(actual, expected)

    def test_finding_number_valueexception(self):
        print("###### Unit Test : ValueError ####### \n")
        self.size=1
        with self.assertRaises(ValueError) as exception_context:
            finding_number(n=self.size,s=list((range(self.size))))
        self.assertEqual(str(exception_context.exception),
                         "Detected problem with your input. Check")
        
    def test_finding_number_indexexception(self):
        print("###### Unit Test : Index Error ####### \n")
        self.inputlist=[]
        self.size=2
        with self.assertRaises(IndexError) as exception_context:
            finding_number(self.size,self.inputlist)
        self.assertEqual(str(exception_context.exception),
                         "The list is empty or None.")
        
    def test_permuations(self):
        print("TESTING PERMUTATIONS FOR 0 CHARACTERS:")
        self.l= []
        self.n= len(self.l)
        self.count=[0]
        permutations(self.l,0,self.n, self.count)
        actual, expected =0,self.count[0]
        self.assertEqual(actual, expected)

    def test_permuations(self):
        print("TESTING PERMUTATIONS FOR MULTIPLE CHARACTERS: \n")
        self.l= ['C','A','T', 'D', 'O', 'G']
        self.n= len(self.l)
        self.count=[0]
        permutations(self.l,0,self.n-1, self.count)
        print("Search has found "+ str(self.count[0])+ " permutations")
        actual, expected= self.count[0], factorial(self.n)
        self.assertEqual(actual, expected)
        
if __name__== '__main__':
    ut.main()
