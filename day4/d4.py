f = open("txt4.txt","r")

l = []

while True:
    line = f.readline()
    l.append(line[:])
    if not line:
        break
f.close()
s = 0
s1 = 0
for i in l[:-1]:
    pair = i.split(',')
    fs = int(pair[0].split('-')[0])
    fe = int(pair[0].split('-')[1])
    ls = int(pair[1].split('-')[0])
    le = int(pair[1].split('-')[1])
    
    if fs >= ls and fe <= le:
        s+=1
    elif fs <= ls and le <= fe:
        s+=1
        
    if fe < ls or fs > le:
        continue
    else:
        s1+=1
    
    #if (fs >= ls and fs <= le) or (ls >= fs and ls <= fe):
     #   s1+=1
print(s)
print(s1)
        