import datetime
import time

with open ("est.txt", 'r') as file:
    map = [line.split() for line in file]
print(len(map[0]))
print(map[0][3])
nn = len(map)
mm = len(map[0])
ff =[[0]*mm]*nn
PI = [[0]*nn]
for i in range(nn):
    #PI[i] = int(map[i][0])
    for j in range(mm):
        ff[i][j] =int(map[i][j])
        print(map[i][j])
        print(ff[i][j])

#result = [map(int,i) for i in map1]
for kk in range(nn):
    print(kk)
    #PI[kk] =int(ff[kk][0])


print(map)
print(ff)
print(PI)
for at in range(1 , 10000):
    print(at)

print(time.time() % 100)