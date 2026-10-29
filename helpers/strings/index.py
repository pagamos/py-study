from helpers.strings.helpers import (
    capitalize,
    checkForPalindrome,
    convertCamelCaseToSnaceCase,
    countVowels,
    removeWhitespaces,
)


def main():
    print("capitalize:", capitalize('aaavvvxxx'))
    print("checkForPalindrome:", checkForPalindrome('radarx'))
    print("convertCamelCaseToSnaceCase:", convertCamelCaseToSnaceCase("camelCase"))
    print("countVowels:", countVowels('avsadvseeeuuuiiiiadvsadv'))
    print("removeWhitespaces:", removeWhitespaces('asdsad sadsadsad asd wqdwqdwq1234 4214'))


if __name__ == "__main__":
    main()