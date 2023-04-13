f = open("d1.txt","r")
l = []
l2 = []
while True:
    line = f.readline()
    if not line:
        break
    if line != '\n':
        l.append(int(line))
    else:
        l2.append(sum(l))
        l = []
f.close()
print(max(l2))
l2.sort(reverse = True)
print(sum(l2[:3]))