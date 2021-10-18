print(0.1+0.1+0.1 == 0.3)

print("{0:0.30f}".format(0.1))
print("{0:0.30f}".format(0.3))

print(round(0.1 * 3, 1) == round(0.3, 1))

months = ['Jan', 'Feb', 'March', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for month in months:
    print(month, end=" ")

print("\n")

for i, month in enumerate(months):
    print("{}월은 영어로 {}". format(i + 1, month))

print("\n")

for i in range(len(months)):
    print("{}".format(months[i], end=" "))
