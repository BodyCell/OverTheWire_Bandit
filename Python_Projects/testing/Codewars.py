# numbers = [1, 2, 3, 1, 1]


# print(min(numbers))

# numbers.remove(min(numbers))

# print(numbers)
# import numpy as np

# a = np.arange(100)
# b = a[50:60:2]

# print(a)

# print(b)



# def solution(args):
#     out = []
#     beg = end = args[0]
    
#     for n in args[1:]+['']:
#         if n != end + 1:
#             if end == beg:
#                 out.append( str(beg) )
#             elif end == beg + 1:
#                 out.extend( [str(beg), str(end)] )
#             else:
#                 out.append( str(beg) + "-" + str(end) )   
#             beg = n
#         end = n
    
#     return ",".join(out)



# print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"


# --------------------------------------------------- Caluclating With Functions --------------------------------------------------- #
# def zero(func=None): 
#     return func(0) if func else 0 

# def nine(func = None): #your code here
#     return func(9) if func else 9

# def plus(y): #your code here
#     return lambda x: y+x
#     # return lambda x: x +y


# print(nine(plus(zero())))

# --------------------------------------------------- Shortest Word --------------------------------------------------- #



# def find_short(s = str):
#     s_list = s.split(" ")
#     l = len(s_list[0])

#     for x in range(len(s_list)):
#         if len(s_list[x]) < l:
#             l = len(s_list[x])
#     return l


# print(find_short("Let's travel abroad shall we"))



# --------------------------------------------------- Find the unique number --------------------------------------------------- #

# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

#     Find the unique number (this kata)
#     Find the unique string
#     Find The Unique

# \/\/\/ SOLUTION WRITTEN BELOW \/\/\/

# def find_uniq(arr=list):
#     s = list(set(arr))
#     return s[0] if arr.count(s[0]) == 1 else s[1]



# print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))

# --------------------------------------------------- Rot13 --------------------------------------------------- #


def rot13(message):
    letters_low = 'abcdefghijklmnopqrstuvwxyz'
    letters_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def in_list(char,list):
        return char in list
    
    code=""

    for x in message:
        if in_list(x,letters_low):
            code += letters_low[letters_low.index(x)+13] if letters_low.index(x) < 12 else letters_low[letters_low.index(x)-13]
        elif in_list(x,letters_up):
            code += letters_up[letters_up.index(x)+13] if letters_up.index(x) < 12 else letters_up[letters_up.index(x)-13]
        else: code+=x
    return code


print(rot13('test'))

# letters_low = 'abcdefghijklmnopqrstuvwxyz'
# letters_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# print(letters_low[letters_up.index('M')+13])