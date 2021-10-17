from time import process_time
import time
t1_start = process_time()
##########################################################################
#ravesh daryaft vorudi tavasot file
with open ("est.txt", 'r') as file:
    file = [line.split() for line in file]
###########################################################################

#tarif oardazeh
def pardazeh():
     for m in range(100000):
          if m % 2 == 0 :
               temp = m / 2
          else:
                temp = m *2
          print(temp)

#yaftan kootah tarin pardazesh
def shortest(CT):
    min = 0
    for f in range(len(CT)):
        if CT[f] < CT[min]:
            min = f
    return min

#############################################################################################
#yaftan kootah tarin pardazeh az rooy adad mojud dar file
def Fshortest(file):
    mini = 0
    for ff in range(len(file)):
        if int(file[ff][1]) < int(file[mini][1]):
            mini = ff
        return mini
############################################################################################

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

t2_start = process_time()
#dar har marhale koochektarin burst tim ra mibad ejra mikonad va az saf kharej mikonad
for h in range(len(PI)):
    if AT[h] <= (time.time() % 100):  # bishtar yek rah hal mafhoomi na amali
       minimumID = 0
       minimumID = shortest(CT)
       CT[minimumID] = 99999999
       PI[minimumID] = 'Executed'
       pardazeh()

######################################################################################
#piyadeh sazi code asli bar asas ekhtezaat kar ba file
for yy in range(len(file)):
    minID = 0
    minID = Fshortest(file)
    file[minID][1] = 9999999
    file[minID][0] ='Excuted'
    pardazeh()
###########################################################################################
t3_stop = process_time()

def suum(CT):
    ssum = 0
    for jj in range(len(CT) -1 ):
        ssum = ssum + CT[jj]
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