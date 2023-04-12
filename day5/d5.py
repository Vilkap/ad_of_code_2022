f = open("txt5.txt","r")
l = []

while True:
    line = f.readline()
    l.append(line)
    if line == '\n':
        break
    if not line:
        break

l1 = []
for i in l[-3::-1]:
    count = 0
    for j in range(1,len(i),4):
        if i[j].isalpha():
            print(i[j])
            #if l1[count] == None:
            l1.insert(count,list())
            #l1[count].append(i[j])
            count += 1
print(l1)
    