print('Hello there! Welcome to the palindrome seeker!')
print("1! 2! 3! Let's begin!!!")

def palindrome(word):
    if word == word[::-1]:
        print("I didn't know that this is a palindrome, either. You're right. It is a palindrome!")
    else:
        print("Don't worry about it. It's not a palindrome. So try again!")  
        
print("Write the word that you would like to know if it's a palindrome:")
word = input()
palindrome(word)
