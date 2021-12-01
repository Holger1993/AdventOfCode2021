# Advent of Code 1, 2021

def count_increase(data):
    count = 0
    for dept in range(1,len(data)):
        if data[dept] > data[dept - 1]:
            count += 1
    return count

def count_increase_three(data):
    count = 0
    for dept in range(len(data)-2):
        first_sum = sum(data[dept:dept+3])
        second_sum =  sum(data[dept+1:dept+4])
        if second_sum > first_sum:
            count += 1
    return count


AOC1data = []
with open('PuzzleInputs/AOC1.txt') as f:
    lines = f.readlines()
for line in lines:
    AOC1data.append(int(line.strip()))


print(count_increase(AOC1data))

print(count_increase_three(AOC1data))