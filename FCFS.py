import datetime
from time import process_time
import time

#tarif pardazeh
t1_start = process_time()
def pardazeh():
     for m in range(100000):
          if m % 2 == 0 :
               temp = m / 2
          else:
                temp = m *2
          print(temp)

######################################################################
#ravesh daryaft vorudi tavasot file
with open ("est.txt", 'r') as file:
    file = [line.split() for line in file]
#######################################################################

#set tedad pardazeh
print("tedad pardazeh ha ra vared konid :")
n = input()
nn = int(n)
PI = [0]*nn
AT = [0]*nn
P =  [0]*nn
CT = [0]*nn

#set maghadir Arival time,beurst time,priority,processID
for i in range(nn):
     print("PID vared konid :")
     PI[i] = int(input())
     print("burst time vared konid :")
     CT[i] = int(input())
     print("Arival Time ra vared konid :")
     AT[i] = int(input())
     print("Pririty vared konid :")
     P[i] = int(input())

#be dalil in ke avalin vorudi az PI[0] bood az anja ejra shoru mishvad
t2_start = process_time()
for x in range(len(PI)):
      if AT[x] <= (time.time() % 100) : #bishtar yek rah hal mafhoomi na amali
         PI[x]= 'executed'
         pardazeh()
#######################################################################3
#ejra algorithm ba ekhtezaat kar ba file
for x in range(len(file)):
     file[x][0] = 'executed'
     pardazeh()
########################################################################
def sum(CT):
    ssum = 0
    for jj in range(len(CT) -1 ):
        ssum += CT[jj]
    return (ssum * (len(CT) / 2))


def summ(CT):
    ssum = 0
    for jj in range(len(CT)):
        ssum += CT[jj]
    return (ssum * (len(CT) / 2))

def summm(AT):
    ssum = 0
    for jj in range(len(AT)):
        ssum += AT[jj]
    return ssum

t3_stop = process_time()
mm= (t3_stop - t1_start)
mmm = (len(PI) / (t3_stop - t1_start))
mnm = len(PI)
AvW = (sum(CT) - summm(AT))  / len(CT)
AtT = (summ(CT) - summm(AT)) / len(CT)
print(" tedad pardazeh bararbar ast ba :" ,mnm )
print("kol zaman pardazesh barabar ast :" , mm)
print("the utilization time is : 100 %")
print(" the through put is : " , mmm)
print("miangin zaman entezar barabar ast ba : " , AvW)
print(" miangin turn around Time :" , AtT)
print(" miangin zaman pasokhghooyee :"  , AvW)








