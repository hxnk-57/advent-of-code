S = [1,3,4,5,11,15,18]
target = 20
elements = {}

for s in S:
    elements({s: target-s})

print(elements)