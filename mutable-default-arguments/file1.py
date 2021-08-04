def createList_and_append_1(aList=[]):
    aList.append(1)
    return aList


list_1 = createList_and_append_1()
print(list_1)

list_2 = createList_and_append_1()
print(list_2)  # WHAT? Why would it print [1, 1]?


def createList_None(aList=None):
    if aList is None:
        aList = []
        aList.append(1)
    return aList


list_3 = createList_None()
print(list_3)

list_4 = createList_None()
# WHAT? Nice! aList is created each time the function is called this way.
print(list_4)
