import unittest

def encrypt(message):
    return 0

class LearnTeast(unittest.TestCase):

    def setUp(self):
        self.my_message = ""

    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    def test_funcReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message))

if __name__ == "___main__":
    unittest.main()
