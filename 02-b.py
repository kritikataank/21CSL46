def bintodec(val):
    rev = val[::-1]
    dec, i = 0, 0
    for dig in rev:
        dec += int(dig) * (2 ** i)
        i += 1
    return dec


def octtohex(val):
    rev = val[::-1]
    dec, i = 0, 0
    for dig in rev:
        dec += int(dig) * (8 ** i)
        i += 1
    print(f"Decimal: {dec}")
    lst = []
    while dec != 0:
        lst.append(dec % 16)
        dec = dec // 16
    n1 = []
    for elem in lst[::-1]:
        if elem <= 9:
            n1.append(str(elem))
        else:
            n1.append(chr(ord('A')+(elem-10)))
    hex = "".join(n1)
    return hex


num1 = input("Enter a Binary number: ")
print(f"Decimal: {bintodec(num1)}")
num2 = input("Enter an Octal number: ")
print(f"Hexadecimal: {octtohex(num2)}")