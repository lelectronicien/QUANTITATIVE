## **2. Variables and data types**

A variable is a name that refers to a value. Python determines its type dynamically.

| Type    | Description                   | Example          |
| ------- | ----------------------------- | ---------------- |
| `int`   | Integer number                | `25`             |
| `float` | Floating-point number         | `25.75`          |
| `str`   | Text                          | `"NASDAQ"`       |
| `bool`  | Boolean                       | `True`, `False`  |
| `list`  | Mutable ordered collection    | `[1, 2, 3]`      |
| `tuple` | Immutable ordered collection  | `(1, 2, 3)`      |
| `dict`  | Key-value collection          | `{"price": 100}` |
| `set`   | Collection of unique elements | `{1, 2, 3}`      |

### `int`**&#x20;— Integer**

```python
quantity = 5
loss = -150
# Convert text to 
integervalue = int("100")
# Convert float to integer (truncates toward zero)
price = int(100.95)  
# 100
```

### `float`**&#x20;— Decimal number**

```python
entry_price = 20150.75
exit_price = 20200.25
# Calculate price difference
difference = exit_price - entry_price
print(difference)  
# 49.5
# Convert text into a float
price = float("20150.75")
```

Floating-point arithmetic can have small precision errors. For exact decimal arithmetic, such as certain financial calculations, Python provides `decimal.Decimal`.

### `str`**&#x20;— String**

```python
symbol = "MNQ"
# Convert text to uppercase
print(symbol.upper())  
# MNQ
# Convert text to lowercase
print(symbol.lower())  
# mnq
# Extract part of a string
print(symbol[0:2])  
# MN
# Join strings
name = "NASDAQ" + " Futures"
# Insert variables into strings
print(f"Trading {symbol}")
```

### `bool`**&#x20;— Boolean**

```python
market_open = True
trade_active = False
# Comparison returns a boolean
price = 200 
is_above = price > 150
print(is_above)  
# True
```

### `list`**&#x20;— Mutable ordered collection**

```python
prices = [100, 105, 110, 115]
# Access the first element
print(prices[0])  
# 100
# Access the last element
print(prices[-1])  
# 115
# Change an element
prices[0] = 102
# Add an element
prices.append(120)
# Remove an element by value
prices.remove(105)
# Extract a slice
print(prices[1:3])
```

### `tuple`**&#x20;— Immutable ordered collection**

```python
trade = (20000, 20100, 2)
# Access values
entry = trade[0]
exit_price = trade[1]
quantity = trade[2]
# Unpack a tuple
entry, exit_price, quantity = trade
# Cannot modify an element
trade[0] = 20500  
# TypeError
```

### `dict`**&#x20;— Dictionary**

```python
trade = {   "symbol": "MNQ",
            "entry": 20000,    
            "exit": 20100,    
            "quantity": 2
        }
# Access a value
print(trade["entry"])
# Modify a value
trade["entry"] = 20050
# Add a new key
trade["direction"] = "long"
# Retrieve a value safely
print(trade.get("stop_loss", None))
```

### `set`**&#x20;— Unique elements**

```python
symbols = {"MNQ", "MES", "MNQ", "MGC"}
# Duplicate MNQ is automatically removed
print(symbols)
# Add an element
symbols.add("MCL")
# Remove an element if present
symbols.discard("MES")
# Check membership
print("MNQ" in symbols)  
# True
```


