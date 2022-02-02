list_of_numbers = [1, 2, 3, 4, 5]

print(list_of_numbers)
print(list_of_numbers[0])
print(list_of_numbers[-1])  # returns last element of the list
print(list_of_numbers[-2])  # returns second last element of the list

print(f"Returns first three element {list_of_numbers[0:3]}")

print(1 in list_of_numbers)

for i in list_of_numbers:
    print(i)

list_of_numbers.clear()
print(list_of_numbers)

print("Testing range")
range_numbers = range(5, 10)  # start from 5 ends at 9
print(range_numbers)
for number in range_numbers:
    print(number)
