t=input("Enter a word or sentence: ")
t=t.lower()
t=t.replace(" ", "")
r=t[::-1]
if t==r:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
