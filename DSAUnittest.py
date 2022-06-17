import unittest as ut
import unittest.mock
from primermodule import finding_number
from primermodule import rd

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
    
if __name__== '__main__':
    ut.main()
