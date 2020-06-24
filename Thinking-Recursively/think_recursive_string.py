'''
Given a string, str, and a character, char, your function countChar should count the number of char characters in the string str.
We have written a helper function countChar_ for you, but it only works for substring str[1:].
This means that you have to do processing for str[0] character while the rest of the answer can be found in the countChar_ function.

str = "abacada"
char = 'a'
'''


def countChar(string, char):
    count = 0

    if (len(string) == 0):
        return 0

    if (len(string) == 1):
        if (string[0] == char):
            return 1
        else:
            return 0

    countFrom1 = countChar(string[1:], char)
    if (string[0] == char):
        count = countFrom1 + 1
    else:
        count = countFrom1

    return count

print(countChar('shashank', 'a'))