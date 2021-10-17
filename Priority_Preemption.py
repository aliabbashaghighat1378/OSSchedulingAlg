from time import process_time
import time
import math
#################################################################
#ravesh daryaft vorudi tavasot file
t1_start = process_time()
with open ("est.txt", 'r') as file:
    file = [line.split() for line in file]
FNE = [[-100]*(len(file))]
###############################################################
#tarif oardazeh
def pardazeh():
     for m in range(100000):
          if m % 2 == 0 :
               temp = m / 2
          else:
                temp = m *2
          print(temp)

#yaftan bihtarin priority
def bigest(P , NE , ff):
    max = 0
    for f in range(len(P)):
        if NE[f] != ff:
            if P[f] > P[max]:
                 max = f
            return max

###############################################################################
#yaftan bishtarin priority baray file
def Fbigest(file , FNE , ff):
    maxf = 0
    for qq in range(len(file)):
        #if FNE[qq] != ff:
            if int(file[qq][3]) > int(file[maxf][3]):
                 maxf = qq
            return maxf
#################################################################################

#to find which process takes most time
def longest(CT):
    maxi = 0
    for f in range(len(CT)):
        if CT[f] > CT[maxi]:
            maxi = f
    return CT[maxi]
#######################################################################
#to find which process takes most time for file datas
def Flongest(file):
    maxif = 0
    for qq in range(len(file)):
         if int(file[qq][1]) > int(file[maxif][1]):
             maxif = qq
    return int(file[maxif][1])
########################################################################

#set tedad pardazeh
print("tedad pardazeh ha ra vared konid :")
n = input()
nn = int(n)
PI = [0]*nn
AT = [0]*nn
P =  [0]*nn
CT = [0]*nn
NE = [0]*nn
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
     print("Number of execution for all at first is -100 ")
     NE[i] = -100

#yaftan tedad dor hay mored niaz baray in ke kole process ha ejra shavand

tedadEjra = int(math.ceil(longest(CT) / 2))

t2_start = process_time()
for ff in range(1 , tedadEjra+1):
    #tarif moteghayyer temp baray hefz maghadir asli
    TAT = AT
    TP = P
    TCT = CT
    TPI = PI
    for mm in range(len(PI)):
        if AT[mm] <= (time.time() % 100):  # bishtar yek rah hal mafhoomi na amali
            maximumID = bigest(TP , NE , ff)
            TP[maximumID] = -99999999
            NE[maximumID] = ff
            if (TCT[maximumID] - (ff * 2)) <= 0 :
                 P[maximumID] = -9999999
                 PI[maximumID] = 'Executed'
                 pardazeh()
##################################################################################
#yaftan tedad dor hay mored niaz baray in ke kole process ha ejra shavand

FtedadEjra = int(math.ceil(Flongest(file) / 2))
#piyadeh sazi algorithm asli ba ekhtezaat kar ba file
for ff in range(1 , FtedadEjra+1):
    #tarif moteghayyer temp baray hefz maghadir asli
    nn = len(file)
    mm = len(file[0])
    tf = [[0] * mm] * nn
    for i in range(nn):
        for j in range(mm):
            tf[i][j] = int(file[i][j])
            print(file[i][j])
            print(tf[i][j])

    for mm in range(len(file)):
        FmaximumID = Fbigest(file , FNE , ff)
        tf[FmaximumID][3] = -99999999
        FNE[FmaximumID] = ff
        if (int(tf[maximumID][1]) - (ff * 2)) <= 0 :
             file[maximumID][3] = -9999999
             file[maximumID][0] = 'Executed'
             pardazeh()
#############################################################################################

t3_stop = process_time()

def sum(CT):
    ssum = 0
    for jj in range(len(CT)  ):
        ssum += CT[jj]
    return ((ssum * (len(CT) / 2)) -2 )


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

