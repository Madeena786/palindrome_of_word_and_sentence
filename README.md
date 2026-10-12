### **Palindrome Checker**

###### 

###### **Project Description**



This project is a simple Python program that checks whether a word or sentence is a palindrome.



A palindrome is a word or sentence that reads the same forward and backward.



The program converts the input into lowercase, removes spaces, reverses the string, and compares the original string with its reverse.



###### **Objective**



The main objective of this project is to practice:



\- String manipulation

\- String methods

\- String slicing

\- Conditional statements

\- User input



###### **Technologies Used**



\- Python



###### **How the Program Works**



The program follows these steps:



1\. Take a word or sentence from the user.

2\. Convert the input into lowercase using `lower()`.

3\. Remove spaces using `replace()`.

4\. Reverse the string using `\[::-1]`.

5\. Compare the original string with the reversed string.

6\. Display whether it is a palindrome or not.



###### **Python Program**

t=input("Enter a word or sentence: ")

t=t.lower()

t=t.replace(" ", "")

r=t\[::-1]



if t==r:

&#x20;   print("It is a palindrome.")

else:

&#x20;   print("It is not a palindrome.")



**Sample Output 1**

Enter a word or sentence: 1234321

It is a palindrome.



**Sample Output 2**

Enter a word or sentence: madeena

It is not a palindrome.


**Sample Output 3**

Enter a word or sentence: Never Odd Or Even

It is a palindrome.



###### **Key Concepts**

lower()

The lower() method converts all uppercase letters into lowercase letters.

**Example:**

t = "Madam"t = t.lower()





**Output:**

madam



replace()

The replace() method is used to remove spaces from the input.

t = t.replace(" ", "")





String Slicing

The \[::-1] syntax reverses a string.

r = t\[::-1]





**Example:**

madam → madam

hello → olleh



if-else

The if-else statement compares the original string with its reverse.

if t == r:    print("It is a palindrome.")else:    print("It is not a palindrome.")



###### 

###### **Conclusion**

This project demonstrates how Python string methods, slicing, user input, and conditional statements can be used to create a simple Palindrome Checker.

