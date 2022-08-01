# s = "hello world welcome to python world"
# words = s.split()
# print(words)
#
# d={}
# for word in words:
#     d[word] = len(word)
#
# print(d)
#
# sorted_item = sorted(d.keys())
# print(sorted_item)
#
# sorted_value = sorted(d.values())
# print(sorted_value)

# for row in range(6):
#     print("* "*row)

# for row in range(6,0,-1):
#     print("* "*row)

# for row in range(6):
#     print(f"{'* '*row:>12}")

# for row in range(6,0,-1):
#     print(f"{'* '*row:>12}")

# for row in range(6):
#     print(f"{'* '*row:^12}")

# for row in range(6,0,-1):
#     print(f"{'* '*row:^12}")

# for i in range(0,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

# for row in range(1,6):
#     print("*")
#     print("* "*row)

# for i in range(6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print()

# from random import random
#
# for _ in range(0,2):
#     print(random())

# pat = ""
# for i in range(1,6):
#     pat = pat +str(i) +""
#     print(pat)

# pat = ""
# for i in range(1,6):
#     pat = pat + str(i) + " "
#     print(f"{pat:>12}")

# for row in range(6,0,-1):
#     print(f"{'*'*row:>12}")

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(chr(64+j), end=" ")
#     print()

#print(ord('c'))
#
# for i in range(1,6):
#     for j in range(1, i+1):
#         if i+j == 6:
#             print("*",end=" ")
#         else:
#             print(j,end=" ")
#     print()

# s = "Hello how are you i am vivek and you are also a good man"
# words = s.split()
# print(words)

count = 0
# for word in words:
#     count+= 1
#
# print(count)
#
# l = {}
# for word in words:
#     l[word] = len(word)
#
# print(l)
#
# dict_comp = { word:len(word) for word in words }
# print(dict_comp)

# count = 0
# for word in words:
#     if words.count(word)>1:
#         count += 1
#
#
# print(count)

# from collections import defaultdict
#
# dd = defaultdict(int)
# for word in words:
#     dd[word] +=1
#
# print(dd)

# from time import sleep
# def log(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
# @log
# def add(a,b):
#     sleep(2)
#     return a+b
#
# @log
# def sub(a,b):
#     sleep(3)
#     return a-b
#
# print(add(45,89))
# print(sub(87,96))


# from time import sleep, time
#
# def exe_time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end =time()
#         print(f"Execution time: {end - start} seconds")
#         return result
#     return wrapper
#
# @exe_time
# def add(a, b):
#     sleep(5)
#     return a+b
#
# @exe_time
# def sub(a, b):
#     sleep(3)
#     return a-b
#
# print(add(5,6))
#print(sub(4,3))

# _add = lambda a,b:a+b
# print(_add(78,98))

# _mul = lambda a, b, c: a*b*c
# print(_mul(5,6,7))

# greet = lambda name: f"Hello {name}"
# print(greet("vivek"))

# s_sorted = sorted(words, key=lambda item:item[-1])
# print(s_sorted)

# s_sorted = sorted(words, key=len)
# print(s_sorted)

# sentence = "this is a programming language and programming is very fun"
# words = sentence.split()
# print(words)

# d = { word:len(word) for word in words }
# print(d)
#
# s_sorted = sorted(d.items() ,key= lambda item:item[-1])
# print(s_sorted)
# print(s_sorted[-1])

# l = []
# for word in words:
#     if len(word) >5:
#         l.append(word)
#
# print(l)

l = []
l.append(25)
l.append(65)
l.append(89)
l.append(41)
print(l)

string ="vivek"
res = ""
for word in string:
    res = word +res

print(res)

# def is_Palindrome(string):
#     if string == string[::-1]:
#         return f"{string} is  pallindrome"
#     return f"{string} is not pallindrome"
#
# rs=is_Palindrome("mada")
# print(rs)