def check_permu(ori_str,chk_str):
    # return sorted(ori_str) == sorted(chk_str)
    # return set(ori_str) == set(chk_str)
    dict_permu = {}
    for i in ori_str:
        dict_permu[i]=0
        if i in chk_str:
            dict_permu[i]+=1  
    if 0 in dict_permu.values():
        return False
    return True

ori_str= input()
chk_str = input()
if check_permu(ori_str,chk_str):
    print("is permuation")
else:
    print("not permutation")