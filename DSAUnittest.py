import unittest as ut
import unittest.mock
from primermodule import finding_number
from primermodule import rd

class DSAUnittest(ut.TestCase):
    def test_check_finding_missing_number(self):
        self.input=12
        l=list(range(self.input))
        removed=rd.randrange(self.input)
        l.remove(removed)
        print("TEST : we have removed ",removed)
        result=finding_number(self.input,l)
        self.assertEqual(removed,result)

if __name__== '__main__':
    ut.main()
