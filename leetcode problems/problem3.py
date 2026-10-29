#Binary Search in a Descending Array
'''A gaming leaderboard stores player scores in descending order. Your task is to find
the index of a given target score efficiently.
Given a descending-sorted array of distinct scores and a target score, return its index
if it exists; otherwise, return −1.'''


n = int(input("Enter the number of players: "))
scores = list(map(int, input("Enter the scores in descending order: ").split()))
target = int(input("Enter the target score: "))

left = 0
right = n - 1
result = -1

while left <= right:
    mid = (left + right) // 2

    if scores[mid] == target:
        result = mid
        break
    elif scores[mid] < target:
        right = mid - 1
    else:
        left = mid + 1

print("Index:", result)
