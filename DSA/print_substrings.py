# def subString(s, n):
#     for i in range(n):
#         for len in range(i+1,n+1):
#             print(s[i: len])
def subString(s, n):
 
    # Fix start index in outer loop.
    # Reveal new character in inner loop till end of string.
    # Print till-now-formed string.
    for i in range(n):
        temp=""
        for j in range(i,n):
            temp+=s[j]
            print(temp)
# Driver program to test above function
s = "abcd"
subString(s,len(s))