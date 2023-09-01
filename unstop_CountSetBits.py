
#Count set Bits

""" Let input N = 5

then we have to count total set bits in digit 1 to 5

for (1) => (0001), set bits = 1
for (2) => (0010), set bits = 1
for (3) => (0011), set bits = 2
for (4) => (0100), set bits = 1
for (5) => (0101), set bits = 2
Total set bits = 7

Therefore, for N = 5, result is 7"""



n = int(input())
count = 0

for i in range(n):
    count += bin(i).count('1')

print(count)


