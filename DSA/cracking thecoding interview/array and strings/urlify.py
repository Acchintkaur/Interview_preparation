# # -----------Method 1------------------
# n = input()
# ipt = n.split()
# opt = '%20'.join(ipt)
# print(opt)
# # ----------------Method 2----------------
# print(input("Enter the string to urlify").replace(' ','%20'))
# ------------------Method 3--------------
n=input()
res = ''
for i in range(len(n)):
    if n[i]== ' ':
        res+='%20'
    else:
        res+=n[i]
print(res)