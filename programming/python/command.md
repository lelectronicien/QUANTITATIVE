
## **4. Conditions**

Conditions allow a program to make decisions.

### `if`**,&#x20;**`elif`**,&#x20;**`else`

```
price = 20100ema = 20000# Execute only if the condition is trueif price > ema:    print("Bullish")# Test another conditionelif price < ema:    print("Bearish")# Execute when none of the conditions matchelse:    print("Neutral")
```

Python uses indentation to determine which statements belong to each condition.

### **Nested conditions**

```
price = 20100ema = 20000volume = 1500if price > ema:    if volume > 1000:        print("Strong bullish signal")    else:        print("Weak bullish signal")
```

### **Conditional expression**

```
profit = 150# Compact if/else expressionresult = "Win" if profit > 0 else "Loss"print(result)  # Win
```

### `match`**&#x20;and&#x20;**`case`

Pattern matching was introduced in Python 3.10.

```
direction = "long"match direction:    case "long":        print("Buy order")    case "short":        print("Sell order")    case "flat":        print("No position")    case _:        print("Unknown direction")
```

`case _` acts as a wildcard matching anything not handled by earlier cases. `match` can also match structured data, not just simple values.

## **5. Loops**

Loops repeat operations.

### `for`**&#x20;— Iterate over a sequence**

```
prices = [100, 105, 110, 115]# Visit each pricefor price in prices:    print(price)
```

### `while`**&#x20;— Repeat while a condition remains true**

```
capital = 1000while capital < 1500:    capital += 100    print(capital)
```

A `while` loop can run indefinitely if its condition never becomes false.

### `break`**&#x20;— Exit a loop**

```
for price in [100, 105, 110, 115]:    if price == 110:        break  # Stop the loop    print(price)
```

Output: `100`, `105`.

### `continue`**&#x20;— Skip the current iteration**

```
for number in range(5):    if number == 2:        continue  # Skip number 2    print(number)
```

Output: `0`, `1`, `3`, `4`.

### `pass`**&#x20;— Do nothing**

```
def future_strategy():    pass  # Placeholder for future implementation
```

### `enumerate()`**&#x20;and&#x20;**`zip()`

These two built-in functions are especially useful when working with loops.

```
prices = [100, 105, 110]volumes = [500, 600, 700]# enumerate(): Get index and valuefor index, price in enumerate(prices):    print(index, price)# zip(): Iterate through two collections togetherfor price, volume in zip(prices, volumes):    print(price, volume)
```

## **6. Functions**

Functions organize reusable code into named blocks.

### `def`**&#x20;— Define a function**

```
def calculate_profit(entry, exit_price, quantity):    profit = (exit_price - entry) * quantity    return profitresult = calculate_profit(100, 110, 2)print(result)  # 20
```

`def` creates the function. Its body executes when you call the function.

### `return`**&#x20;— Return a result**

```
def square(number):    return number ** 2result = square(5)print(result)  # 25
```

`return` immediately exits the function and provides a result to its caller. Without an explicit `return`, a function returns `None`.

### **Default parameters**

```
def calculate_fee(quantity, fee_per_contract=1.5):    return quantity * fee_per_contractprint(calculate_fee(2))       # 3.0print(calculate_fee(2, 2.0))  # 4.0
```

### `lambda`**&#x20;— Anonymous function**

```
# Regular functiondef square(x):    return x ** 2# Equivalent lambda functionsquare_lambda = lambda x: x ** 2print(square_lambda(5))  # 25
```

A lambda function contains a single expression. It is often useful for short operations such as sorting.

```
trades = [    {"profit": 100},    {"profit": -50},    {"profit": 200}]# Sort trades by profitsorted_trades = sorted(    trades,    key=lambda trade: trade["profit"])print(sorted_trades)
```

### `*args`**&#x20;— Variable positional arguments**

```
def calculate_total(*args):    return sum(args)print(calculate_total(10, 20))          # 30print(calculate_total(10, 20, 30, 40))  # 100
```

Inside the function, `args` is a tuple.

### `**kwargs`**&#x20;— Variable keyword arguments**

```
def create_trade(**kwargs):    for key, value in kwargs.items():        print(key, value)create_trade(    symbol="MNQ",    direction="long",    quantity=2,    entry=20000)
```

Inside the function, `kwargs` is a dictionary.

### **Type hints**

```
def calculate_return(    entry: float,    exit_price: float) -> float:    return (exit_price - entry) / entry
```

Type hints document expected types and help static analysis tools. Python does not automatically enforce them at runtime.

## **7. Lists and dictionaries**

These methods manipulate collections.

### **List methods**

| Method             | Purpose                            |
| ------------------ | ---------------------------------- |
| `append(x)`        | Add one element to the end         |
| `extend(iterable)` | Add elements from another iterable |
| `insert(i, x)`     | Insert an element at a position    |
| `remove(x)`        | Remove the first matching element  |
| `pop(i)`           | Remove and return an element       |
| `sort()`           | Sort the list in place             |
| `reverse()`        | Reverse the list in place          |
| `count(x)`         | Count occurrences                  |
| `index(x)`         | Find the first matching index      |
| `clear()`          | Remove all elements                |
| `copy()`           | Create a shallow copy              |

```
prices = [100, 105, 110]# Add one elementprices.append(115)# Add multiple elementsprices.extend([120, 125])# Insert 102 at index 1prices.insert(1, 102)# Remove the first occurrence of 105prices.remove(105)# Remove and return the last elementlast_price = prices.pop()# Sort in ascending orderprices.sort()# Reverse the current orderprices.reverse()# Count occurrences of 100count = prices.count(100)# Find the index of 110index = prices.index(110)# Create a shallow copynew_prices = prices.copy()# Remove all elementsprices.clear()
```

Most methods that modify a list in place, including `append()` and `sort()`, return `None`.

### **Dictionary methods**

| Method         | Purpose                                   |
| -------------- | ----------------------------------------- |
| `get()`        | Retrieve a value with an optional default |
| `keys()`       | Return a view of keys                     |
| `values()`     | Return a view of values                   |
| `items()`      | Return a view of key-value pairs          |
| `update()`     | Add or overwrite entries                  |
| `pop()`        | Remove a key and return its value         |
| `popitem()`    | Remove and return the last inserted pair  |
| `setdefault()` | Get a value or insert a default           |
| `copy()`       | Create a shallow copy                     |
| `clear()`      | Remove all entries                        |

```
trade = {    "entry": 20000,    "exit": 20100,    "quantity": 2}# Retrieve a valueentry = trade.get("entry")# Retrieve a missing key with a defaultstop = trade.get("stop", 0)# Iterate over keysfor key in trade.keys():    print(key)# Iterate over valuesfor value in trade.values():    print(value)# Iterate over key-value pairsfor key, value in trade.items():    print(key, value)# Update the dictionarytrade.update({"quantity": 3})# Remove a key and return its valuequantity = trade.pop("quantity")# Insert a default only if the key is missingtrade.setdefault("direction", "long")
```

## **8. File operations**

Python can read and write text files, CSV files, binary files, and other formats.

### `open()`**&#x20;— Open a file**

```
# Open a text file for readingfile = open("trades.txt", "r", encoding="utf-8")# Read the entire filecontent = file.read()# Close the filefile.close()
```

### **Common file modes**

| Mode   | Purpose                              |
| ------ | ------------------------------------ |
| `"r"`  | Read an existing file                |
| `"w"`  | Write, overwriting existing content  |
| `"a"`  | Append to the end                    |
| `"x"`  | Create a new file; fail if it exists |
| `"b"`  | Binary mode                          |
| `"t"`  | Text mode (default)                  |
| `"r+"` | Read and write an existing file      |

### `read()`**,&#x20;**`readline()`**,&#x20;**`readlines()`

```
with open("trades.txt", "r", encoding="utf-8") as file:    # Read the entire file    content = file.read()    # Read the next line (empty here after read())    next_line = file.readline()
```

```
with open("trades.txt", "r", encoding="utf-8") as file:    # Read all lines into a list    lines = file.readlines()    for line in lines:        print(line.strip())
```

### `write()`**&#x20;— Write to a file**

```
with open("results.txt", "w", encoding="utf-8") as file:    file.write("Trading Results\n")    file.write("Profit: 250\n")    file.write("Loss: -100\n")
```

### `close()`**&#x20;— Close a file**

```
file = open("results.txt", "r", encoding="utf-8")content = file.read()file.close()
```

The recommended approach is `with open(...) as file:`. It automatically closes the file when the block finishes, even if an exception occurs.

### **CSV example**

```
import csvtrades = [    ["symbol", "profit"],    ["MNQ", 150],    ["MES", -50],    ["MNQ", 200]]# Write CSV datawith open("trades.csv", "w", newline="", encoding="utf-8") as file:    writer = csv.writer(file)    writer.writerows(trades)# Read CSV datawith open("trades.csv", "r", newline="", encoding="utf-8") as file:    reader = csv.DictReader(file)    for row in reader:        print(row["symbol"], row["profit"])
```

Values read from a CSV file are strings by default, so convert them before numerical calculations.

## **9. Error handling**

Error handling prevents expected failures from unexpectedly terminating a program.

### `try`**&#x20;and&#x20;**`except`

```
try:    number = int("abc")except ValueError:    print("Invalid number")
```

The `try` block executes first. If a matching exception occurs, the corresponding `except` block handles it.

### `else`**&#x20;and&#x20;**`finally`

```
try:    result = 100 / 2except ZeroDivisionError:    print("Cannot divide by zero")else:    # Runs only when no exception occurs    print("Result:", result)finally:    # Runs whether or not an exception occurs    print("Calculation finished")
```

### `raise`**&#x20;— Generate an exception**

```
def calculate_position_size(capital, risk_fraction):    if capital <= 0:        raise ValueError("Capital must be positive")    if not 0 < risk_fraction <= 1:        raise ValueError("Risk fraction must be between 0 and 1")    return capital * risk_fraction
```

### **Common exceptions**

| Exception           | Meaning                            |
| ------------------- | ---------------------------------- |
| `ValueError`        | Invalid value                      |
| `TypeError`         | Incompatible type or operation     |
| `ZeroDivisionError` | Division by zero                   |
| `IndexError`        | Sequence index outside valid range |
| `KeyError`          | Missing dictionary key             |
| `FileNotFoundError` | File does not exist                |
| `AttributeError`    | Object has no requested attribute  |
| `ImportError`       | Import failed                      |
| `NameError`         | Name is not defined                |

Avoid catching every exception with a bare `except:` unless you have a specific reason. Catching known exceptions makes debugging easier.

## **10. Object-oriented programming (OOP)**

Object-oriented programming organizes code around objects that contain data and behavior.

### `class`**&#x20;— Define a class**

```
class Trade:    # Constructor: Initialize a new object    def __init__(self, entry, exit_price, quantity):        # self refers to the current instance        self.entry = entry        self.exit_price = exit_price        self.quantity = quantity    # Instance method    def calculate_profit(self):        return (            self.exit_price - self.entry        ) * self.quantity# Create an objecttrade1 = Trade(100, 110, 2)# Access an attributeprint(trade1.entry)  # 100# Call a methodprint(trade1.calculate_profit())  # 20
```

### **Key OOP concepts**

| Concept         | Purpose                                               |
| --------------- | ----------------------------------------------------- |
| `class`         | Defines a blueprint for objects                       |
| Object          | An instance of a class                                |
| `__init__()`    | Initializes an instance                               |
| `self`          | Refers to the current instance by convention          |
| Attribute       | Data stored on an object                              |
| Method          | Function defined inside a class                       |
| Inheritance     | Create a class based on another class                 |
| `super()`       | Access methods of a parent class                      |
| `@property`     | Define managed attribute access                       |
| `@staticmethod` | Define a method without an implicit instance argument |
| `@classmethod`  | Define a method receiving the class                   |

### **Inheritance and&#x20;**`super()`

```
# Parent classclass Position:    def __init__(self, symbol, quantity):        self.symbol = symbol        self.quantity = quantity    def describe(self):        return f"{self.quantity} contracts of {self.symbol}"# Child classclass LongPosition(Position):    def __init__(self, symbol, quantity, entry):        # Initialize attributes from the parent class        super().__init__(symbol, quantity)        self.entry = entry    def unrealized_profit(self, current_price, point_value):        return (            current_price - self.entry        ) * self.quantity * point_valueposition = LongPosition("MNQ", 2, 20000)print(position.describe())print(position.unrealized_profit(20100, 2))  # 400
```

The `point_value` parameter represents the monetary value of one full price point per contract.

### `@property`

```
class Account:    def __init__(self, balance):        self._balance = balance    @property    def balance(self):        return self._balanceaccount = Account(25000)print(account.balance)  # 25000
```

`@property` lets a method be accessed using attribute syntax.

## **11. Modules**

A module is a Python file containing reusable code. A package organizes related modules.

### `import`

```
# Import an entire moduleimport mathprint(math.sqrt(25))  # 5.0
```

### `from`

```
# Import a specific functionfrom math import sqrtprint(sqrt(25))  # 5.0
```

### `as`

```
# Assign an aliasimport math as mprint(m.sqrt(25))  # 5.0
```

### `math`**&#x20;— Mathematical functions**

| Function            | Purpose                  |
| ------------------- | ------------------------ |
| `math.sqrt(x)`      | Square root              |
| `math.pow(x, y)`    | Power, returning a float |
| `math.log(x)`       | Natural logarithm        |
| `math.log10(x)`     | Base-10 logarithm        |
| `math.exp(x)`       | Exponential              |
| `math.ceil(x)`      | Round upward             |
| `math.floor(x)`     | Round downward           |
| `math.factorial(n)` | Factorial                |
| `math.sin(x)`       | Sine                     |
| `math.cos(x)`       | Cosine                   |
| `math.pi`           | Mathematical constant π  |
| `math.e`            | Euler's number           |

```
import mathprint(math.sqrt(16))     # 4.0print(math.log(math.e))  # 1.0print(math.exp(2))print(math.ceil(4.2))    # 5print(math.floor(4.8))   # 4print(math.factorial(5)) # 120
```

### `random`**&#x20;— Pseudorandom numbers**

```
import random# Random integer between 1 and 10, inclusiveprint(random.randint(1, 10))# Random float between 0 and 1print(random.random())# Random float between two valuesprint(random.uniform(10, 20))# Select one elementprint(random.choice(["long", "short"]))# Shuffle a list in placenumbers = [1, 2, 3, 4]random.shuffle(numbers)# Draw from a Gaussian distributionvalue = random.gauss(0, 1)print(value)
```

For reproducible simulations:

```
import randomrng = random.Random(42)print(rng.random())
```

The standard `random` module is useful for simulation, but not cryptographic security.

### `datetime`**&#x20;— Dates and times**

```
from datetime import datetime, date, timedelta# Current local date and timenow = datetime.now()# Today's datetoday = date.today()# Create a datestart = date(2026, 1, 1)# Add 10 daysfuture = start + timedelta(days=10)# Convert date to formatted textformatted = now.strftime("%Y-%m-%d %H:%M:%S")# Parse text into a datetime objecttimestamp = datetime.strptime(    "2026-11-20 09:30",    "%Y-%m-%d %H:%M")print(now)print(today)print(future)print(formatted)print(timestamp)
```

For trading applications, use timezone-aware timestamps when comparing market sessions across timezones.

## **12. Advanced Python**

These concepts are useful when building larger applications, research systems, and data pipelines.

### **Generators — Produce values lazily**

A generator yields values one at a time rather than creating the entire collection immediately.

```
def generate_prices():    yield 100    yield 105    yield 110prices = generate_prices()print(next(prices))  # 100print(next(prices))  # 105print(next(prices))  # 110
```

`yield` suspends the function and preserves its state until the next value is requested.

A generator can also be written using a generator expression:

```
squares = (x ** 2 for x in range(5))for value in squares:    print(value)
```

### **Decorators — Modify function behavior**

A decorator wraps or transforms a function.

```
from functools import wrapsdef log_execution(func):    @wraps(func)    def wrapper(*args, **kwargs):        print("Function started")        result = func(*args, **kwargs)        print("Function finished")        return result    return wrapper@log_executiondef calculate_profit(entry, exit_price):    return exit_price - entryprint(calculate_profit(100, 120))
```

`@log_execution` applies the decorator to the function immediately below it.

Decorators are frequently used for logging, validation, caching, authentication, and timing.

### **Iterators — Traverse collections**

An iterator is an object that returns successive elements using `next()`.

```
numbers = [10, 20, 30]# Create an iteratoriterator = iter(numbers)# Retrieve elementsprint(next(iterator))  # 10print(next(iterator))  # 20print(next(iterator))  # 30
```

After the final element, another `next(iterator)` raises `StopIteration`.

A `for` loop handles this automatically.

### **Context managers — Manage resources**

Context managers define how resources are entered and cleaned up.

```
from contextlib import contextmanager@contextmanagerdef trading_session():    print("Session started")    try:        yield    finally:        print("Session ended")with trading_session():    print("Executing strategy")
```

The `with` statement invokes the context manager and ensures its cleanup logic runs when the block exits.

### **Asynchronous programming —&#x20;**`async`**&#x20;and&#x20;**`await`

Asynchronous programming is useful when a program spends time waiting for I/O operations, such as network responses.

```
import asyncioasync def fetch_market_data():    print("Requesting data")    # Simulate a two-second I/O wait    await asyncio.sleep(2)    print("Data received")    return [100, 105, 110]async def main():    prices = await fetch_market_data()    print(prices)asyncio.run(main())
```

`async def` defines a coroutine function. `await` suspends the current coroutine while waiting for an awaitable operation.

### **Running concurrent asynchronous tasks**

```
import asyncioasync def task(name, delay):    await asyncio.sleep(delay)    return f"{name} completed"async def main():    results = await asyncio.gather(        task("NASDAQ", 2),        task("S&P 500", 1),        task("Gold", 3)    )    print(results)asyncio.run(main())
```

All three tasks can wait concurrently, so this example finishes in approximately three seconds rather than six.

Asynchronous programming does not automatically make CPU-intensive numerical calculations faster.

## **Python for quantitative finance: putting the concepts together**

The following example combines variables, lists, dictionaries, loops, functions, conditions, and error handling to calculate trading performance.

```
# -----------------------------------------    losing_trades = len(losses)    # Calculate win rate    win_rate = winning_trades / total_trades    # Calculate total net profit    net_profit = sum(trades)    # Calculate average win and loss    average_win = (        sum(wins) / winning_trades        if winning_trades > 0 else 0    )    average_loss = (        abs(sum(losses) / losing_trades)        if losing_trades > 0 else 0    )    # Calculate expected profit per trade    expectancy = net_profit / total_trades    # Calculate profit factor    gross_profit = sum(wins)    gross_loss = abs(sum(losses))    profit_factor = (        gross_profit / gross_loss        if gross_loss > 0 else float("inf")    )    # Return all statistics as a dictionary    return {        "total_trades": total_trades,        "win_rate": win_rate,        "net_profit": net_profit,        "average_win": average_win,        "average_loss": average_loss,        "expectancy": expectancy,        "profit_factor": profit_factor    }# Run the analysisresults = analyze_trades(trades)# Display resultsfor metric, value in results.items():    print(f"{metric}: {value:.2f}")
```

OUTPUT

Total trades

## **7**

Win rate

## **57.14%**

Net profit

## **$450**

Average win

## **$181.25**

Average loss

## **$91.67**

Expectancy / trade

## **$64.29**

Profit factor

## **2.64**

These results are illustrative, not evidence of a statistically reliable strategy. The sample contains only seven trades, and the code assumes the profit and loss values already include any relevant costs.

## **Quick reference: what to learn first**

| Learning stage       | Topics                           | Main objective                                                |
| -------------------- | -------------------------------- | ------------------------------------------------------------- |
| Beginner             | 1–5                              | Understand Python syntax and program flow                     |
| Intermediate         | 6–9                              | Write reusable functions and process data                     |
| Software development | 10–11                            | Organize larger programs                                      |
| Advanced             | 12                               | Build efficient applications and data pipelines               |
| Quantitative finance | NumPy, pandas, SciPy, statistics | Analyze market data, simulate strategies, and backtest models |

For your quantitative finance studies, the most important next step after these 12 categories is learning **NumPy arrays, pandas DataFrames, statistical distributions, and Monte Carlo simulation**. Those tools allow you to move from basic Python programs to systematic trading research.