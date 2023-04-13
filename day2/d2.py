f = open("d2.txt","r")
l = []
while True:
    line = f.readline()
    if not line:
        break
    l.append(line[:3:2])

s = 0
s1 = 0
for i in l:
    if i[0] == "A" and i[1] == "X":
        s += 1 + 3
    if i[0] == "B" and i[1] == "X":
        s += 1 + 0
    if i[0] == "C" and i[1] == "X":
        s += 1 + 6
        
    if i[0] == "A" and i[1] == "Y":
        s += 2 + 6
    if i[0] == "B" and i[1] == "Y":
        s += 2 + 3
    if i[0] == "C" and i[1] == "Y":
        s += 2 + 0
        
    if i[0] == "A" and i[1] == "Z":
        s += 3 + 0
    if i[0] == "B" and i[1] == "Z":
        s += 3 + 6
    if i[0] == "C" and i[1] == "Z":
       s += 3 + 3
        
print(s)

for i in l:
    if i[0] == "A" and i[1] == "X":
        s1 += 3 + 0
    if i[0] == "B" and i[1] == "X":
        s1 += 1 + 0
    if i[0] == "C" and i[1] == "X":
        s1 += 2 + 0
        
    if i[0] == "A" and i[1] == "Y":
        s1 += 1 + 3
    if i[0] == "B" and i[1] == "Y":
        s1 += 2 + 3
    if i[0] == "C" and i[1] == "Y":
        s1 += 3 + 3
        
    if i[0] == "A" and i[1] == "Z":
        s1 += 2 + 6
    if i[0] == "B" and i[1] == "Z":
        s1 += 3 + 6
    if i[0] == "C" and i[1] == "Z":
        s1 += 1 + 6
        
print(s1)