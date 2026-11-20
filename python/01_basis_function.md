
## **1. Basic functions**

Basic functions are built into Python. You can use them without importing a library.

| Function  | Purpose                          | Example                  |
| --------- | -------------------------------- | ------------------------ |
| `print()` | Displays output on the screen    | `print("Hello")`         |
| `input()` | Reads user input as a string     | `input("Name: ")`        |
| `len()`   | Returns the number of elements   | `len([1, 2, 3])` → `3`   |
| `type()`  | Returns the type of an object    | `type(10)` → `int`       |
| `range()` | Generates a sequence of integers | `range(5)` → 0 through 4 |

### `print()`**&#x20;— Display information**

```python
#Print text 
print("Hello World")
# Print a number 
print(100)
# Print multiple values
price = 20000 
quantity = 2 
print("Price:", price, "Quantity:", quantity)
# Insert variables into text using an f-string
print(f"Price = {price}, Quantity = {quantity}")
# Control the separator between values 
print(10, 20, 30, sep="-")  
# 10-20-30
# Change the ending character
print("Hello", end=" ")print("World")  # Hello World
```

### `input()`**&#x20;— Get information from the user**

```python
# Read text from the keyboard
name = input("Enter your name: ")
# input() always returns a string
age = input("Enter your age: ")
# Convert the string into an integer
age = int(age)
# Read a decimal number
price = float(input("Enter price: "))
print(name, age, price)
```

### `len()`**&#x20;— Count elements**

```python
prices = [100, 105, 110, 115]
# Number of elements in a list
print(len(prices))  
# 4
# Number of characters in a string
print(len("NASDAQ"))  
# 6
# Number of keys in a dictionary
trade = {"entry": 100, "exit": 110}
print(len(trade))  
# 2
```

### `type()`**&#x20;— Identify data types**

```python
price = 20000.5
quantity = 2
symbol = "MNQ"
active = Trueprint(type(price))     # <class 'float'>print(type(quantity))  # <class 'int'>print(type(symbol))    # <class 'str'>print(type(active))    # <class 'bool'>
```

### `range()`**&#x20;— Generate integer sequences**

```python
# range(stop)
for i in range(5):    print(i)  # 0, 1, 2, 3, 4
# range(start, stop)
for i in range(2, 6):    print(i)  # 2, 3, 4, 5
# range(start, stop, step)
for i in range(0, 10, 2):    print(i)  # 0, 2, 4, 6, 8
# Count backward
for i in range(5, 0, -1):    print(i)  # 5, 4, 3, 2, 1
```
