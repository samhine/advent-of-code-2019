with open('input.txt', 'r') as f:
    inputtxt = [int(line.strip()) for line in f]

s = 0
for module in inputtxt:
    fuel = module
    while int(fuel/3)-2>0:
        n_fuel = int(fuel/3)-2
        s += n_fuel
        fuel = n_fuel

print(s)