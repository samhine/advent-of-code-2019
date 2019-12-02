with open('input.txt', 'r') as f:
    inputtxt = [int(line.strip()) for line in f]

def f(m):
    if (int(m/3)-2<0): return m
    else: return f(int(m/3)-2)+m

print(sum([f(module)-module for module in inputtxt]))
