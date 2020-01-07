# Problem: Logic to print number in words up to a billion
# Implementation of Solution in Python by Raunak Sarbajna
# 6th January, 2020

import math
import sys

# Create list of digits
    
singles = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
doubles = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
large = ["hundred", "thousand", "million", "billion"]

def getIntegerLength(theNumber):
    """
        Optimal O(1) solution for getting the length of a numebr in python
        Taken from: https://stackoverflow.com/a/28883802/926543

    """
    if theNumber == 0:
        return 1
    if theNumber <= 999999999999997:
        return int(math.log10(theNumber)) + 1
    else:
        counter = 15
        while theNumber >= 10**counter:
            counter += 1
        return counter

def HundredsToWords(a):
    """
        Returns the entered number in hundreds converted into words

        Number must be positive

        Only works for numbers in hundreds
    """
    
    numLength = getIntegerLength(a)
    numlist = list(map(int, str(a)))
    numstring = ""

    for index, num in enumerate(numlist):
        if (numLength - index) > 2:
            numstring += singles[num] + " hundred"
            if (numlist[index+1] != 0) or (numlist[index+2] != 0):
                numstring += " and"
        elif ((numLength - index) > 1) and (num == 1):
            numstring += " " + doubles[numlist[index+1]]
            break
        elif ((numLength - index) > 1) and (num > 1):
            numstring += " " + tens[numlist[index]]
        elif ((numLength - index) == 1):
            numstring += " " + singles[numlist[index]]

    return numstring.strip()

def NumberToWords(a):

    """
        Returns the entered number converted into words

        Number can be positive or Negative

        Only works for numbers in billions
    """

    if a < 0:
        numstring = "minus "
    else:
        numstring = ""
    a = abs(a)

    numLength = getIntegerLength(a)

    if (numLength < 1) or (numLength > 12):
        return "null"

    if a == 0:
        return ("zero")

    numlist = list(map(int, str(a)))
    
    billions = False
    millions = False
    thousands = False
    hundreds = False

    for index, num in enumerate(numlist):
        if ((numLength - index) > 9) and (not billions):
            size = numLength - 9
            numstring += HundredsToWords(int (str(a)[:size]) ) + " billion "
            billions = True
        if ((numLength - index) > 6) and (not millions):
            size = numLength - 6
            if numLength > 9:
                numstring += HundredsToWords(int (str(a)[3:size]) ) + " million "
            else:
                numstring += HundredsToWords(int (str(a)[:size]) ) + " million "
            millions = True
        if ((numLength - index) > 3) and (not thousands):
            size = numLength - 3
            if numLength > 9:
                numstring += HundredsToWords(int (str(a)[6:size]) ) + " thousand "
            elif numLength > 6:
                numstring += HundredsToWords(int (str(a)[3:size]) ) + " thousand "
            else:
                numstring += HundredsToWords(int (str(a)[:size]) ) + " thousand "
            thousands = True
        if ((numLength - index) > 0) and (not hundreds):
            size = numLength
            if numLength > 9:
                numstring += HundredsToWords(int (str(a)[9:size]) )
            elif numLength > 6:
                numstring += HundredsToWords(int (str(a)[6:size]) )
            elif numLength > 3:
                numstring += HundredsToWords(int (str(a)[3:size]) )
            else:
                numstring += HundredsToWords(int (str(a)[:size]) )
            hundreds = True
    
    return numstring
    
if (len(sys.argv) - 1) > 0:
    print(NumberToWords(int(sys.argv[1])))
else:
    print("Run script as $python " + sys.argv[0] + " <number>")
