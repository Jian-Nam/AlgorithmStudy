N =  int(input())
P = []
for i in range(N):
    row = list(map(int, input().split(" ")))
    P.append(row)
# print(P)

def isOneColor(l):
    color = l[0][0]
    for i in l:
        for j in i:
            if j != color:
                return False
    return True

# print(isOneColor(P))
def devideAndConquer(l):
    count = [0 , 0]
    if isOneColor(l) == False:
        half = len(l)//2
        ul = []
        ur = []
        dl = []
        dr = []

        up = l[:half]
        down = l[half:]

        for u in up:
            ul.append(u[:half])
            ur.append(u[half:])

        for d in down:
            dl.append(d[:half])
            dr.append(d[half:])

        # print(ul)
        # print(ur)
        # print(dl)
        # print(dr)
        r1 = devideAndConquer(ul)
        r2 = devideAndConquer(ur)
        r3 = devideAndConquer(dl)
        r4 = devideAndConquer(dr)

        count[0] += r1[0] + r2[0] + r3[0] + r4[0]
        count[1] += r1[1] + r2[1] + r3[1] + r4[1]
    else:
        count[l[0][0]] += 1
    return count

result = devideAndConquer(P)
print (result[0])
print (result[1])
        
