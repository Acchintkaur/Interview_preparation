def str_rotation(org,rot):
    if len(org) != len(rot):
        return False
    s = rot+rot
    if org in s:
        return True
    return False
org = input()
rot = input()
print(str_rotation(org,rot))