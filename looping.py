i = 1
while i <= 5:
    print(i * '*')
    i += 1


i = 1
while i <= 1_0:  # see `underscore` used for readability e.g. 1_000
    print(i)
    i += 1

for item in "Python":
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for x in range(4):
    for y in range(3):
        print(f"{x} {y}")

given_list = [5, 2, 5, 2, 2]
for x in given_list:
    print(x * 'x')

# Little new for:else
names = ["AJohn", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")
