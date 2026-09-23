m = int(input("No. of rows: "))
n = int(input("No. of columns: "))
base = int(input("Enter Base Address: "))
w = int(input("Enter the element size in bytes: "))

i, j = map(int, input("Enter row index and column index: ").split())

address = base + w * ((i * n) + j)
print(f"Address of A[{i}][{j}] = {address}")
