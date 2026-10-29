from helpers.numbers.helpers import (
    removeDuplicates,
    splitInChunks,
    findCommonElements,
    rotateList,
    findSecondLargest,
)


def main():
    print("removeDuplicates:", removeDuplicates([1, 2, 3, 4, 5, 2, 6, 7, 8, 1]))
    print("splitInChunks:", splitInChunks([1, 2, 3, 4, 5, 6 ,7 ,8], 3))
    print("findCommonElements:", findCommonElements([1, 2, 3, 4, 5], [2, 6, 7, 5, 8, 1]))
    print("rotateList:", rotateList([1, 4, 6, 8, 9, 99, 19]))
    print("findSecondLargest:", findSecondLargest([1, 2, 3, 4444, 5, 6, 7, 22, 33, 12, 85, 199, 200]))


if __name__ == "__main__":
    main()