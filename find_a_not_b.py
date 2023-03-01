def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff([0, 5, 3, 7], [0, 4, 3]))

# def array_diff(a, b):
#     newlist = []
#     for x in a:
#         if x not in b:
#             newlist.append(x)
#     return newlist