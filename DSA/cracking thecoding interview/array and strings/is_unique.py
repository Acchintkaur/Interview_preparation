ip_str = input()

# -------------Method 1 -----------------
if len(set(ip_str)) == len(ip_str):
    print("All are unique")
else:
    print("Contains Duplicates")
# -------------Method 2 -----------------
c=0
for i in range(len(ip_str)):
    if ip_str[i] in ip_str[i+1:]:
        print("Contains Duplicates")
        c+=1
        break
if c==0:
    print("All elemets are unique")