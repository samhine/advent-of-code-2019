with open('input.txt', 'r') as f:
    inputtxt = [int(line.strip()) for line in f]

print(sum([int(i/3)-2 for i in inputtxt]))