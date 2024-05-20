# find if the given number is a palindrome or not?
n=input()
if n==n[::-1]:
    print(f"{n} is palindrome")
else:
    print(f"{n} is  not palindrome")
