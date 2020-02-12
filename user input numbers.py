n1 = int(input("Pick a number\n"))
n2 = int(input("Pick a number\n"))


if n1 > n2:
    start = n2 
    stop = n1 
else:
    start = n1
    stop = n2

for number in range(start, stop + 1, 1):
    print(number)