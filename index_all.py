'''
Author Notes:
It took more time than expected to finish this challenge. It was very valuable, nonetheless, because it helped me with the comprehension on how recursion works.
It also helped me to realize how important is the ability of mentally going step by step through the code.
'''
def index_all(user_list,elem):
    result = []
    subpaths = []
    for i,item in enumerate(user_list):
        if isinstance(item,list):
            subpaths = index_all(item,elem)
            for path in subpaths:
                result.append([i] + path)
        elif item == elem:
                result.append([i])
    return result

# Please, uncomment the lines below to execute the code with the example given

# myList = [[[1,2,3],2,[1,3]],2,[1,2,3]]
# print(index_all(myList, 2))
