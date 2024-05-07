
with open('data2.txt', 'r') as file:
    lines = [line.strip() for line in file]

numbers = lines[0].split(',')


boards = []
for i in range(0, len(lines) - 1, 6):
    boards.append(lines[i+2:i+7])

def calculate_score(winning_board, winning_numbers):
    print("Winning numbers:", winning_numbers)
    print("Winning Board:\n")    
    total = 0
    for row in winning_board:
        print(row)
        numbers = row.split()
        for n in numbers:
            if n not in winning_numbers:
                total += int(n)
    return total * int(winning_numbers[-1])


def transpose_board(board):
    return [' '.join(row).split() for row in zip(*board)]


def bingo(board: list[int], winning_numbers: list[int]) -> bool:
    # row check
    for i in range(0, 5):
        count = 0
        row = board[i].split(" ")
        for n in winning_numbers:
            if n in row:
                count += 1
            if count == 5:
                print(calculate_score(board, winning_numbers[:winning_numbers.index(n)+1]))
                return True
    # column check
    # Transpose the board so that columns become rows
    transposed_board = transpose_board(board)
    
    # Column check
    for i in range(0, 5):
        count = 0
        column = transposed_board[i]
        for n in winning_numbers:
            if str(n) in column:
                count += 1
            if count == 5:
                return True

    return False
           
def part_one():
    number_index = 1
    while True:
        for current_board in boards:
            if bingo(current_board, numbers[:number_index]):
                break
        else:
            number_index += 1
            continue
        break

def part_two():


    return
    