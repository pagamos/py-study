from helpers.numbers.helpers import (
    isEven,
    findLargestNumber,
    calculateFactorial,
    calculateAvarage,
    countDigits,
)


def main():
    print("isEven:", isEven(4))
    print("findLargestNumber:", findLargestNumber([5, 23, 190, 30, 4]))
    print("calculateFactorial:", calculateFactorial(5))
    print("calculateAvarage:", calculateAvarage([5, 23, 190, 30, 4]))
    print("countDigits:", countDigits(1234))


if __name__ == "__main__":
    main()