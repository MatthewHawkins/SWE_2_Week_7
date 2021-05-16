import word_count
import unittest



class TestCase(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(word_count.word_count("word"), 1)
        
    def test_multiple_words(self):
        self.assertEqual(word_count.word_count("Hello, this should come back as seven"), 7)
    
    #This comes back as failed, but this is what we want, as it checks for only spaces not being
    #counted as actual words
    def test_only_spaces(self):
        self.assertEqual(word_count.word_count("     "), 0)

    def test_many_words_together(self):
        self.assertEqual(word_count.word_count("ThisShouldBeOne"), 1)


if __name__ == "__main__":
    unittest.main()