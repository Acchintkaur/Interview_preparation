def get_powerset(fullset):
    listrep = list(fullset)
    powerset = []
    for i in range(2**len(listrep)):
        subset = []
        for k in range(len(listrep)):
            if i & 1<<k:
                subset.append(listrep[k])
        powerset.append(subset)    
    return powerset
powerset = get_powerset(set([1,2,3]))
print(powerset)
print(len(powerset))