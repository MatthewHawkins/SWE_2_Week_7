
def palindrome(word):
    length = len(word)
    for i in range(length):
        if word[length-i-1] != word[i]:
            print("This is not a palindrome")
            return False
        else:
            print("This is a palindrome")
            return True