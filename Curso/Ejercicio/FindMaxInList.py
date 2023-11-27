numList = [2,4,3,20,2,1,5,6,2,10]

def find_max_in_list(list):
    if len(list) == 0:
        return None
    mayor = list[0]
    for num in list:
        if num > mayor:
            mayor = num
    return mayor
print(find_max_in_list(numList))

# FORMA MÁS SENCILLA
def find_max_in_list(list):
    if len(list) == 0:
        return None
    return max(list)
print(find_max_in_list(numList))


# FORMA USANDO TERNARIOS
def find_max_in_list(list):
    return max(list) if list else None
print(find_max_in_list(numList))

