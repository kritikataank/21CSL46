a = int(input("First IA marks: "))
b = int(input("Second IA marks: "))
c = int(input("Third IA marks: "))

marks = [a,b,c]
marks.sort()
avg = (marks[-1]+marks[-2])/2
print(f"The best of two test average is: {avg}")