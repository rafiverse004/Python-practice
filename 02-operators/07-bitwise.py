# Bitwise operators work directly with the binary representation of integers.

a = 5      # 0101
b = 3      # 0011

# Bitwise AND
print("a & b =", a & b)

# Bitwise OR
print("a | b =", a | b)

# Bitwise XOR
print("a ^ b =", a ^ b)

# Bitwise NOT
print("~a =", ~a)

# Left shift
print("a << 1 =", a << 1)

# Right shift
print("a >> 1 =", a >> 1)

# Binary representation helps understand the result
print("\nBinary of a:", bin(a))
print("Binary of b:", bin(b))
print("Binary of a & b:", bin(a & b))
print("Binary of a | b:", bin(a | b))