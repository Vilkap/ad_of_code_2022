f = open("d6.txt","r")

s = ""

while True:
    line = f.readline()
    s += line
    if not line:
        break
f.close()

s1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
l = []
for i in range(len(s)):
    l.append(s[i])
    l.append(s[i + 1])
    l.append(s[i + 2])
    l.append(s[i + 3])
    set1 = set(l)
    if len(set1) == 4:
        print(i + 4)
        break
    else:
        l = []
        set1 = set()
    

l1 = []

for i in range(len(s)):
    for j  in range(i , i + 14 ):
        l.append(s[j])
    set1 = set(l)
    if len(set1) == 14:
        print(i + 14)
        break
    else:
        l = []
        set1 = set()