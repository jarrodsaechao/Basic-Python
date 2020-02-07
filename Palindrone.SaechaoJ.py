# Palindrome_SaechaoJ.py
# See if word is a Palindrome
# Jarrod Saechao
# 11/21/17
# Python 3.6.2



def main():
    word = input("Gimme a word ")
    removeChars = "1234567890!@#$%^&*()_+-={}[];',./<> "
    for char in removeChars:
        word = word.replace(char, '')
        
    if(word[0:] == word[-1::-1]):
        print("is a palindrome")
    else:
        print("is not a palindrome")
main()
