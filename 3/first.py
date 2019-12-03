with open('input.txt', 'r') as f:
    inputtxt = [line.strip() for line in f]
    wire1 = inputtxt[0].split(",")
    wire2 = inputtxt[1].split(",")

x=0
y=0

wire_set_1 = []
wire_set_2 = []

for intr in wire1:
    if intr[0]=="U": [wire_set_1.append((x,y+p)) for p in range(1,int(intr[1:])+1)]
    elif intr[0]=="D": [wire_set_1.append((x,y-p)) for p in range(1,int(intr[1:])+1)]
    elif intr[0]=="L": [wire_set_1.append((x-p,y)) for p in range(1,int(intr[1:])+1)]
    elif intr[0]=="R": [wire_set_1.append((x+p,y)) for p in range(1,int(intr[1:])+1)]
    x, y = wire_set_1[-1]


x=0
y=0

for intr in wire2:
    if intr[0]=="U": [wire_set_2.append((x,y+p)) for p in range(1,int(intr[1:])+1)]
    elif intr[0]=="D": [wire_set_2.append((x,y-p)) for p in range(1,int(intr[1:])+1)]
    elif intr[0]=="L": [wire_set_2.append((x-p,y)) for p in range(1,int(intr[1:])+1)]
    elif intr[0]=="R": [wire_set_2.append((x+p,y)) for p in range(1,int(intr[1:])+1)]
    x, y = wire_set_2[-1]


min_v = 1000000000000
intersec = list(set(wire_set_1) & set(wire_set_2))

for v in intersec:
    if min_v > abs(v[0]) + abs(v[1]): 
        min_v = abs(v[0]) + abs(v[1])
        print(v)

print(min_v)

