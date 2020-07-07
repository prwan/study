Fn = int(input("시작숫자:"))
Sn = int(input("끝숫자:"))

def FIND(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False

    return True

for a in range(Fn+1,Sn):
    if FIND(a) and str(a) == str(a)[::-1]:
        print(a,end=" ")


