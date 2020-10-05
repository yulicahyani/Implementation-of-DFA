# DFA L1
#mendeklarasikan delta untuk L1
deltaL1 = {'q0':{'0':'q0', '1':'q1'},
           'q1':{'0':'q2', '1':'q1'},
           'q2':{'0':'q0', '1':'q3'},
           'q3':{'0':'q3', '1':'q3'}}

#fungsi untuk 'Extension of the Transition Function for DFA'
def deltatopiL1(transisi,initial,finalstate,s):
    state = initial
    i = len(s)
    j = 1
    k = 1

    print('\ndeltop(q0',',',s,')\n')

    #untuk menampilkan fungsi deltatopi
    for c in s:
        if k == i:
            print('=', k, 'delta ( deltop ( q0, e )', s[(i - k):i], ')')
        else:
            print('=', k, 'delta ( deltop ( q0,', s[0:(i - k)], ')', s[(i - k):i], ')')
        k+=1

    #Transition Function
    for c in s:
        try:
            print('=',(i+1)-j,'delta (', state, ',', c, ')', s[j:i])
            state = transisi[state][c]
            j+=1
        except KeyError:
            return False

    print('=',state)
    return state in finalstate

#validasi string inputan (Output program)
def validL1(string):
    validasi = 'Diterima' if deltatopiL1(deltaL1, 'q0', {'q3'}, string) else 'Ditolak'
    print('\n' + string, '->', validasi)

# Menginputkan string
def inputstr():
    print('\nInputan harus terdiri atas 0 atau 1')
    stringL1 = input('Masukan string >> ')
    cekinput(stringL1)

#cek inputan
def cekinput(str):
    l = 0
    for c in str:
        if c == '0' or c == '1':
            l+=1
        else:
            l=0

    if l == len(str):
        validL1(str)
    else:
        print('Inputan Salah!!!. Silahkan masukan string kembali!!')
        inputstr()


print("===================================================================")
print("==                           DFA L1                              ==")
print("== L1 adalah himpunan semua string yang mengandung substring 101 ==")
print("===================================================================")

inputstr()

#DFA L5
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
