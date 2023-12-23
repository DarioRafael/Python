
lista = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6]


def remove_duplicates(listNum):
    result = []
    for i in listNum:
        if i not in result:
            result.append(i)
    return result


print(remove_duplicates(lista))


def remove_duplicates(listNum):
    return list(dict.fromkeys(listNum))


print(remove_duplicates(lista))
