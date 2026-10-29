# Two Sum Using a Hash Map
'''An online shopping portal needs to identify two products whose prices add up exactly
to a customer’s gift-card balance.
Given a list of distinct product prices and a target amount, find the indices of two
prices whose sum equals the target.'''



n = int(input("Enter the number of products: "))
prices = list(map(int, input("Enter the product prices: ").split()))
target = int(input("Enter the target amount: "))

seen = {}

for i in range(n):
    complement = target - prices[i]

    if complement in seen:
        print([seen[complement], i])
        break

    seen[prices[i]] = i

