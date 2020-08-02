# PyClassicRound

The current implementation of round() function in Python 3 uses Banker's rounding i.e integers are rounded to the nearest even integer, this package allows you to round off numbers the classical way.

### Installation

PyClassicRound has no dependencies.

```sh
> pip install PyClassicRound
```

### Usage (example)

```sh
> from PyClassicRound import classic_round

> classic_round(2.55, 1) #outputs 2.6 whereas python 3's round() outputs 2.5
```
#### OR

```sh
> from PyClassicRound import classic_round as cround

> cround(2.55, 1) #outputs 2.6 whereas python 3's round() outputs 2.5
```

### Parameters

- Number that needs to be rounded off
- Upto how many decimal places (__optional__) (**defaults to 2 decimal points** (Hundredths Place))

Input parameters can be in any format i.e. integer, float, string etc.

Output will be:
- integer: if decimal point is 0
- on successful operation: float
- None: if the input value cannot be resolved / rounded off for ex. strings -> ("", " ", "abc")

### License
MIT
