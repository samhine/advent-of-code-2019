c = 0
for n in range(264793, 803935+1):
    sn = str(n)
    if sn[0]<=sn[1] and sn[1]<=sn[2] and sn[2]<=sn[3] and sn[3]<=sn[4] and sn[4]<=sn[5]:
        print(sn)
        if sn[0]==sn[1] or sn[1]==sn[2] or sn[2]==sn[3] or sn[3]==sn[4] or sn[4]==sn[5]:
            c+=1

print(c)