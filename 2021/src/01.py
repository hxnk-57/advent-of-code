file_path = r"2021\input\01.txt"

depths = [int]

with open(file_path, 'r') as file:    
    depths = [int(line) for line in file]

def part_one() -> int:
    return sum(1 for current_depth, next_depth in zip(depths, depths[1:]) if current_depth < next_depth)

def part_two() -> int:
    return sum(1 for i in range(len(depths) - 3) if sum(depths[i:i+3]) < sum(depths[i+1:i+4]))

print(f"Part one:", part_one())
print(f"Part Two:", part_two())