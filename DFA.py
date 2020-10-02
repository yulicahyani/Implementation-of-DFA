#delta topi L5

def deltop5(Q, ZigBin):
    if Q==0 and ZigBin==0:
        return 0
    else:
        ZigBin = ZigBin - 1
        return delta5(deltop5(Q, ZigBin), str[ZigBin])

#delta L5
def delta5(Q, Zigma):
    if Q==0 and Zigma=='0':
        return 0
    elif Q==0 and Zigma=='1':
        return 1
    elif Q==1 and Zigma=='0':
        return 1
    elif Q==1 and Zigma=='1':
        return 0

#Validation String L5
def valid5(valid):
    if valid==1:
        print('String Diterima')
    else:
        print('String Ditolak')

#input
str = input('Enter a String: ')

#Menghitung panjang string
ZigBin = len(str)

#output
valid5(deltop5(0,ZigBin))
