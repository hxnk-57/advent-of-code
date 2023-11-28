policies =[]

with open(r"2020\2\input.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        policies.append(line)
    
valid_passwords = 0

for policy in policies:
    #use regex to find these instead. TODO
    min = int(policy[:policy.find("-")])
    max = int(policy[policy.find("-")+1:policy.find(" ")])
    letter = policy[policy.find(":")-1]
    password = policy[policy.find(":")+2:]
    count = 0
    for character in password:
        if character == letter:
            count += 1

    if (count <= max):
        if (count >= min):
            valid_passwords += 1



# Part one
print(valid_passwords)






        
    # count the number of times the letter occurs.
    # check that the value lies between the minimum and maximum.

