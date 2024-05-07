# Boyer-moore is appropriate since we only have two candidates and we know there is a majority candidate
def boyer_moore(numbers: list[int]) -> str:
    candidate, count = None, 0

    for number in numbers:
        if count == 0:
            candidate = number
            count = 1
        elif number == candidate:
            count += 1
        else:
            count -= 1

    return candidate

with open("data.txt", "r") as file:
    content = [line.strip() for line in file]

# transposing rows and columns of the orginal 2D list
columns = list(map(list, zip(*content)))

gamma_rate = "".join((boyer_moore(column) for column in columns))
epsilon_rate = "".join("1" if bit == "0" else "0" for bit in gamma_rate)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# part two

def majority(numbers: list[int]) -> int:
    zeros = numbers.count(0)
    ones = numbers.count(1)
    return 1 if ones >= zeros else 0

def minority(numbers: list[int]) -> int:
    zeros = numbers.count(0)
    ones = numbers.count(1)
    return 0 if ones >= zeros else 1

def find_candidate(content: list[list[int]], function) -> int:
    candidates = content.copy()
    for i in range(len(candidates[0])):
        candidate_column = [row[i] for row in candidates]
        major_element = function(candidate_column)
        co2_candidates = [candidate for candidate in candidates if candidate[i] == major_element]
        candidates = co2_candidates.copy()
        if len(co2_candidates) == 1:
            break
    # return int("".join(map(str, co2_candidates[0])), 2)
    return int("".join(map(str, co2_candidates[0])), 2)

with open("data.txt", "r") as file:
    content = [[int(bit) for bit in line.strip()] for line in file]

print(content)

oxygen_rating = find_candidate(content, majority)
co2_rating = find_candidate(content, minority)

print(oxygen_rating * co2_rating)