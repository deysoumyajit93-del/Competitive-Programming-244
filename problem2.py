#Remove Duplicates Using a Hash Set
'''Students register for a technical fest through an online form. Some students submit
the form multiple times, resulting in duplicate roll numbers in an unsorted list.
Given an unsorted list of roll numbers, remove duplicates while preserving the order
of the first occurrence of each roll number.'''


n = int(input("Enter the number of students: "))
roll_numbers = list(map(int, input("Enter the roll numbers: ").split()))

seen = set()
result = []

for roll in roll_numbers:
    if roll not in seen:
        seen.add(roll)
        result.append(roll)

print("Roll numbers after removing duplicates:", result)
