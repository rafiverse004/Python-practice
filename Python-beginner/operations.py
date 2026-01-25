"""
OPERATORS IN PYTHON

Arithmetic Operators:
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulus (remainder)
**  Exponent (power)

Relational / Comparison Operators:
==  Equal to
!=  Not equal to
>   Greater than
<   Less than
>=  Greater than or equal to
<=  Less than or equal to

Assignment Operators:
=   Assign
+=  Add and assign
-=  Subtract and assign
*=  Multiply and assign
/=  Divide and assign
%=  Modulus and assign
**= Power and assign

Logical Operators:
not
and
or
"""


"""
ARITHMETIC OPERATORS
"""

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)
print("Exponent:", a ** b)


"""
RELATIONAL / COMPARISON OPERATORS
"""

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater or equal:", a >= b)
print("Less or equal:", a <= b)


"""
ASSIGNMENT OPERATORS
"""

c = 5
print("Initial c:", c)

c += 2
print("c += 2:", c)

c -= 3
print("c -= 3:", c)

c *= 2
print("c *= 2:", c)

c /= 4
print("c /= 4:", c)

c %= 2
print("c %= 2:", c)

c = 3
c **= 3
print("c **= 3:", c)


"""
LOGICAL OPERATORS
"""

x = True
y = False

print("not x:", not x)
print("x and y:", x and y)
print("x or y:", x or y)


"""
TYPE CONVERSION (IMPLICIT)

• Python automatically converts int to float
• Happens during operations with mixed types
"""

a = 2
b = 4.14

result = a + b
print("Sum:", result)
print("Type of result:", type(result))
