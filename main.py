from collections import Counter
s=[12,23,34,45,56,65,54,43,32,21,13,15,17,71,51,31,31,34,34,34,31,31]


def mean(s):
    return int((sum(s))/len(s))

def median(s):
    s.sort()
    if(len(s)%2==0):
        return ((s[len(s)//2]+s[(len(s)+1)//2])/2)
    else:
        return (s[len(s)//2])


def mode(s):
    count = Counter(s)
    max1 = max(count.values())
    mod_elems = [key for key, value in count.items() if value == max1]    
    return mod_elems



print(mean(s))
print(median(s))
print(mode(s))