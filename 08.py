class PaliStr:
    def __init__(self):
        self.isPali = False
    def chkPali(self,mystr):
        if mystr == mystr[::-1]:
            self.isPali = True
        else:
            self.isPali=False
        return self.isPali

class PaliInt(PaliStr):
    def __init__(self):
        self.isPali =False
    def chkPali(self, val):
        temp = val
        rev = 0
        while temp!=0:
            dig = temp%10
            rev = (rev*10)+dig
            temp = temp//10
        if rev == val:
            self.isPali=True
        else:
            self.isPali=False
        return self.isPali

st = input("Enter a String: ")
sobj = PaliStr()
if sobj.chkPali(st):
    print("Given String is a Palindrome")
else:
    print("Given String is not a Palindrome")

val = int(input("Enter an Integer: "))
iobj = PaliInt()
if iobj.chkPali(val):
    print("Given Integer is a Palindrome")
else:
    print("Given Integer is not a Palindrome")