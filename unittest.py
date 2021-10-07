#-------------------------------------------------------------------------------------------------------------------------main.py

def add(a, b):
    return a + b

def add_numbers():
    a = 3
    b = 2
    return add(a,b)

#-------------------------------------------------------------------------------------------------------------------------test.py

import unittest
from unittest.mock import patch
from unittest import TestCase

class TestSecureCX(TestCase):
    
    def mock_add_func(a, b):
        return a-b
    
    @patch('main.add', side_effect = mock_add_func)
    def test_facenet(self, mock_add):
        from main import add_numbers
        add_numbers()
        print(add_numbers())
            
if __name__ == '__main__':
    unittest.main()

#-------------------------------------------------------------------------------------------------------------------------test_template.py

import unittest
from unittest.mock import patch, Mock
from unittest import TestCase

class TestSecureCX(TestCase):
    
    @classmethod
    def setUpClass(cls):
        #run at start of the first test
        pass
    
    def setUp(self):
        #run at start of the every test
        pass
    
    def tearDown(self):
        #run at the end of the every test
        pass
    
    def test_facenet(self):
        pass
    
    def test_faceqnet(self):
        pass
    
    @classmethod
    def tearDownClass(cls):
        #run at the end of last test
        pass

if __name__ == '__main__':
    unittest.main()
