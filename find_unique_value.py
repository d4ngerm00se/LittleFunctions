def find_uniq(arr):
    count_dict = {}
    lst = []
    # Count the occurrences of each value in the list
    for x in arr:
        count_dict[x] = count_dict.get(x, 0) + 1
    # Find the value that appears only once
    for x in count_dict:
        if count_dict[x] == 1:
            lst.append(x)
    return lst
        
y = [0, 2, 0, 5, 5, 0, 4]

print("The unique value in your list is: ", find_uniq(y))

#First attempt was too slow:
# def find_uniq(arr):
#     lst = []
#     for x in arr:
#         count = arr.count(x)
#         if count == 1:
#             lst.append(x)
#     return lst

# y = [0, 2, 0, 5, 5, 0, 4]

# print("The unique value in your list is: ", find_uniq(y))