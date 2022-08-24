def palindromic_permutation(ipt,n):
    dict_count={}
    for i in ipt[:n//2]+ipt[n//2+1:]:
        dict_count[i] =0
    for i in ipt[:n//2]+ipt[n//2+1:]:
        dict_count[i] +=1
    # print(dict_count)
    for i in dict_count.values():
        if i%2 !=0:
            return False
    return True
ipt = ''.join(input().split())
print(palindromic_permutation(ipt,len(ipt)))