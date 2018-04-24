#Write and test a recursive function max to find the largest number in a list. The max is the
#larger of the first item and the max of all the other items.

def Max(list):

    if len(list) == 1:
        return list[0]

    else:
        return max(list[0],max(list[1:]))


lista=[11,23,31]
print(max(lista))