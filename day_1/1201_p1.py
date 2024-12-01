# /usr/bin/env python3

# Create variables to store the data
data = ""
list1 = []
list2 = []

# Open the file and read the data
with open("1201_input.txt") as file:
    data = file.read()

# Split the data into two lists
for line in data.splitlines():
    left, right = line.split()
    list1.append(int(left))
    list2.append(int(right))

# Sort the lists
list1.sort()
list2.sort()

index = 0
answer = 0

for item in list1:
    answer += abs(list1[index] - list2[index])
    index += 1

print(answer)