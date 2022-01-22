import unittest
from name_function import get_formatted_name
class NameTestFunction(unittest.TestCase):
    """way to test functions"""
    def test_first_last_name(self):
        """look if first and last name work"""
        formatted_name=get_formatted_name("Mohamed Ali","Jmal")
        self.assertEqual(formatted_name,"Mohamed Ali Jmal")
        """ formatted_name=get_formatted_name("hama","hmal")
        # for test number have no role
        self.assertEqual(formatted_name,"Hama Hmal") """

if __name__=="__main__":
    unittest.main()
