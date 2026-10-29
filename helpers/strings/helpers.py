def capitalize(str):
    return str.capitalize()

def countVowels(str):
    ret = 0
    
    for c in str:
        if c in "aeiouAEIOU":
            ret = ret + 1
    

    return ret

def removeWhitespaces(str):
    return str.replace(' ', '')

def checkForPalindrome(str):
    reverseStr = ''
    i = 1
    while i <= len(str):
        reverseStr = reverseStr + str[-i]
        i = i + 1

    return str == reverseStr

def convertCamelCaseToSnaceCase(str):
    ret = ''
    i = 0
    while i < len(str):
        if str[i].isupper():
            ret = ret + '_' + str[i].lower()
        else:
            ret = ret + str[i]

        i = i + 1

    return ret
