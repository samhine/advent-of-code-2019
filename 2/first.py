input_txt = [
    1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0
]

input_txt[1] = 12
input_txt[2] = 2

codep = 0
while input_txt[codep] != 99:
    if input_txt[codep] == 1:
        input_txt[input_txt[codep+3]] = input_txt[input_txt[codep+1]] + input_txt[input_txt[codep+2]]
    else:
        input_txt[input_txt[codep+3]] = input_txt[input_txt[codep+1]] * input_txt[input_txt[codep+2]]
    codep += 4

print(input_txt[0])