def is_palindrome(text):
    # Convert to lowercase and remove spaces
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

word = input("Enter a word or sentence: ")
if is_palindrome(word):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
