# 1. Basic Python functions

Built-in functions are available without imports.

| Function | Purpose | Example |
| --- | --- | --- |
| `print()` | Display output | `print("Hello")` |
| `input()` | Read a string from the user | `input("Name: ")` |
| `len()` | Count items | `len([1, 2, 3])` |
| `type()` | Inspect an object's type | `type(10)` |
| `range()` | Produce integer sequences | `range(5)` |

## print()

```python
print("Hello World")
print(100)
price = 20000
quantity = 2
print("Price:", price, "Quantity:", quantity)
print(f"Price = {price}, Quantity = {quantity}")
print(10, 20, 30, sep="-")  # 10-20-30
print("Hello", end=" ")
print("World")  # Together: Hello World
```

## input()

The examples below prompt for interactive input.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
price = float(input("Enter price: "))
print(name, age, price)
```

## len()

```python
prices = [100, 105, 110, 115]
print(len(prices))  # 4
print(len("NASDAQ"))  # 6
trade = {"entry": 100, "exit": 110}
print(len(trade))  # 2
```

## type()

```python
price = 20000.5
quantity = 2
symbol = "MNQ"
active = True
print(type(price))     # <class 'float'>
print(type(quantity))  # <class 'int'>
print(type(symbol))    # <class 'str'>
print(type(active))    # <class 'bool'>
```

## range()

```python
for i in range(5):
    print(i)  # 0 through 4, on separate lines

for i in range(2, 6):
    print(i)  # 2 through 5

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```
