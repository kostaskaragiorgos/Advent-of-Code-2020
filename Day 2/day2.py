passw = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

for i in passw:
    print(i[0],i[2:4],i[4:6],i[7:-1])



def isval(minim, maxim,char, passw):
    charcounter = 0
    for i in passw:
        if i == char:
            charcounter +=1
    if charcounter >= int(minim) and charcounter <= int(maxim):
        return 1
    else:
        return 0
    
    
def isval2(index1 , index2, char, passw):
    lower = passw[index1-1] == char 
    higher = passw[index2-1] == char
    if lower != higher:
        return 1
    else:
        return 0
nfval =0
nfval2 = 0


passin = []
with open("Day 2/day2.txt", 'r') as f:
    for line in f:
        counts, char, password = line.strip().split()
        minim , maxim = [int(n) for n in counts.split("-")]
        char = char[0]
        passin.append([minim,maxim, char, password])

for i in passin:
    nfval2 += isval2(i[0],i[1],i[2],i[3])
    nfval += isval(i[0],i[1],i[2],i[3])

print(nfval)
print(nfval2)
