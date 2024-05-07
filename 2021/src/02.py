file_path = r"2021\input\02.txt"

directions = [str]

with open(file_path, 'r') as file:    
    directions = [line for line in file]

def part_one() -> int:
    horizontal_position: int = 0
    depth: int = 0
    for direction in directions:
        action, value = direction.split()
        value = int(value)
        if 'forward' in action:
            horizontal_position += value
        elif 'down' in action:
            depth += value
        else:
            depth -= value
    return depth * horizontal_position

def part_two() -> int:
    horizontal_position: int = 0
    depth: int = 0
    aim: int = 0
    for direction in directions:
        action, value = direction.split()
        value = int(value)
        if 'forward' in action:
            horizontal_position += value
            depth += aim * value
        elif 'down' in action:
            aim += value
        else:
            aim -= value
    return depth * horizontal_position
    
print(part_one())
print(part_two())