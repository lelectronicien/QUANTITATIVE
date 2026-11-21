# 2. Variables and data types

Python determines the type of a value at runtime.

| Type | Example | Description |
| --- | --- | --- |
| `int` | `25` | Integer |
| `float` | `25.75` | Floating-point number |
| `str` | `"MNQ"` | Text |
| `bool` | `True` | Boolean |
| `list` | `[1, 2]` | Mutable sequence |
| `tuple` | `(1, 2)` | Immutable sequence |
| `dict` | `{"price": 100}` | Key-value mapping |
| `set` | `{1, 2}` | Unique elements |

## Integers and floats

```python
quantity = 5
loss = -150
integer_value = int("100")  # Convert text to integer
price = int(100.95)  # 100: truncates toward zero
entry_price = 20150.75
exit_price = 20200.25
difference = exit_price - entry_price
print(difference)  # 49.5
converted_price = float("20150.75")
```

Floating-point values can have rounding errors. For exact decimal calculations, consider `decimal.Decimal`.

## Strings and booleans

```python
symbol = "MNQ"
print(symbol.upper())  # MNQ
print(symbol.lower())  # mnq
print(symbol[:2])      # MN
name = "NASDAQ" + " Futures"
print(f"Trading {symbol}")
market_open = True
trade_active = False
is_above = 200 > 150
print(is_above)  # True
```

## Lists

```python
prices = [100, 105, 110, 115]
print(prices[0])   # 100
print(prices[-1])  # 115
prices[0] = 102
prices.append(120)
prices.remove(105)
print(prices[1:3])  # [110, 115]
```

## Tuples

```python
trade = (20000, 20100, 2)
entry, exit_price, quantity = trade
print(entry, exit_price, quantity)
```

Tuples are immutable. Attempting `trade[0] = 20500` raises `TypeError`; that expression is intentionally not included in runnable examples.

## Dictionaries and sets

```python
trade = {
    "symbol": "MNQ",
    "entry": 20000,
    "exit": 20100,
    "quantity": 2,
}
print(trade["entry"])
trade["entry"] = 20050
trade["direction"] = "long"
print(trade.get("stop_loss"))  # None

symbols = {"MNQ", "MES", "MNQ", "MGC"}
symbols.add("MCL")
symbols.discard("MES")
print("MNQ" in symbols)  # True
```
