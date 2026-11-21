# 3. Python operators

## Arithmetic

| Operator | Meaning | Example |
| --- | --- | --- |
| `+` | Addition | `10 + 3` |
| `-` | Subtraction | `10 - 3` |
| `*` | Multiplication | `10 * 3` |
| `/` | True division | `10 / 3` |
| `//` | Floor division | `10 // 3` |
| `%` | Remainder | `10 % 3` |
| `**` | Exponentiation | `10 ** 3` |

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
print(-10 // 3)  # -4: floor division rounds down
```

## Comparison

```python
price = 200
print(price == 200)  # True
print(price != 100)  # True
print(price > 150)   # True
print(price < 150)   # False
print(price >= 200)  # True
print(price <= 200)  # True
```

## Logical operators

```python
price = 200
volume = 1000
buy = price > 150 and volume > 500
signal = price > 250 or volume > 500
market_closed = not True
print(buy)            # True
print(signal)         # True
print(market_closed)  # False
```

## Assignment operators

```python
capital = 1000
capital += 100
capital -= 50
capital *= 2
capital /= 2
capital //= 3
capital %= 7
capital **= 2
print(capital)
```

Use `in` and `not in` for membership, `is` and `is not` for object identity, and `==` for value equality.
