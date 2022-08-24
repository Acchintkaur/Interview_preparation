def oneAway(f,s):
    if len(f)-len(s)<=1:
        if len(f)>=len(s):
            c=0
            for i in f:
                if i not in s:
                    c+=1
            return True if c==1 else False
        elif len(f)<len(s):
            c=0
            for i in s:
                if i not in f:
                    c+=1
            return True if c==1 else False

        else:
            return False
    else: 
        return False
first = sorted(input())
second = sorted(input())
print(oneAway(first,second))
