f = open("d3.txt","r")

l = []

while True:
    line = f.readline()
    l.append(line[:-1])
    if not line:
        break
f.close()

l2 = []

for i in l[:-1]:
    st1 = set(i[:len(i)//2])

    st2 = set(i[len(i)//2:])
    
    l2.append(st1.intersection(st2).pop())
    
s = 0

for i in l2:
    if i.islower():
        s += ord(i)- 96
    if i.isupper():
        s+= ord(i) - 64 + 26

print(s)

l3 = []
s = 0
for i in range(0,len(l[:-1]),3):
    st3 = set(l[i]).intersection(set(l[i+1])).intersection(set(l[i+2]))    
    l3.append(st3.pop())
for i in l3:
    if i.islower():
        s += ord(i) - 96
    if i.isupper():
        s+= ord(i) - 64 + 26

print(s)