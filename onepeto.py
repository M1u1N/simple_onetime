# without graphic

def one_peti(message:str,key:str):
    if len(message) <= len(key):
        m= message.encode()
        k= key.encode()
        liste= []
        for counter,i in enumerate(m):
            liste.append(i^k[counter])
        return bytes(liste).decode("utf-8")

def de_one_peti(c:str,key:str):
    k = key.encode()
    c = c.encode()
    liste = []
    for counter,i in enumerate(c):
        liste.append(i ^ k[counter])
    return bytes(liste).decode("utf-8")

ci=one_peti("hello","12345")
print(ci)
print(de_one_peti(ci,"12345"))
