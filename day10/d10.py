f = open("d10.txt","r")

l = []
while True:
    line = f.readline()
    l.append(line[:4])
    if len(line) > 5:
        l.append(line[5:])
    if not line:
        break
f.close()
l.pop()
sch = 1
summ = 1
summ2 = 0
for ind,_ in enumerate(l):
    if sch in [20,60,100,140,180,220]:
        summ2 += sch*summ
    sch += 1
    if l[ind][0].isalpha() == False:
        summ+=int(l[ind])
print(summ2)


for ind,_ in enumerate(l):
    