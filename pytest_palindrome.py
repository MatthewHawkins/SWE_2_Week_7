import palindrome


def test_single_word():
    assert palindrome.palindrome("racecar") == True
    
def test_taco_space():
    assert palindrome.palindrome("taco cat") == True

#This comes back as failed, but this is what we want, as it checks for capital letters
#not being properly accounted for
def test_capitals():
    assert palindrome.palindrome("Taco Cat") == True

def test_not_palindrome():
    assert palindrome.palindrome("Matthew") == False