## **3. Operators**

Operators perform calculations, comparisons, and logical operations.

### **Arithmetic operators**

| Operator | Name               | Example   | Result     |
| -------- | ------------------ | --------- | ---------- |
| `+`      | Addition           | `10 + 3`  | `13`       |
| `-`      | Subtraction        | `10 - 3`  | `7`        |
| `*`      | Multiplication     | `10 * 3`  | `30`       |
| `/`      | True division      | `10 / 3`  | `3.333...` |
| `//`     | Floor division     | `10 // 3` | `3`        |
| `%`      | Modulo (remainder) | `10 % 3`  | `1`        |
| `**`     | Exponentiation     | `10 ** 3` | `1000`     |

```python
a = 10
b = 3
print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Remainder
print(a ** b)  # Power
```

Note that `//` rounds toward negative infinity: `-10 // 3` equals `-4`.

### **Comparison operators**

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | Equal                 |
| `!=`     | Not equal             |
| `>`      | Greater than          |
| `<`      | Less than             |
| `>=`     | Greater than or equal |
| `<=`     | Less than or equal    |

```python
price = 200
print(price == 200)  # True
print(price != 100)  # True
print(price > 150)   # True
print(price < 150)   # False
print(price >= 200)  # True
print(price <= 200)  # True
```

### **Logical operators**

| Operator | Purpose                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses a Boolean condition        |

```python
price = 200
volume = 1000 
# Both conditions must be true
buy = price > 150 and volume > 500
# At least one condition must be true
signal = price > 250 or volume > 500 
# Reverse a condition
market_closed = not Trueprint(buy)           # Trueprint(signal)        # Trueprint(market_closed) # False
```

### **Assignment operators**

```
capital = 1000capital += 100  # capital = capital + 100capital -= 50   # capital = capital - 50capital *= 2    # capital = capital * 2capital /= 2    # capital = capital / 2capital //= 3   # Floor division assignmentcapital %= 7    # Modulo assignmentcapital **= 2   # Exponentiation assignment
```

Other useful operators include `in` and `not in` for membership, and `is` and `is not` for object identity. `is` should not be used as a replacement for `==`.
