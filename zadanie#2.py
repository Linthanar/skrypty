charList = {"a", "b", "c", "d"}

alfb = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alfs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def Hard_to_code(char,A,a):
    rchar =[]
    for i in range(len(char)):
        # print(i)
        rchar.append(alfb[i])
    return rchar

print(Hard_to_code(charList,alfs,alfb))

def toCaps(chars):
    for l in chars:
        print(l.upper())

print(toCaps(charList))