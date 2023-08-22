def roman2dec(romstr):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    RomanBank = list(romstr)[::-1]
    value = 0
    rightValue = roman_dict[RomanBank[0]]
    for numeral in RomanBank:
        leftValue = roman_dict[numeral]
        if leftValue < rightValue:
            value -= leftValue
        else:
            value += leftValue
        rightValue = leftValue
    return value


romanstr = input("Enter a Roman Number: ")
print(roman2dec(romanstr))