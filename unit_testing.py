import unittest
from stack import IntegerStack

class TestIntegerStack(unittest.TestCase):

    def setUp(self):
        self.test_stack = IntegerStack()
   
    def test_push_integer(self):
        self.assertEqual(self.test_stack.push(4), [4])
        self.assertEqual(self.test_stack.push(0), [4, 0])
        self.assertEqual(self.test_stack.push(99999999), [4, 0, 99999999])
        self.assertEqual(self.test_stack.push(-4), [4, 0, 99999999, -4])

    def test_push_float(self):
        self.assertEqual(self.test_stack.push(0.76), [0])
        self.assertEqual(self.test_stack.push(-5.7456), [0, -5])

    def test_push_string(self):
        self.assertEqual(self.test_stack.push("56"), [56])
        self.assertEqual(self.test_stack.push("random string"), [56])
        self.assertEqual(self.test_stack.push("random string winh numbers 234548"), [56])



    def test_pop(self):
        self.assertEqual(self.test_stack.pop(), [])
        self.assertEqual(self.test_stack.push(4), [4])
        self.assertEqual(self.test_stack.push(3), [4, 3])
        self.assertEqual(self.test_stack.push(12), [4 , 3, 12])
        self.assertEqual(self.test_stack.pop(),  12)
        self.assertEqual(self.test_stack.pop(),  3)
        self.assertEqual(self.test_stack.pop(),  4)
        self.assertEqual(self.test_stack.pop(), [])

        

  
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()