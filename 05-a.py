import re

def isphonenumber(numstr):
    if len(numstr) != 12:
        return False
    for i in range(len(numstr)):
        if i == 3 or i == 7:
            if numstr[i] != "-":
                return False
        else:
            if numstr[i].isdigit() == False:
                return False
    return True


def checkphonenumber(numstr):
    phone_number_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if phone_number_pattern.match(numstr):
        return True
    else:
        return False


ph_num = input("Enter a phone number: ")
print("\nWithout using Regular Expression")
if isphonenumber(ph_num):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
print("\nUsing Regular Expression")
if checkphonenumber(ph_num):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")