class Stack(object):
    def __init__(self):
        self.array = [[], []]

    def l_push(self, data):
        self.array[0].append(data)

    def l_pop(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            self.array[0].pop()

    def r_push(self, data):
        self.array[1].append(data)

    def r_pop(self):
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            self.array[1].pop()

    def show(self):
        if len(self.array[0]) == 0:
            print('Left Stack is empty')
        else:
            print('Left Stack:', self.array[0])
        if len(self.array[1]) == 0:
            print('Right Stack is empty')
        else:
            print('Right Stack:', self.array[1])


import unittest
class TestStack(unittest.TestCase):
    stack=Stack()
    def testLstack(self):
        print("Left Stack")
        self.stack.l_push(1)
        self.stack.l_pop()
        self.stack.l_pop()
        self.stack.l_push(1)
        self.stack.l_push(2)

    def testRstack(self):
        print("Right Stack")
        self.stack.r_push(1)
        self.stack.r_pop()
        self.stack.r_pop()
        self.stack.r_push(1)
        self.stack.r_push(2)
    def testShow(self):
        print("Stack Show")
        self.stack.show()

def suite():
  suite = unittest.TestSuite()
  suite.addTest(TestStack("testLstack"))
  suite.addTest(TestStack("testRstack"))
  suite.addTest(TestStack("testShow"))
  return suite
if __name__ == "__main__":
  unittest.main(defaultTest = 'suite')
#.Left Stack
# Stack a is empty
# .Right Stack
# Stack b is empty
# .Stack Show
# Left Stack: [1, 2]
# Right Stack: [1, 2]