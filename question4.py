#write a program to find the sum of digits of a given number'
def sumofdigits(n):
    return sum(int(digit) for digit in str(abs(n)))

n = int(input("Enter a number: "))
result = sumofdigits(n)

print(f"The sum of the digits of {n} is {result}.")

