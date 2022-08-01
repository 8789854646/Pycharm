# for num in range(1,100):
#     if num>1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#         else:
#             print(num)



def is_Prime(num):
    if num>1:
        for i in range(2, num):
           if num%i == 0:
               print("Not Prime no")
               break
        else:
            print("Prime No")

is_Prime(22)