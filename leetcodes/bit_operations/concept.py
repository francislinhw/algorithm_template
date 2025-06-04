# AND

res = 5 & 3
print(res)

# ODD or EVEN
# if n & 1 == 0, then n is even
# if n & 1 == 1, then n is odds

# bitmask
mask = 0b1111

res = 5 & mask  # Take the last 4 bits of 5s

# OR

res = 5 | 3
print(res)

# Set k th bit to 1

n = 5
k = 2
n = n | (1 << k)  # Set the 2nd bit to 1
print(n)


# XOR
res = 5 ^ 3
print(res)

# Swap two numbers without using extra space
# a = a ^ b
# b = a ^ b  # b 變成 a
# a = a ^ b  # a 變成 b


# NOT
res = ~5
print(res)

# Left Shift
res = 5 << 1
print(res)

# n * 2^k
k = 2

res = 5 << k
print(res)


# Right Shift
res = 5 >> 1
print(res)

# divide by 2^k //
k = 2
res = 5 >> k
print(res)
print(5 // (2**k))
