# from itertools import permutations

# my_list = [1,2,3,4]

# list_of_permutations = permutations(my_list)
# for permutation in list_of_permutations:
#     print(permutation)



# from itertools import permutations

# my_list = [1,2,3,4,5,6,7]

# list_of_permutations = permutations(my_list)
# cnt = 0
# for permutation in list_of_permutations:
#     cnt += 1
# print (len(my_list), cnt)


# def faculty(n):
#     if n <= 1:
#         return n
#     else:
#         return faculty(n-1)*n

# for i in range(10):
#     print(faculty(i))

# import cProfile

# def faculty(n):
#     if n <= 1:
#         return n
#     else:
#         return faculty(n-1)*n

# def counter(n):
#     cnt = 0
#     for i in range(n):
#         cnt+=1
#     return cnt

# cProfile.run("counter(faculty(12))")



import cProfile

def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n-20)*n
def counter(n):
    cnt = 0
    for i in range(n):
        cnt+=1
    return cnt

cProfile.run("counter(faculty(10))")