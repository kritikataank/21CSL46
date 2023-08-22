num1 = input("Enter number to check whether its a palindrome or not: ")
num2 = num1[::-1]
if num1 == num2:
    print(f"The number {num1} is a palindrome")
else:
    print(f"The number {num1} is not a palindrome")

original = list(num1)
l = []
for i in num1:
    if i not in l:
        l.append(i)
    else:
        continue
for j in l:
    print(f"The number {j} appears {original.count(j)} times.")