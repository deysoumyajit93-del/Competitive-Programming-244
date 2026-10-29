#  Single Number (Bit Manipulation)
''' An office RFID gate logs every employee twice: once when entering and once when
 leaving. However, one employee’s ID appears only once.
 Given a list of n employee IDs in which every ID appears exactly twice except one,
ind the ID that appears only once.'''



n = int(input("Enter the number of employee IDs: "))
ids = list(map(int, input("Enter the employee IDs: ").split()))

result = 0

for id in ids:
    result = result ^ id

print("Employee ID appearing only once:", result)
