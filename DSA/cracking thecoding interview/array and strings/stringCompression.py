# # if we want count of element in whole string
# # eg: aabcccccaa ----> a4b1c5
# def compression(str):
#     dict_str={}
#     res=[]
#     for i in str:
#         if i in dict_str:
#             dict_str[i]+=1
#         else:
#             dict_str[i]=1

#     for i in dict_str:
#         res.append(i)
#         val="{}".format(dict_str[i])
#         res.append(val)
#     return ''.join(res)
# n= input()
# print(compression(n))

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# if we want aabcccccaaa ----> a2blc5a3
def compression(n):
    count=0
    res=''
    for i in range(len(n)):
        count+=1
        if (i+1)>=len(n) or n[i]!=n[i+1]:
            res+= n[i]+str(count)
            count=0
    return res
n= input()
print(compression(n))