from collections import deque

# MOCK tests
users = [
    {"id": 1, "name": "Alice", "country": "BR"},
    {"id": 2, "name": "Bob", "country": "US"},
    {"id": 3, "name": "Charlie", "country": "BR"},
    {"id": 4, "name": "David", "country": "US"},
    {"id": 5, "name": "Alice", "country": "BR"}
]

def getUserNames():
    ret = []
    for item in users:
        ret.append(item['name'])

    print('list names:', ret)
    return ret


def getNameByIndex(index):
    print('Name of', index + 1, '=', users[index]['name'])
    return users[index]['name']

def createDictionary():
    ret = {}
    for item in users:
        ret.update({item['id']: item})

    print(ret)
    return ret


def groupDictionary():
    ret = {}
    for item in users:
        if item['country'] in ret:
            ret[item['country']].append(item)
        else:
            ret.update({item['country']: [item]})

    print(ret)
    return ret


def createSetWithCountries():
    ret = set()
    for item in users:
        ret.add(item['country'])

    print(ret)
    return ret


def hasCountryInTheSet(country):
    list = createSetWithCountries()
    print(country in list)
    return country in list


def createSimpleStack():
    arr = []

    arr.append("a")
    arr.append("b")
    arr.append("c")

    print(arr.pop())
    print(arr.pop())
    print(arr.pop())

def createSimpleQueue() -> int:
    arr = deque()

    arr.append("first request")
    arr.append("second request")
    arr.append("third request")

    print(arr.popleft())
    print(arr.popleft())
    print(arr.popleft())

def sortDictionaryByField():
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 27}
    ]
    sorted_users = sorted(users, key=lambda user: user["age"])

    print(sorted_users)
    return sorted_users

def sortListItemsAsc(list: list[int]):
    newItems = sorted(list)
    return newItems

def sortListItemsDesc(list: list[int]):
    list.sort(reverse=True)
    return list

def searchItem(l: list[int], target: int):
    list = sortListItemsAsc(l)
    left = 0
    right = len(list)

    while left < right:
        middle = (left + right) // 2

        if list[middle] == target:
            return middle

        if list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1