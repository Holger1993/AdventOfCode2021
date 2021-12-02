def aoc21(data):
    forward = 0
    down = 0
    up = 0
    for dat in data:
        if dat[:dat.index(' ')] == 'forward':
            forward += int(dat[dat.index(' ')+1:])
        if dat[:dat.index(' ')] == 'down':
            down += int(dat[dat.index(' ')+1:])
        if dat[:dat.index(' ')] == 'up':
            up += int(dat[dat.index(' ')+1:])      
    return forward * (down - up)

def aoc22(data):
    forward = 0
    depth = 0
    aim = 0
    for dat in data:
        if dat[:dat.index(' ')] == 'forward':
            forward += int(dat[dat.index(' ')+1:])
            depth += aim * int(dat[dat.index(' ')+1:])
        if dat[:dat.index(' ')] == 'down':
            aim += int(dat[dat.index(' ')+1:])
        if dat[:dat.index(' ')] == 'up':
            aim -= int(dat[dat.index(' ')+1:])   
    return forward * depth

AOC2data = []
with open('PuzzleInputs/AOC2.txt') as f:
    lines = f.readlines()
for line in lines:
    AOC2data.append(line.strip())

print(aoc21(AOC2data))
print(aoc22(AOC2data))