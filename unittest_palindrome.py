import palindrome
import unittest



class TestCase(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(palindrome.palindrome("racecar"), True)
        
    def test_taco_space(self):
        self.assertEqual(palindrome.palindrome("taco cat"), True)
    
    #This comes back as failed, but this is what we want, as it checks for capital letters
    #not being properly accounted for
    def test_capitals(self):
        self.assertEqual(palindrome.palindrome("Taco Cat"), True)

    def test_not_palindrome(self):
        self.assertEqual(palindrome.palindrome("Matthew"), False)


if __name__ == "__main__":
    unittest.main()