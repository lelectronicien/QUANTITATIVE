# Python: control flow, functions, and advanced concepts

These examples target Python 3.10 or newer. Each Python code block is a standalone example unless otherwise noted.

## 4. Conditions

```python
price = 20100
ema = 20000
if price > ema:
    print("Bullish")
elif price < ema:
    print("Bearish")
else:
    print("Neutral")

volume = 1500
if price > ema:
    if volume > 1000:
        print("Strong bullish signal")
    else:
        print("Weak bullish signal")

profit = 150
result = "Win" if profit > 0 else "Loss"
print(result)
```

### Pattern matching (Python 3.10+)

```python
direction = "long"
match direction:
    case "long":
        print("Buy order")
    case "short":
        print("Sell order")
    case "flat":
        print("No position")
    case _:
        print("Unknown direction")
```

## 5. Loops

```python
for price in [100, 105, 110, 115]:
    print(price)

capital = 1000
while capital < 1500:
    capital += 100

for price in [100, 105, 110, 115]:
    if price == 110:
        break
    print(price)

for number in range(5):
    if number == 2:
        continue
    print(number)

def future_strategy():
    pass

prices = [100, 105, 110]
volumes = [500, 600, 700]
for index, price in enumerate(prices):
    print(index, price)
for price, volume in zip(prices, volumes):
    print(price, volume)
```

## 6. Functions

```python
def calculate_profit(entry, exit_price, quantity):
    return (exit_price - entry) * quantity

print(calculate_profit(100, 110, 2))  # 20

def calculate_fee(quantity, fee_per_contract=1.5):
    return quantity * fee_per_contract

print(calculate_fee(2))  # 3.0

square = lambda x: x ** 2
print(square(5))  # 25

trades = [{"profit": 100}, {"profit": -50}, {"profit": 200}]
print(sorted(trades, key=lambda trade: trade["profit"]))

def calculate_total(*args):
    return sum(args)

print(calculate_total(10, 20, 30))  # 60

def create_trade(**kwargs):
    return kwargs

print(create_trade(symbol="MNQ", direction="long", quantity=2))

def calculate_return(entry: float, exit_price: float) -> float:
    return (exit_price - entry) / entry
```

Type hints are not enforced automatically at runtime.

## 7. Lists and dictionaries

```python
prices = [100, 105, 110]
prices.append(115)
prices.extend([120, 125])
prices.insert(1, 102)
prices.remove(105)
last_price = prices.pop()
prices.sort()
prices.reverse()
count = prices.count(100)
index = prices.index(110)
new_prices = prices.copy()
prices.clear()

trade = {"entry": 20000, "exit": 20100, "quantity": 2}
entry = trade.get("entry")
stop = trade.get("stop", 0)
for key, value in trade.items():
    print(key, value)
trade.update({"quantity": 3})
quantity = trade.pop("quantity")
trade.setdefault("direction", "long")
```

Methods such as `append()` and `sort()` modify lists in place and return `None`.

## 8. Files and CSV

The following example creates files in the current directory.

```python
from pathlib import Path
import csv
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "trades.txt"
    path.write_text("Profit: 250\nLoss: -100\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    print(content)

    csv_path = Path(folder) / "trades.csv"
    trades = [["symbol", "profit"], ["MNQ", 150], ["MES", -50]]
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(trades)
    with csv_path.open("r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            print(row["symbol"], int(row["profit"]))
```

File modes: `r` read, `w` overwrite, `a` append, `x` create only, `b` binary, `r+` read/write. Prefer `with open(...)` for automatic cleanup.

## 9. Error handling

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number")

try:
    result = 100 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Calculation finished")

def calculate_position_size(capital, risk_fraction):
    if capital <= 0:
        raise ValueError("Capital must be positive")
    if not 0 < risk_fraction <= 1:
        raise ValueError("Risk fraction must be between 0 and 1")
    return capital * risk_fraction
```

Common exceptions: `ValueError`, `TypeError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `FileNotFoundError`, `AttributeError`, `ImportError`, `NameError`.

## 10. Object-oriented programming

```python
class Trade:
    def __init__(self, entry, exit_price, quantity):
        self.entry = entry
        self.exit_price = exit_price
        self.quantity = quantity

    def calculate_profit(self):
        return (self.exit_price - self.entry) * self.quantity

trade = Trade(100, 110, 2)
print(trade.calculate_profit())  # 20

class Position:
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity

class LongPosition(Position):
    def __init__(self, symbol, quantity, entry):
        super().__init__(symbol, quantity)
        self.entry = entry

    def unrealized_profit(self, current_price, point_value):
        return (current_price - self.entry) * self.quantity * point_value

position = LongPosition("MNQ", 2, 20000)
print(position.unrealized_profit(20100, 2))  # 400

class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

print(Account(25000).balance)
```

## 11. Modules

```python
import math
from math import sqrt
import math as m
import random
from datetime import date, datetime, timedelta

print(math.sqrt(16))
print(sqrt(25))
print(m.factorial(5))
rng = random.Random(42)
print(rng.random())
print(rng.gauss(0, 1))
start = date(2026, 1, 1)
print(start + timedelta(days=10))
timestamp = datetime.strptime("2026-11-20 09:30", "%Y-%m-%d %H:%M")
print(timestamp)
```

For market sessions, use timezone-aware datetimes. Pseudorandom number generators are useful for reproducible simulation, not cryptographic security.

## 12. Advanced Python

### Generators, decorators, and iterators

```python
from functools import wraps

def generate_prices():
    yield 100
    yield 105
    yield 110

for price in generate_prices():
    print(price)

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result
    return wrapper

@log_execution
def calculate_profit(entry, exit_price):
    return exit_price - entry

print(calculate_profit(100, 120))
iterator = iter([10, 20, 30])
print(next(iterator))
```

### Context managers

```python
from contextlib import contextmanager

@contextmanager
def trading_session():
    print("Session started")
    try:
        yield
    finally:
        print("Session ended")

with trading_session():
    print("Executing strategy")
```

### Asynchronous programming

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} completed"

async def main():
    results = await asyncio.gather(
        task("NASDAQ", 0.01),
        task("S&P 500", 0.01),
        task("Gold", 0.01),
    )
    print(results)

asyncio.run(main())
```

Asynchronous programming helps I/O-bound workloads, but does not automatically speed up CPU-intensive calculations.

## Quantitative finance example: trade statistics

The following hypothetical trades are net P&L amounts after any assumed costs.

```python
def analyze_trades(trades):
    if not trades:
        raise ValueError("At least one trade is required")
    wins = [pnl for pnl in trades if pnl > 0]
    losses = [pnl for pnl in trades if pnl < 0]
    gross_profit = sum(wins)
    gross_loss = -sum(losses)
    return {
        "total_trades": len(trades),
        "win_rate": len(wins) / len(trades),
        "net_profit": sum(trades),
        "average_win": gross_profit / len(wins) if wins else 0.0,
        "average_loss": gross_loss / len(losses) if losses else 0.0,
        "expectancy": sum(trades) / len(trades),
        "profit_factor": gross_profit / gross_loss if gross_loss else float("inf"),
    }

trades = [200, -100, 175, -75, 150, -100, 200]
results = analyze_trades(trades)
for metric, value in results.items():
    print(f"{metric}: {value:.2f}")
```

This seven-trade example is illustrative and too small to establish a reliable trading edge. Profit factor is infinite when gross loss is zero, which requires careful interpretation.

## Next steps

Learn NumPy, pandas, SciPy, statistical inference, and Monte Carlo simulation. For research, document assumptions, data provenance, costs, and out-of-sample validation.
