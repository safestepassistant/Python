# Example of complex numbers in Python
a = 5 + 3j
print(type(a))
print(a.imag)
print(a.real)
print(a.conjugate())
print(a + (2 + 4j))
print(a * (2 + 4j))
# Example of complex numbers in Python
b = complex(2, 4)
print(type(b))
print(b.imag)
print(b.real)
print(b)
print(b.conjugate())
print(b + (5 + 3j))
print(b * (5 + 3j))
print(a == b)
# Example of numeric types in Python
x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex
print(type(x))
print(type(y))
print(type(z))
print(x + y)
print(y * z)
print(x / 3)
print(z - x)
print(int(y))
print(float(x))
print(complex(x))
print(isinstance(x, int))
print(isinstance(y, float))
print(isinstance(z, complex))
print(isinstance(y, int))
print(isinstance(z, float))
print(isinstance(x, complex))
# Example of numeric operations in Python
m = 7
n = 2
print(m + n)
print(m - n)
print(m * n)
print(m / n)
print(m // n)
print(m % n)
print(m ** n)
print(abs(-m))
print(round(3.14159, 3))
print(pow(m, n))
print(divmod(m, n))
print(m > n)
print(m < n)
print(m == n)
print(m != n)
print(m >= n)
print(m <= n)
print(m & n)
print(m | n)
print(m ^ n)
print(~m)
print(m << 1)
print(m >> 1)
print(bin(m))
print(oct(m))
print(hex(m))
# Example of type conversion in Python
p = 15
q = 4.5
r = 1 + 2j
print(float(p)) # int to float
print(int(q))   # float to int 
print(complex(p)) # int to complex
print(complex(q)) # float to complex
print(int(r.real)) # complex to int
print(float(r.imag)) # complex to float
print(complex(int(q), int(p))) # float to complex using int values

# Example of using math module in Python
import math
print(math.sqrt(16))
print(math.factorial(5))
print(math.gcd(48, 18))
print(math.sin(math.pi / 2))
print(math.cos(0))
print(math.log(100, 10))
print(math.exp(2))
print(math.ceil(4.3))
print(math.floor(4.7))
print(math.pow(2, 3))
print(math.radians(180))
print(math.degrees(math.pi))
print(math.isclose(0.1 + 0.2, 0.3))
# Example of using random module in Python
import random
print(random.randint(1, 10))
print(random.uniform(1.0, 10.0))
print(random.choice(['apple', 'banana', 'cherry']))
print(random.sample(range(1, 100), 5))
print(random.random())
print(random.shuffle([1, 2, 3, 4, 5]))
print(random.seed(42))
# Example of using decimal module in Python
from decimal import Decimal, getcontext 
getcontext().prec = 6
d1 = Decimal('0.1')
d2 = Decimal('0.2')
print(d1 + d2)
print(d1 * d2)
print(d1 / d2)
print(d1 - d2)
print(d1 ** 2)
print(d1.quantize(Decimal('0.01')))
print(d1.sqrt())
print(d1.compare(d2))
print(d1 == d2)
print(d1 < d2)
print(d1, d2)
# Example of using fractions module in Python
from fractions import Fraction
f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
print(f1 + f2)
print(f1 * f2)
print(f1 / f2)
print(f1 - f2)
print(f1 == f2)
print(f1 < f2)
print(f1, f2)
print(f1.numerator)
print(f1.denominator)  
print(f1.limit_denominator(10))
print(f2.limit_denominator(10))
print(f1 + 1)
print(f2 - 1)
print(float(f1))
print(float(f2))   
# Example of using built-in numeric functions in Python
num = -15.67
print(abs(num))
print(round(num))
print(pow(2, 3))
print(divmod(15, 4))
print(int(num))
print(float(num))
print(complex(num))
print(isinstance(num, float))
print(isinstance(num, int))
print(isinstance(num, complex))
print(bin(10))
print(oct(10))
print(hex(10))
print(sum([1, 2, 3, 4, 5])) 
print(max(1, 5, 3, 9, 2))
print(min(1, 5, 3, 9, 2))
print(len([1, 2, 3, 4, 5]))
print(pow(3, 4, 5))  # (3^4) % 5
print(round(3.14159, 2))
print(int('1010', 2))  # binary to int
print(float('3.14'))
print(complex('1+2j'))









